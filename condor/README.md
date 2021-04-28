# Condor

The condor pool consists of:

- master, it contains the collector and the negotiator.
- schedd, submit jobs for users.
- worker, execute the jobs submitted.

## Condor deployment structure

The structure of the deployment consists of persistent volumes, configmaps,
deployments and services. There are some features added to this infrastructure
that are listed below:

- Condor exporter https://github.com/niclabs/htcondor-monitor/tree/master/CondorExporter/exporter/condor.
- singularity containers execution.
- condor with jupyter notebook that is used as scheduler.

The above features needed special configuration that will be mentioned below in **Special Features**.

### Configmaps

The configmaps contain the configuration files for each condor node.
The configuration files are the following:

- Role file that specifies the condor host, the daemon list.
- Singularity file for locating singularity. (worker specific)

### Deployments

It specifies the following:

- Application name that kubernetes can identify.
- Node affinity according to specified criteria (hostname, gpu, memory ....)
- containers and the volume mounting locations
- resources (request and limit)
- ports
- volumes

### Special Features

Some applications needed specific configuration, the modifications are:

- condor exporter needed uwsgi to publish condor metrics. Python and python
development tool needed to be installed. A bash script substituted the CMD
script executed at the launch of each condor container. It added lines in the
supervisord configuration file to run uwsgi.

- Jupyter notebook needed a special configuration file which is mounted on a 
specific directory.

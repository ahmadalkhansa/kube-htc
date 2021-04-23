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
- docker that is introduced to the execution pods.
- condor with jupyter notebook that is used as scheduler.

The above features needed special configuration that will be mentioned below in **Special Features**.

### Persistent Volumes

The persistent volume has two purposes: submission files input and output and execution of special scripts.
The scripts in this infrastructure is for running condor exporter on lunch.

**NOTE:** The scripts part can be avoided by creating a new image.  

### Configmaps

The configmaps contain the configuration files for each condor node.
The configuration files are the following:

- Role file that specifies the condor host, the daemon list and if there is docker(worker specific).
- Security file for authentication and integrity options.
- Authorization file for specifying authority for components.
- Singularity file for locating singularity. (worker specific)

### Deployments

It specifies the following:

- Application name that kubernetes can identify.
- Node affinity according to specified criteria (hostname, gpu, memory ....)
- containers and the volume mounting locations
- resources (request and limit)
- ports
- volumes

### Services

There are several types of services (Nodeport, LoadBalancer and none). It exposes
the applications through specific ports.

### Special Features

Some applications needed specific configuration, the modifications are:

- condor exporter needed uwsgi to stream its metrics. Python and python
development tool needed to be installed. A bash script substituted the CMD
script executed at the launch of each condor container. It added lines in the
supervisord configuration file to run uwsgi.

- In docker, docker-io is installed in the execution node. There was a problem
in docker permessions so condor has to be added to the wheel group. The other issue was
in  mounting the volume which is solved by creating "/var/lib/condor/execute" on
the host machine then mounting it to the execution pod (make sure that the ownership
is for the 'condor' user). DOCKER macro in the configuration file of the executer to 
the docker bin path is recommended. The image exists on 2281995/worker-docker repository.

- Jupyter notebook needed a special configuration file which is mounted on a 
specific directory.
  
## NFS and Singularity

The following steps have been taken:

- open 2049 port by checking `rpcinfo -p | grep nfs`

- launch nfs server that contains the singularity images

- open `/etc/exports` and add the dir and the `<dir path>   *(rw,sync,no_root_squash,no_all_squash)`

- restart nfs

- run `exportfs -arv`

- setup pv and pvc 

- make sure the deployment has nfs

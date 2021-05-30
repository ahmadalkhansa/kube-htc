# kube-htc

HTCondor deployemnt on top of Kubernetes with dynamic resource allocation capabilities.

# Components:

## HTCondor Deployment:

### Master:

The Master contains the collector and the negotioter.

### Schedulers:

There are 3 Schedulers:

- Scheduler with solo function of job submission.
- Scheduler with jupyter-notebook for credential access through a browser.
- Scheduler with condor-exporter for exporting metrics to prometheus(https://github.com/niclabs/htcondor-monitor/tree/master/CondorExporter/exporter/condor).

### Worker Nodes:

The Worker Nodes are resources of the HTCondor pool. They are able to run singularity containers if specified. The containers are stored in a network file system, allowing the Worker Nodes to access the images no matter their location in the Kubernetes cluster.

## Prometheus:

The Monitoring component of the cluster(https://prometheus.io/).

## Alertmanager:

Notifying component that warns a specific reciever if a metric exceeds a certain limit.

## Grafana:

Visualizer for Prometheus metrics(https://grafana.com/).

## Prometheus-adapter:

The adapter function in this infrastructure is to build Kubernetes custom metrics scraped by Prometheus, particularly HTCondor metrics.

## Autoscalers:

The autoscalers are designed specifically for this infrastructure:

- Node Autoscaler communicates with an OpenStack cloud API for creating and deleting Kubernetes Nodes, depending on resource demand.

- Pod Autoscaler autoscales Worker Nodes depending on their activity.

# Notes:

- The cloud is OpenStack with Oidc authentication and OAuth authorization protocols.

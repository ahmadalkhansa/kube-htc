# Prometheus

The monitoring tool of kubernetes + HTCondor. https://prometheus.io/docs/introduction/overview/

## Structure

Prometheus uses RBAC to scrape metrics from different components of kubernetes.
It communicates with the apiservers and extract metrics from them 
https://github.com/prometheus/prometheus/blob/release-2.24/documentation/examples/rbac-setup.yml. 

- clusterrole specifies the role and the resources that prometheus is allowed 
to access.
- clusterrole binding bind the clusterrole to the serviceaccount
- serviceacount provide the identity that processses that run inside the pod.
- configmap contains the configuration files. Scrape file 
https://github.com/prometheus/prometheus/blob/release-2.24/documentation/examples/prometheus-kubernetes.yml. recording rules
and alert rules for the alertmanager.
- deployment that specifies the node affinity, ports to be exposed, containers and the mounting locations
of the volumes, and the volumes to be mounted.
- persistent volume to store the data.
- service that exposes the application.
  

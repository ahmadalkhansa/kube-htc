# Prometheus Adapter

The deployment explanation exists on https://github.com/directxman12/k8s-prometheus-adapter.
The adapter is an implementation of resource metrics, custom metrics and external metrics APIs.


## Steps:

- create tls certificate and key:

`openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes`

- store them in a secret:
 
`kubectl create secret tls cm-adapter-serving-certs --cert=cert.pem --key=key.pem`

- mount them on the pod and specify the path of the files in flags

- specify the url of prometheus service (eg. http://prometheus.default.svc:9090/)

- get the raw value kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/default/Job/kubernetes-pods/condor_slot_activity_busy"

- kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/default/Job/kubernetes-pods/condor_slot_activity_busy?machine=$(kubectl get po -l app=worker -o name)" | jq for single node try!!!

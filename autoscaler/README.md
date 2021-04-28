# Node Autoscaler:

Check the cloud API access information and adjust the script as neccessary. The Autoscaler uses snapshots of computational instances on the cloud. The K3S agent provisioning is available on https://rancher.com/docs/k3s/latest/en/quick-start/.

# Pod Autoscaler:

The autoscaler deploy pods when all HTCondor working pods are busy and downscale by targeting idle pods.

# Note:

Supervisord is used to run the above scripts.

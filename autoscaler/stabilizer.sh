#!/bin/sh -x

while true; do
	ACTIVITY="$(kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/default/Job/kubernetes-pods/condor_slot_activity_busy" | cut -d "\"" -f 46 | cut -d "m" -f 1)"
	LWORKER="$(kubectl get pods | grep worker | cut -d " " -f 1 | tail -n 1)"
	SLOT="$(curl -s localhost:32747/metrics | grep condor_slot_activity_busy | grep "$LWORKER" | cut -d " " -f 2 | cut -d "." -f 1)"
	WORKERS="$(kubectl get pods | grep worker | cut -d " " -f 1)"
	LIST="$(kubectl get pods | grep worker | cut -d " " -f 1 | wc -l)"
	echo "$ACTIVITY"
	if [[ $ACTIVITY -ne 1 ]] && [[ $LIST -ne 1 ]]
	then
		echo "$SLOT"
		if [[ $SLOT -eq 1 ]]
		then
			IFS=$'\n'
			for WORKER in $WORKERS; do
				PSLOT="$(curl -s localhost:32747/metrics | grep condor_slot_activity_busy | grep "$WORKER" | cut -d " " -f 2 | cut -d "." -f 1)"
				echo "$(curl -s localhost:32747/metrics | grep condor_slot_activity_busy | grep "$WORKER")"
				if [[ $PSLOT -eq 0 ]]
				then
					kubectl delete pod $WORKER
				fi
				done
		fi
	fi
	sleep 240
done

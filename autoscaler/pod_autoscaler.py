#!/usr/bin/python3.6

import sys
import os
import yaml
import time
import threading


def detector():
	global pend
	global workers
	global avg_work
	global slots
	print(workers, pend)
	while True:
		try:
			pend = 0
			workers = {}
			avg_work = 0
			slots = 0
			pods = os.popen("kubectl get pods | grep worker")
			pods = pods.read().splitlines()
			for line in pods:
				pod_info = line.split()
				if pod_info[2] != "Running":
					pend += 1
				elif pod_info[2] == "Running":
					workers[pod_info[0]] = 0
			for worker in workers.keys():
				slot = os.popen("curl -s localhost:32747/metrics | grep condor_slot_activity_busy | grep %s" % worker)
				slot = slot.read()
				slot = slot.split()[1]
				slot = slot.split(".")[0]
				workers[worker] = int(slot)
			print(workers)
			for i in workers.keys():
				avg_work += workers[i]
				slots += 1
			if slots != 0:
				avg_work = float(avg_work)/float(slots)
			print("calculator data: avg= %d slots= %d" % (avg_work, slots))
		except:
			pass
		time.sleep(30)

def upscale():
	global pend
	global workers
	global avg_work
	global slots
	global order
	while True:
		print("evaluating for upscaling")
		print(workers)
		if pend == 0 and avg_work == 1:
			found = True
			while found:
				preorder = order
				for j in workers.keys():
					if str(order) == j.split("-")[1]:
						order += 1
				if preorder == order:
					found = False
			print("scaling up")
			template = {'apiVersion': 'v1', 'kind': 'Pod', 'metadata': {'name': 'worker-'+str(order), 'labels': {'name': 'worker'}}, 'spec': {'affinity': {'nodeAffinity': {'requiredDuringSchedulingIgnoredDuringExecution': {'nodeSelectorTerms': [{'matchExpressions': [{'key': 'k3s.io/hostname', 'operator': 'NotIn', 'values': ['k3s-htc.novalocal']}]}]}}}, 'containers': [{'name': 'worker', 'imagePullPolicy': 'IfNotPresent', 'image': '2281995/worker_singularity', 'resources': {'requests': {'cpu': '1000m'}, 'limits': {'cpu': '1000m'}}, 'volumeMounts': [{'mountPath': '/etc/condor/config.d/', 'name': 'worker'}, {'mountPath': '/home/simages', 'name': 'sing-images'}], 'ports': [{'containerPort': 9618}], 'securityContext': {'privileged': True}}], 'volumes': [{'name': 'worker', 'configMap': {'name': 'worker'}}, {'name': 'sing-images', 'persistentVolumeClaim': {'claimName': 'sing-images'}}]}}
			readable_template = yaml.dump(template)
			os.system('cat << EOF | kubectl apply -f -\n%s\nEOF' % readable_template)
			print("new worker node: worker-%s" % str(order))
		time.sleep(60)

def downscale():
	global workers
	global pend
	while True:
		print("evaluating for downscaling")
		print(workers)
		inact_worker = 0
		for worker in workers.keys():
			if workers[worker] == 0:
				inact_worker += 1
		if inact_worker > 1:
			for pods in workers.keys():
				if workers[pods] == 0:
					os.system("kubectl delete pod %s" % pods)
					print("delete working pod: %s" % pods)
					break
		time.sleep(300)
	
if __name__ == "__main__":
	pend = 0
	workers = {}
	avg_work = 0
	slots = 0
	order = 1
	p_detect = threading.Thread(target=detector)
	p_detect.start()
	p_upscale = threading.Thread(target=upscale)
	p_upscale.start()
	p_downscale = threading.Thread(target=downscale)
	p_downscale.start()
	
	


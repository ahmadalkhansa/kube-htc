#!/usr/bin/python3.6

from keystoneauth1 import session
from keystoneauth1.identity import v3
from keystoneauth1.identity.v3 import oidc
import novaclient.client as client
import time
import os
from prometheus_api_client import PrometheusConnect

if __name__ == "__main__":
	#create authorized session
	prom = PrometheusConnect(url ="http://192.168.20.16:30909/", disable_ssl=True)
	token = 'eyJraWQiOiJyc2ExIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI5NDc1NjA3Zi03MWEwLTRiMWUtOTM2OC1mNmJhNjExZGI0Y2IiLCJpc3MiOiJodHRwczpcL1wvaWFtLmNuYWYuaW5mbi5pdFwvIiwiZXhwIjoxNjE4ODU2NTMxLCJpYXQiOjE2MTg4NTI5MzEsImp0aSI6ImU5MWY4N2VjLTJjODEtNDAyMS1iYzcyLWQzMGZjZjZmZWY5YiIsImNsaWVudF9pZCI6IjA1NWU4MzM5LWUzYTEtNDVhMi05MDMzLTZkZGIzNmViZmE2NCJ9.HLVC0SS_8JCK12YxPNndEqqQHnnN7_ikCv80C0h8xA1HWMPeni8NzEqLk4ZXIIsozO6tgyfRxYqkS0xFOibmNi05Uch5MylO_8Vs9RQEtJSZI45lkxAU2dN_uH3JuFsH6SW1VkUCLSXvC0x6MbfnwbNRpQw79iAUHryJfs4h93s'
	auth = oidc.OidcAccessToken('https://cloud-api-pub.cr.cnaf.infn.it:5000/v3', 'cnaf', 'openid',
		token,
		project_id='be520a9af00641419710061d06dc0455', 
		project_name='Students'
		)
	sess = session.Session(auth=auth)
	token_auth = ''
	max_workers = 4
	removed = []
	order = 1
	while True:
		pending = 0
		pods = os.popen("kubectl get pods -o wide | grep worker")
		nodes = os.popen("kubectl get nodes | grep clust")
		pods_list = pods.read().splitlines()
		nodes_list = nodes.read().splitlines()
		workers = {}
		for line in nodes_list:
			nodes_info = line.split()
			worker = nodes_info[0].split(".")[0]
			workers[worker] = 0
		for line in pods_list:
			pod_info = line.split()
			if pod_info[2] == "Pending":
				pending += 1
			elif pod_info[2] != "Pending":
				worker = pod_info[6].split(".")[0]
				workers[worker]+=1
		# create new token and run the new session with it
		print("creating active session")
		token_auth = sess.get_token()
		print(token_auth)
		auth = v3.token.Token('https://cloud-api-pub.cr.cnaf.infn.it:5000/v3', 
			token_auth, 
			project_id='be520a9af00641419710061d06dc0455', 
			project_name='Students' 
			)
		sess = session.Session(auth=auth)
		nova = client.Client('2.1', session=sess)
		print(nova.servers.list())
		# to_be_deleted is important for down scaling
		to_be_deleted = []

		# query cpu usage from prometheus and update the usage list
		print("evaluating for autoscaling")
		print(workers)
                # check in the list for inactive nodes and request to delete them from openstack
		if len(workers.keys()) > 1 and pending == 0:
			for worker in workers.keys():
				if workers[worker] == 0:
					to_be_deleted.append(worker)

		if len(to_be_deleted) > 0:
			for inact_worker in to_be_deleted:
				print("downscaling %s" % inact_worker)
				nova.servers.delete(server=nova.servers.find(name=inact_worker))
				del workers[inact_worker]
				os.system('kubectl delete node '+inact_worker+'.novalocal')
				removed.append(inact_worker.split("t")[-1])

		# average the usage and check if there is possibility for upscale
		if pending > 0 and len(workers.keys()) < max_workers:
			if len(removed) == 0:
				found = True
				while found:
					preorder = order
					for i in workers.keys():
						if str(order) == i[-1]:
							order += 1
					if preorder == order:
						found = False
				removed.append(str(order))
			new_instance = "k3s-htc-clust"+removed[0]
			print("upscaling %s" % new_instance)
			del removed[0]
			nova.servers.create(name=new_instance, image="c1e682f6-012d-432b-9369-95d2425a3988", flavor=nova.flavors.find(name="m1.large"), security_groups=["kube_htc"])
			
		
		time.sleep(900)
		

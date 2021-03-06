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
	token = '<iam token>'
	auth = oidc.OidcAccessToken('<id url>', '<id provider>', '<id protocol>',
		token,
		project_id='<project id>', 
		project_name='<project name>'
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
		auth = v3.token.Token('<id url>', 
			token_auth, 
			project_id='<project id>', 
			project_name='<project name>' 
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
			nova.servers.create(name=new_instance, image="<kubernetes instance image snapshot id>", flavor=nova.flavors.find(name="<flavor name>"), security_groups=["<list of security groups>"])
			
		
		time.sleep(900)
		

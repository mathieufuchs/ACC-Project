import os
import swiftclient.client

config = {'username':os.environ['OS_USERNAME'], 
          'api_key':os.environ['OS_PASSWORD'],
          'project_id':os.environ['OS_TENANT_NAME'],
          'auth_url':os.environ['OS_AUTH_URL'],
           }
from novaclient.client import Client
nc = Client('2',**config)

# Terminate all your running instances
def kill(i):
	toTerminate = "mat_test_%i" %(i)
	serverToTerminate = nc.servers.find(name=toTerminate)
	serverToTerminate.delete()
	print("killed instance: %s" %(toTerminate))

for i in range(0,2):
	kill(i)
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
serverToTerminate = nc.servers.find(name="mat-test")
serverToTerminate.delete()
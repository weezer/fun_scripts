from keystoneclient import session as ksc_session
from keystoneclient.auth.identity import v3
from keystoneclient.v3 import client as keystone_v3
from novaclient.v2 import client as nova_v2

auth = v3.Password(auth_url='http://172.29.236.100:5000/v3',
                   username='admin',
                   password='4IMuRmqNPITPwnhb9YUQtvbihErpCGKo',
                   project_name='admin',
                   user_domain_name='default',
                   project_domain_name='default')

session = ksc_session.Session(auth=auth)
print "test"
keystone = keystone_v3.Client(session=session)
nova = nova_v2.Client(session=session)
print nova.servers.list()

from keystoneclient import session as ksc_session
from keystoneclient.auth.identity import v3
from keystoneclient.v3 import client as keystone_v3
from novaclient.v2 import client as nova_v2
import os

def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_name'] = os.environ['OS_PROJECT_NAME']
    d['user_domain_name'] = os.environ['OS_USER_DOMAIN_NAME']
    d['project_domain_name'] = os.environ['OS_PROJECT_DOMAIN_NAME']
    return d

cred = get_keystone_creds()

auth = v3.Password(**cred)

session = ksc_session.Session(auth=auth)
print "test"
keystone = keystone_v3.Client(session=session)
nova = nova_v2.Client(session=session)
print nova.servers.list()

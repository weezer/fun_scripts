__author__ = 'weez8031'


from keystoneclient import session as ksc_session
from keystoneclient.auth.identity import v3
from keystoneclient.v3 import client as keystone_v3
from novaclient.v2 import client as nova_v2
from cinderclient.v1 import client as cinder_v1
import os, socket, time, shutil


def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_name'] = os.environ['OS_PROJECT_NAME']
    d['user_domain_name'] = os.environ['OS_USER_DOMAIN_NAME']
    d['project_domain_name'] = os.environ['OS_PROJECT_DOMAIN_NAME']
    return d


def get_keystone_session():
    cred = get_keystone_creds()
    auth = v3.Password(**cred)
    return ksc_session.Session(auth=auth)


def create_volume_from_image(img_uuid):
    session = get_keystone_session()
    img_uuid = img_uuid
    vol_name = "test"
    cinder = cinder_v1.Client(session=session)
    cinder.volumes.list()
    myvol = cinder.volumes.create(size=10, display_name=vol_name, imageRef=img_uuid)
    return myvol


def read_user_date(file_path='user_data.file'):
    with open(file_path) as f:
        return f


def boot_instance_from_volume(img_uuid, network_id):
    hostname = "nova:" + socket.gethostname()
    session = get_keystone_session()
    nova = nova_v2.Client(session=session)
    block_dev_mapping = {'vda': create_volume_from_image(img_uuid).id}
    nics = [{'net-id': network_id}]
    instance = nova.servers.create(name="python-test3", image='', block_device_mapping=block_dev_mapping,
                                   flavor=4, nics=nics, userdata=read_user_date(), availability_zone=hostname)
    return instance


def logfile_analyzer(filename):
    filename = filename
    file = open(filename)
    md5code = ''
    md5check = ''
    while 1:
        where = file.tell()
        line = file.readline()
        if not line:
            time.sleep(1)
            file.seek(where)
        else:
            if line.containes('text1.log'):
                md5code = line[:32]
                md5check = True
                continue
            if md5check and line.contains('text'):
                if md5code == line[:32]:
                    continue
                else:
                    print "found error"
                    break
    shutil.copy(filename, '/var/log/lvmtest.log')


from greww.data.basics import stdir
from greww.utils.exceptions import RejectedConnection, FileNotFound
import paramiko


# allow_agent, look_forkeys
# paramiko
def ssh_connection(hostname=None, port=None, username=None, password=None):
    if hostname is None or port is None:
        return -1
    client = paramiko.Transport((hostname, port))
    client.connect(username=username, password=password)
    return client


def ssh_session(ssh_connection=None, hostname=None, username=None, password=None, kind=None):
    if ssh_connection:
        session = ssh_connection.open_channel(kind=kind)
        return session
    else:
        session = ssh_connection(hostname=hostname,
                                 port=port,
                                 username=username,
                                 password=password)
        session = session.open_channel(kind=kind)
        return session


def private_rsa_key(location):
    return paramiko.RSAkey.from_private_key_file(location)

#with key
def ssh_connection_with_private_key(server=None, user=None, location, pkey=None, allow_agent=False, look_for_keys=True):
    pkey = pkey or private_rsa_jey(location)
    c = paramiko.SSHCLient()
    #FIXME: pls


def send_ssh_command(ssh_connection=None):
    pass



class sshConnection(object):
    def __init__(self):
        pass

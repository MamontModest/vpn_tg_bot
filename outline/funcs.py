# Здесь хранится код по работе с ключами и серверами
import paramiko


def id_key(link):
    try:
        link=str(link).split()[0][2:]
        k1,k2=0,0
        for i in range(len(link)):
            if link[i]=='[':
                k1=i
                break
        for j in range(len(link)-1,0,-1):
            if link[j]==']':
                k2=j
                break
        spisok=link[k1+2:k2-1].split(',')
        id,accessUrl=spisok[0].split(':'),spisok[5].split(':')
        return int(id[1][1:-1]),(accessUrl[2])
    except:
        return False,False

def chek_all(host, username, password, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command('curl --insecure  https://46.151.26.65:13777/f5vG_VPTATspwHUUv4YMOA/access-keys/')
    data = stdout.read() + stderr.read()
    client.close()
    return data

def create_one(host, username, password, port):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command('curl --insecure -X POST https://46.151.26.65:13777/f5vG_VPTATspwHUUv4YMOA/access-keys/')
    data = stdout.read() + stderr.read()
    client.close()
    return data

def delete_one(id: int, host: str, username: str, password: str, port: int):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command('curl --insecure -X DELETE https://46.151.26.65:13777/f5vG_VPTATspwHUUv4YMOA/access-keys/'+str(id))
    data = stdout.read() + stderr.read()
    client.close()
    return data

def data_limit(id:int, limit:int, host:str, username:str, password:str, port:int):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, port=port)
    stdin, stdout, stderr = client.exec_command('''curl -v --insecure -X PUT -H 'Content-Type: application/json' -d  '{"limit": {"bytes": '''+str(limit)+'''}}' https://46.151.26.65:13777/f5vG_VPTATspwHUUv4YMOA//access-keys/'''+str(id)+'/data-limit')
    data = stdout.read() + stderr.read()
    client.close()
    return data
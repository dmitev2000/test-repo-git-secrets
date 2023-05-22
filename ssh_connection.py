import paramiko

hostname = 'remote_endpoint'
username = 'root'
private_key_path = './myKey'
public_key_path = './myKey.pub'

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    private_key = paramiko.RSAKey(filename=private_key_path)

    client.connect(hostname, username=username, pkey=private_key)

    stdin, stdout, stderr = client.exec_command('ls -l')
    print(stdout.read().decode())

    client.close()
except paramiko.AuthenticationException as auth_error:
    print(f"Authentication failed: {str(auth_error)}")
except paramiko.SSHException as ssh_error:
    print(f"SSH connection failed: {str(ssh_error)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
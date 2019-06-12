import paramiko

# 生成一个连接远程机器的客户端
ssh = paramiko.SSHClient()

# 加入主机列表中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 建立连接
ssh.connect(hostname='39.100.110.135', port=22, username='root', password='liuchao.0725')

while True:
    command = input('[root@39.100.110.135 ~]# ')
    if command == 'exit' or command == 'quit':
        break
    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    result = stdout.read()
    print(str(result, 'utf-8'))
    if len(result) == 0:
        print(str(stderr.read(), 'utf-8'))
    else:
        print(str(result, 'utf-8'))

ssh.close()

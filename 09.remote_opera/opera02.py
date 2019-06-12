import paramiko

# 建立ssh客户端
ssh = paramiko.SSHClient()

# 是否加入信任主机列表中时自动加入
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 创建ssh连接实例
ssh.connect(hostname='39.100.110.135', port=22, username='root', password='liuchao.0725')

# 写一个死循环从而反复使用Linux命令
while True:
    command = input("root@39.100.110.135:# ")
    if command == 'quit':
        break
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    if len(result) == 0:
        print(stderr.read())
    else:
        print(str(result, 'utf-8'))

# 关闭ssh连接
ssh.close()

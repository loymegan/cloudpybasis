import os


def request(url):
    global respond
    os.system("ping -c1 {}".format(url))
    if os.system("echo $?") == 0:
        respond = "Successfully"
    return respond



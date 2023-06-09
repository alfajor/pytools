import socket 

def init_server():
    host = 'localhost'
    port = 9000

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(1)

        while True:
            conn, addr = s.accept()
            print('Connection established', str(addr))
            cmd = input('Enter a cmd >> ') # test with single cmd

            if cmd == 'exit':
                break

            conn.send(cmd.encode())
    
            msg = conn.recv(8096).decode()
            print(msg)

        s.close()
           
    except Exception as err:
        print('There was a problem connecting', err)

init_server()
import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("Conexão com o servidor perdida")
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 65432))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    name = input(client.recv(1024).decode('utf-8'))
    client.send(name.encode('utf-8'))

    while True:
        try:
            message = input()
            if message.lower() == 'sair':
                break
            client.send(message.encode('utf-8'))
        except:
            break

    client.close()

if __name__ == "__main__":
    main()

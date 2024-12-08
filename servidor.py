import socket
import threading

clients = {}

def broadcast(message, sender=None):
    for client in clients.values():
        if client != sender:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove_client(client)

def handle_client(client_socket, address):
    client_socket.send("Digite seu nome: ".encode('utf-8'))
    name = client_socket.recv(1024).decode('utf-8')
    clients[name] = client_socket

    print(f"{name} entrou no chat")
    broadcast(f"{name} entrou no chat", client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"{name}: {message}")
            broadcast(f"{name}: {message}", client_socket)
        except:
            break

    remove_client(client_socket, name)

def remove_client(client_socket, name=None):
    if name:
        print(f"{name} saiu do chat")
        broadcast(f"{name} saiu do chat")
        del clients[name]
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 65432))
    server.listen(5)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        client_socket, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, address))
        thread.start()

if __name__ == "__main__":
    main()

import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    
    while True:
        message = input("Enter command (HELLO, TIME, EXIT, SHUTDOWN): ")
        client_socket.send(message.encode())
        response = client_socket.recv(1024).decode()
        print(f"Received from server: {response}")
        
        if message == "EXIT":
            break
    
    client_socket.close()

if __name__ == "__main__":
    start_client()

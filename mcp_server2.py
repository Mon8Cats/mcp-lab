import socket
import threading

shutdown_flag = False

def handle_client(client_socket):
    global shutdown_flag
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received: {data}")
        
        if data == "HELLO":
            response = "Hello from MCP Server"
        elif data == "TIME":
            response = f"Server time is {time.ctime()}"
        elif data == "EXIT":
            response = "Goodbye!"
            client_socket.send(response.encode())
            break
        elif data == "SHUTDOWN":
            response = "Server shutting down..."
            client_socket.send(response.encode())
            shutdown_flag = True
            break
        else:
            response = "Unknown command"
        
        client_socket.send(response.encode())
    
    client_socket.close()
    print("Client connection closed.")

def start_server():
    global shutdown_flag
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server started and listening for connections...")

    while not shutdown_flag:
        try:
            server_socket.settimeout(1)  # Set timeout to allow periodic check of shutdown_flag
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
        except socket.timeout:
            continue  # Continue loop to check shutdown_flag
        except Exception as e:
            print(f"Error accepting connections: {e}")

    print("Closing server socket...")
    server_socket.close()
    print("Server has been shut down.")

if __name__ == "__main__":
    import time
    start_server()
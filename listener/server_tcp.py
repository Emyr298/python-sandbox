import socket

TCP_IP = "0.0.0.0"  # IP address to bind the server
TCP_PORT = 12345  # Port number to bind the server

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {TCP_IP}:{TCP_PORT}")

# Accept incoming connections
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive and print data
data = conn.recv(1024)  # Receive data with a buffer size of 1024 bytes
message = data.decode()  # Decode the received data assuming it's in string format
print(f"Received message: {message}")

# Send a response
response = "Thank you for connecting!"
conn.sendall(response.encode())

# Close the connection
conn.close()
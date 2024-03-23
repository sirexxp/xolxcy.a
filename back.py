import socket

# Set the IP address and port of the server
SERVER_IP = '193.176.190.43'
SERVER_PORT = 9203

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect((SERVER_IP, SERVER_PORT))

# Receive commands from the user and send them to the server
while True:
    command = input('Enter command: ')
    
    # Send the command to the server
    s.send(command.encode())
    
    # Receive the output from the server
    output = s.recv(1024).decode()
    
    # Print the output
    print(output)
    
    # Check if the command is to terminate the connection
    if command.lower() == 'quit':
        break

# Close the socket
s.close()

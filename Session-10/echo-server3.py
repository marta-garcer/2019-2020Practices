import socket
import termcolor

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Configure the Server's IP and PORT
PORT = 8081
IP =  "192.168.1.37"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

# -- Variable for counting the number of connections
number_con = 0

# -- List for storing info about clients
client_list = []

print("The server is configured!")

while number_con < 5:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        number_con += 1

        print(f"CONNECTION {number_con}. Client IP,PORT: {client_ip_port}")

        # -- Store the client address in the list
        client_list.append(client_ip_port)

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print("Message received: ", end="")
        termcolor.cprint(msg, "green")

        # -- Send a response message to the client
        response = "ECHO: " + msg + "\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Close the data socket
        cs.close()


print("The following clients has connected to the server: ")
for i, j in enumerate(client_list):
    print(f"Client {i}: {j}")

# -- Close the socket
ls.close()
import socket

contacts = {
    "John Doe": {"address": "123 Main St", "phone": "555-1234"},
    "Jane Smith": {"address": "456 Elm St", "phone": "555-5678"}
}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 18080))  # 使用localhost作为服务器地址
server_socket.listen(1)

print("Server is running...")
while True:
    conn, addr = server_socket.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024).decode()
    print(f"Received data: {data}")
    command, *args = data.split()
    if command == "MODIFY":
        name, address, phone = args
        if name in contacts:
            if address != "None":
                contacts[name]['address'] = address
            if phone != "None":
                contacts[name]['phone'] = phone
            conn.send("Contact modified successfully.".encode())
        else:
            conn.send("Contact not found.".encode())
    elif command == "VIEW":
        if args:
            name = args[0]
            if name in contacts:
                response = f"{name}: {contacts[name]['address']} {contacts[name]['phone']}"
            else:
                response = "Contact not found."
        else:
            response = "\n".join([f"{name}: {info['address']} {info['phone']}" for name, info in contacts.items()])
        conn.send(response.encode())
    conn.close()
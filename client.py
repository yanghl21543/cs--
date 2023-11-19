import socket
def modify_contact(name, address=None, phone=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 18080))  # 连接服务器端的IP地址和端口号
    request = f"MODIFY {name} {address} {phone}"  # 构造修改联系人信息的请求消息
    client_socket.send(request.encode())  # 发送请求消息到服务器端
    response = client_socket.recv(1024).decode()  # 接收服务器端返回的响应消息
    print(response)  # 打印服务器端返回的响应消息
    client_socket.close()  # 关闭客户端socket连接

def view_contact(name=None):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 18080))  # 连接服务器端的IP地址和端口号
    if name:
        request = f"VIEW {name}"  # 构造查看指定联系人信息的请求消息
    else:
        request = "VIEW"  # 构造查看所有联系人信息的请求消息
    client_socket.send(request.encode())  # 发送请求消息到服务器端
    response = client_socket.recv(1024).decode()  # 接收服务器端返回的响应消息
    print(response)  # 打印服务器端返回的响应消息
    client_socket.close()  # 关闭客户端socket连接


modify_contact("John Doe", "456 Oak St", "555-9999")
# 调用view_contact函数发送请求
view_contact("John Doe")
view_contact()  # 查看所有联系人信息
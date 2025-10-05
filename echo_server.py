import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3003))
server_socket.listen()

print("Server is running on localhost:3003")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    request = client_socket.recv(1024).decode()
    if not request or 'favicon.ico' in request:
        client_socket.close()
        continue

    request_line = request.splitlines()[0]
    http_method, path_query, _ = request_line.split()
    path = path_query.split('?')[0]
    query_kwargs = path_query[2:]
    queries = query_kwargs.split('&')
    params = {}
    for query in queries:
        key, value = query.split('=')
        params[key] = value
        
    # from request line, parse into three separate variables
    # split request line by whitespace
    # http_method with value GET
    # path with value /
    # params as a dictionary with rolls and sides properties and the appropriate
    # values. note that the values are strings, which is typical of web apps

    roll = random.randint(1, 6)
    response_body = (f"{request_line}\nHTTP Method: {http_method}\n" +
                     f"Path: {path}\nParameters: {params}\n")
    
    for _ in range(int(params['rolls'])):
        response_body += f'Roll: {random.randint(1, int(params['sides']))}\n'


    response = ("HTTP/1.1 200 OK\r\n"
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(response_body)}\r\n"
                "\r\n"
                f"{response_body}\n")

    client_socket.sendall(response.encode())
    client_socket.close()
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import os

class AuthHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        # Handle /login and /register endpoints
        if self.path == '/login' or self.path == '/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)

            if self.path == '/login':
                username = params.get('username', [''])[0]
                password = params.get('password', [''])[0]

                if self.authenticate(username, password):
                    print(f"Successful login for user: {username}")
                    # Redirect to welcome.html after successful login
                    self.send_response(302)  # Found (redirect)
                    self.send_header('Location', f'/welcome.html?username={username}')
                    self.end_headers()
                else:
                    print(f"Failed login attempt for user: {username}")
                    # Redirect to login.html after unsuccessful login
                    self.send_response(302)  # Found (redirect)
                    self.send_header('Location', '/login.html')
                    self.end_headers()

            elif self.path == '/register':
                new_username = params.get('new_username', [''])[0]
                new_password = params.get('new_password', [''])[0]

                print(f"Attempting to register user: {new_username}")

                if self.register_user(new_username, new_password):
                    print(f"Successfully registered user: {new_username}")
                    # Redirect to index.html after successful registration
                    self.send_response(302)  # Found (redirect)
                    self.send_header('Location', '/index.html')
                    self.end_headers()
                else:
                    print(f"Error registering user: {new_username}")
                    self.send_response(400)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'Error registering user')

        else:
            super().do_POST()

    def authenticate(self, username, password):
        # Check if username:password pair exists in the users.txt file
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                stored_username, stored_password = line.strip().split(':')
                if username == stored_username and password == stored_password:
                    return True
        return False

    def register_user(self, username, password):
        print(f"Attempting to register user: {username}")

        # Check if the username already exists
        with open('users.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                stored_username, _ = line.strip().split(':')
                if username == stored_username:
                    print(f"User already exists: {username}")
                    return False

        # Append the new username and password to the users.txt file
        with open('users.txt', 'a') as f:
            f.write(f'{username}:{password}\n')
            print(f"Successfully registered user: {username}")

        return True

def create_users_file():
    if not os.path.isfile('users.txt'):
        with open('users.txt', 'w') as f:
            print("users.txt not found. Creating a new one.")

if __name__ == '__main__':
    create_users_file()

    # Get user input for server IP address and port
    server_ip = input("Enter the server IP address (default is localhost): ") or 'localhost'
    server_port = int(input("Enter the server port (default is 8000): ") or '8000')

    server_address = (server_ip, server_port)
    httpd = HTTPServer(server_address, AuthHandler)
    print(f'Server started on http://{server_ip}:{server_port}')
    httpd.serve_forever()

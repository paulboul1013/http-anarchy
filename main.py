import socket
import os  


HOST = '127.0.0.1'
PORT = 8080

def start_magic_server():
    # create TCP Socket 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Allow Port reuse to avoid "Address already in use" errors on restart
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            s.bind((HOST, PORT))
            s.listen()

            print(f"Server is running on http://{HOST}:{PORT}")

            while True:
                # Wait for client connection
                conn, addr = s.accept()
                with conn:
                    # Receive request data
                    raw_data = conn.recv(1024)
                    if not raw_data:
                        continue
                    
                    # Decode and get the first line of the request
                    request_text = raw_data.decode('utf-8', errors='ignore')
                    first_line = request_text.splitlines()[0]
                    
                    try:
                        method, path, protocol = first_line.split(' ')
                        
                        # Get the resource name from path (remove leading slash)
                        resource_name = path[1:]
                        custom_code = "200" # Default

                        # --- NEW FEATURE: Extract Header from Image ---
                        if os.path.exists(resource_name) and os.path.isfile(resource_name):
                            try:
                                with open(resource_name, 'rb') as f:
                                    # Read the first 8 bytes (file signature/magic numbers)
                                    header_bytes = f.read(8)
                                    # Convert to Hex string (e.g., "89504E47...")
                                    # Use upper case for better readability
                                    hex_header = header_bytes.hex().upper()
                                    
                                    custom_code = hex_header
                                    print(f"📂 File found: {resource_name}")
                                    print(f"🔍 Extracted Header (Hex): {custom_code}")
                            except Exception as file_err:
                                print(f"File read error: {file_err}")
                                custom_code = "FILE_READ_ERROR"
                        else:
                            # If file doesn't exist, use the path string as the code (Original Logic)
                            custom_code = resource_name if len(resource_name) > 0 else "200"

                        # Filter out favicon
                        if "favicon.ico" in path:
                            custom_code = "404"

                        print(f"Received request: {path} -> Final Status Code: [{custom_code}]")

                        # Format: HTTP/1.1 [Status Code] [Reason Phrase]
                        response_body = f"<h1>Status Code: {custom_code}</h1><p>Breaking the rules with file headers!</p>"
                        
                        response_headers = [
                            f"HTTP/1.1 {custom_code} MagicResponse",
                            "Content-Type: text/html; charset=utf-8",
                            f"Content-Length: {len(response_body.encode('utf-8'))}",
                            "Connection: close"
                        ]
                        
                        full_response = "\r\n".join(response_headers) + "\r\n\r\n" + response_body

                        conn.sendall(full_response.encode('utf-8'))
                        
                    except Exception as e:
                        print(f"Parsing Error: {e}")

        except KeyboardInterrupt:
            print("\nServer shut down.")

if __name__ == "__main__":
    start_magic_server()
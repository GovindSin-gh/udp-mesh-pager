import socket

# 1. Create a UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. ENTER YOUR BROTHER'S VPN IP HERE:
# Replace '100.64.0.5' with the exact virtual IP shown on his phone's VPN app
BROTHER_VPN_IP = '100.64.0.5' 
PORT = 9999

TARGET_ADDRESS = (BROTHER_VPN_IP, PORT)

print("🚀 PAGER SENDER ACTIVE")
print(f"Targeting destination: {BROTHER_VPN_IP} on port {PORT}")
print("Type your message and press Enter. Type 'exit' to quit.\n")

while True:
    try:
        message = input("Send Page: ")
        
        if message.lower() == 'exit':
            break
            
        # 3. Fire the packet directly across the VPN tunnel
        sock.sendto(message.encode('utf-8'), TARGET_ADDRESS)
        print("Transmission sent!\n")
        
    except (KeyboardInterrupt, SystemExit):
        break

sock.close()
print("Sender closed.")

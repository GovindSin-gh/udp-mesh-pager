import socket

# 1. Create a UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. Bind to '0.0.0.0'. This tells the phone to listen on ALL available 
# network routes, including your phone's normal Wi-Fi/SIM and the active VPN.
PORT = 9999
sock.bind(('0.0.0.0', PORT))

print("📟 PAGER RECEIVER ACTIVE")
print(f"Listening for incoming transmissions on port {PORT}...\n")

try:
    while True:
        # 3. Wait silently for a packet to drop in
        data, addr = sock.recvfrom(1024)
        message = data.decode('utf-8')
        
        # Display the alert instantly
        print("-" * 40)
        print(f"📢 ALERT RECEIVED from network path {addr[0]}:")
        print(f"Message: {message}")
        print("-" * 40 + "\n")

except KeyboardInterrupt:
    print("\nShutting down pager receiver.")
    sock.close()

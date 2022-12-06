# A simple program to send an integer to a Max msp patch

from pythonosc import udp_client

print("main running")
IP = "127.0.0.1"
PORT_TO_MAX = 1001
client = udp_client.SimpleUDPClient(IP, PORT_TO_MAX)
client.send_message("max", 1)


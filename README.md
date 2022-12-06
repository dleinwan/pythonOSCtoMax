# pythonOSCtoMax

A simple program to send an integer to a Max msp patch

1. Copy and paste the text from max_patch.txt to an open Max patch.
2. Run main.py

The integer 1 will be sent to the float box in the Max patch. See code from main.py:
client.send_message("max", 1)


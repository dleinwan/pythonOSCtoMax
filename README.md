# pythonOSCtoMax

A simple program to send an integer to a Max msp patch

1. Copy and paste the text from max_patch.txt to an open Max patch.
2. Run main.py

The integer 1 will be sent to the float box in the Max patch. See code from main.py:
> client.send_message("max", 1)

![main](https://user-images.githubusercontent.com/79383600/206001508-16e6d1c7-a35b-4191-8e8e-03307bcaa61c.png)
![max_patch](https://user-images.githubusercontent.com/79383600/206001520-ce43e15b-45d4-40fb-8bb5-095f5e058f8f.png)

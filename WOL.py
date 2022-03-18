import os
from wakeonlan import send_magic_packet

x=input("Turn on or off? (1/0) \n")
x=int(x, base=10)
print (x)
if x==1:
    send_magic_packet('FC.AA.14.9D.9A.AA')
    print ("Packet sent")
else:
    if input("are you sure? (y/n)") != "y":
        print("aborted")
    else:
        os.system('cmd /c "Shutdown -s -m Tokio254PC -t 0"')
        print("shutdown signal sent")

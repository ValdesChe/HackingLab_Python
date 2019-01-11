#!/usr/bin/env python

import subprocess


#interface = "wlp3s0"
#new_mac = "00:11:55:22:33:88"


interface = input("Enter an existing interface > ")
new_mac = input("Enter the new MAC ADDRESS for that interface > ")

print("\n \033[1;37;40m SIMPLE MAC CHANGER \033[0m \n\n")
print("[\033[1;32;40m+\033[0m] Changing the mac address of interface \033[1;33;40m" + interface + "\033[0m to \033[1;53;40m"+new_mac+"\033[0m !")

 
subprocess.call("ifconfig "+interface+" down", shell=True)
 
subprocess.call("ifconfig "+interface+" hw ether  "+new_mac+"", shell=True)
 
subprocess.call("ifconfig "+interface+" up", shell=True)
 
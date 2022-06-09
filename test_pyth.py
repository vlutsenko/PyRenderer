#from netmiko import netmiko
from time import time
from time import sleep

#print(dir())

for t in range(10,40):
    print("The current time is: {}". format(time()))
    sleep (1)
    
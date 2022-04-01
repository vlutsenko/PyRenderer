from netmiko import Netmiko
from netmiko import file_transfer
import time

src_file = "docker_run"
dst_file = "docker_run_tf"
direction = "put"

def docker_up(ip_addrs):
  net_conn = Netmiko(host=ip_addrs , username='root', password='@Ubuntu123a', device_type='linux')

  transfer_dict = file_transfer(net_conn, source_file=src_file, dest_file=dst_file, direction=direction, overwrite_file=True)

  cmd_1 = "ls -al /var/tmp"
  output = net_conn.send_command(cmd_1)
  print(output)

  cmd_2 = "chmod 777 /var/tmp/docker_run_tf"
  output = net_conn.send_command(cmd_2)
  print(output)

  cmd_4 = "/usr/bin/bash /var/tmp/docker_run_tf"
  net_conn.send_command(cmd_4)

  time.sleep(10)

  cmd_5 = "docker ps"
  output = net_conn.send_command(cmd_5)
  print(output)

  net_conn.disconnect()

ips = ['104.248.83.243', '134.209.84.217', '134.209.193.47']

for abc in ips:
    print(abc)
    docker_up(abc)

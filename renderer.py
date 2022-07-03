from asyncio.windows_events import NULL
import re
from pprint import pprint

###templates for file
templ_begin = "docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy:latest "
templ_end = " -t 1000 --rpc 1000  --debug"

#docker_in_txt = NULL
#docker_in = str(docker_in_txt)
docker_in =[]

with open('clear', 'r') as clear_set:
   file0 = clear_set.readlines()

print(type(file0))

for line in file0:
   #pprint(line)
   if ("http" or "https") in line:
      #pprint(line)
      next
   else:
      docker_in.append(line)   

   

# with open('raw_file_test', 'r') as file1:
#    Lines = file1.readlines()

###start file
print(templ_begin, end=" ")

###for line in Lines1:
for line in docker_in:
      result = re.findall("[0-9]+.[0-9]+.[0-9]+.[0-9]+|[0-9]+|tcp|udp", line.strip())
      if len(result) > 1:
         #print(result)

         r = 1 
         while r < len(result):
            #print (r, len(result))
      
            print (result[r+1]+"://"+result[0]+":"+result[r], end=" ")
            r += 2

#file1.close()

###end file
print (templ_end, end=" ")

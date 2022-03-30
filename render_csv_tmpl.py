import csv
import re

foo = "data.csv"

with open(foo) as f:
    print(f.readline())

    read_csv = csv.DictReader(f)
    for bgp_vars in read_csv:
        print(bgp_vars['ipaddress'])
        
import jinja2

ip_addr = ["10.11.11.1", "12.12.12.3", "13.22.11.2", "19.33.1.3"]

<<<<<<< HEAD
var_net = { 
=======
var_val = { 
>>>>>>> 28e55c5a6787e0c6302b0d7e8ace9a35fc13d0c3
    "ip_addr": ip_addr
}



route_templ = '''
  {%- for addr in ip_addr %}
  ip route {{ addr }}/32
  {%- endfor %}
'''
t = jinja2.Template(route_templ)
<<<<<<< HEAD
print (t.render(var_net))
=======
print (t.render(var_val))
>>>>>>> 28e55c5a6787e0c6302b0d7e8ace9a35fc13d0c3

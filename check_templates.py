import jinja2

ip_addr = ["10.11.11.1", "12.12.12.3", "13.22.11.2", "19.33.1.3"]

var = { 
    "ip": ip_addr
}

route_templ = '''
  ip route {%- for address in ip_addr %}
  {%- endfor}
'''
t = jinja2.Template(route_templ)
print (t.render(var))
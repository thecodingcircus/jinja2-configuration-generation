from jinja2 import Template

inputfile = open("interface.tmp")
outputfile = open("interface_out.txt","w")

interface_name = "tenGig0/1/0/0"
description = "This is My Description"
ipv4_address = "1.1.2.3/24"
mtu = "9200"

for thelines in inputfile:
    template = Template(thelines)
    templateList = {
                'interface_name':interface_name,
                'description':description,
                'ipv4_address':ipv4_address,
                'mtu_size':mtu
                            }
    theconfiguration = template.render(**templateList)
    outputfile.write("\n" + theconfiguration)

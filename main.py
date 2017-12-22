from io import StringIO
from xml.dom.minidom import parse
from xml.dom.minidom import getDOMImplementation
from xml_to_ram import xml_to_ram

#from xml.dom.minidom import *

if __name__=="__main__":
    try:
        xml = parse("tasks.xml")
        xml_to_ram(xml)
        xml2 = parse("prjadm.xdb.xml")
        xml_to_ram(xml2)
        print()
    except Exception as e:
        print(e)


#"C:\\Users\\ilia\\Docoments\\P\\toRamAndBack\\tasks.xml"
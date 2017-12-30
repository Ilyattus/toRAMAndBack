from io import StringIO
import xml.dom.minidom as md#import parse

from xml_to_ram import xml_to_ram
from ram_to_xml import ram_to_xml
from xml.dom.minidom import *

if __name__=="__main__":
    try:
        xml = md.parse("tasks.xml")
        ram1 = xml_to_ram(xml)
        xml2 = md.parse("prjadm.xdb.xml")
        xml_to_ram(xml2)

        #print(ram_to_xml(ram1).toprettyxml())
        print()
    except Exception as e:
        print(e)


#"C:\\Users\\ilia\\Docoments\\P\\toRamAndBack\\tasks.xml"
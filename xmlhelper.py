#!/usr/bin/python
# -*- coding: UTF-8 -*-    
# Author: tuguoyi
# FileName:xmlhelper
# DateTime:2/8/21 11:04 AM
import xml.etree.ElementTree as ET
import xml.dom.minidom


class XmlHelper:
    @classmethod
    def _remove_xml_wihtespace(cls, elem, level=0):
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = None
            if not elem.tail or not elem.tail.strip():
                elem.tail = None
            for subelem in elem:
                cls._remove_xml_wihtespace(subelem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = None
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = None
        return elem

    @classmethod
    def prettify_xml_elem(cls, elem):
        cls._remove_xml_wihtespace(elem)
        xml_string = ET.tostring(elem, method='xml')
        dom = xml.dom.minidom.parseString(xml_string)
        return dom.toprettyxml(indent="  ")

    @classmethod
    def prettify_xml_str(cls, xml_str):
        root = ET.fromstring(xml_str)
        return cls.prettify_xml_elem(root)


if __name__ == '__main__':
    s = """
<cpu match="exact" mode="custom">
          <model fallback="forbid">Broadwell-noTSX-IBRS</model>
             <vendor>Intel</vendor>
</cpu>
"""
    root = ET.fromstring(s)
    print(XmlHelper.prettify_xml_elem(root))
    print(XmlHelper.prettify_xml_str(s))



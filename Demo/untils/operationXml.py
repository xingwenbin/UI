import os
import xml.dom.minidom

class OperationXml(object):

    def dir_base(self, fileName, filePath = 'data'):

        return os.path.join(os.path.dirname(os.path.dirname(__file__)), filePath, fileName)

    def getXmlData(self, value):
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        name = db.getElementsByTagName(value)
        nameValue = name[0]
        return nameValue.firstChild.data

    def getXmlUser(self, parent, child):
        dom = xml.dom.minidom.parse(self.dir_base('ui.xml'))
        db = dom.documentElement
        itemlist = db.getElementsByTagName(parent)
        item = itemlist[0]
        return item.getAttribute(child)
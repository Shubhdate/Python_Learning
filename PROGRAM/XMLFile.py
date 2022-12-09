#XML File operations
import xmltodict
handle = open("xml.xml","r")
content = handle.read()
d = xmltodict.parse(content)
print(d['Result']['RequestCode'])
d['Result']['RequestCode'] = 4
x = xmltodict.unparse(d)
# print(content)
print(d)
'''
read an xml document, make changes to it, 
then write it back as xml
'''

from xml.etree.ElementTree import parse, Element

doc = parse('pred.xml')
root = doc.getroot()
print(root)

# remove a few elements
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# insert a new element after <nm>...</nm>
print(root.getchildren().index(root.find('id')))
print(root.getchildren().index(root.find('nm')))
idx = root.getchildren().index(root.find('nm')) + 1
e = Element('spam')
e.text = 'This is a test'
root.insert(idx, e)

# write back to a file
doc.write('newpred.xml', xml_declaration=True)

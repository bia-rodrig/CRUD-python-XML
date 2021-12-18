from xml.etree import ElementTree
import os.path

def createXML():
	check = os.path.exists('db_test.xml')
	if (not check):
		tree = ElementTree.ElementTree()
		root = ElementTree.Element('List_of_Contacts')
		tree._setroot(root)
		tree.write('db_test.xml')
		
	'''
	root = xml.Element('List_of_Contacts')
	cl = xml.Element('Contact')
	root.append(cl)
	typel=xml.SubElement(cl, 'Name')
	typel.text='Bianca'

	last_name = xml.SubElement(cl, 'Last_Name')
	last_name.text='Rodrigues'
	'''
def insert(filename):
	tree = ElementTree.parse(filename)
	root = tree.getroot()
	#print(root.attrib) # root não tem atributos
	#count = 0
	#for child in root:
		#count += 1
		#for elem in child:
			#print(elem.tag, elem.attrib)
		#	print(elem.text)
	#print (count)

	cl2 = ElementTree.Element('Contact')
	root.append(cl2)
	typel2=ElementTree.SubElement(cl2, 'Name')
	typel2.text='Bianca'

	last_name2 = ElementTree.SubElement(cl2, 'Last_Name')
	last_name2.text='Rodrigues'

	tree = ElementTree.ElementTree(root)
	with open (filename, 'wb') as files:
		tree.write(files)

GenerateXML("Contacts1.xml")

insert("Contacts1.xml")
insert("Contacts1.xml")

from xml.etree import ElementTree
import os.path

#Bianca Rodrigues
#GitHub: https://github.com/bia-rodrig/

'''
# XML Sctructure
<Contacts_List>
	<Contact>
		<Name>Contact Name</Name>
		<Age>Contact Age</Age>
		<Phone> Contact Phone Number</Phone>
	</Contact>
</Contacts_List>
'''

filename = 'db_test.xml'
op = 5

# Check if DB exists and create if doesn't
check = os.path.exists(filename)
if (not check):
	tree = ElementTree.ElementTree()
	root = ElementTree.Element('Contacts_List')
	tree._setroot(root)
	tree.write(filename)
	print('Database created\n')


def insert_contact():
	print('\nInsert contact info:')
	name = input('Name: ')
	age = input('Age: ')
	phone = input('Phone: ')

	tree = ElementTree.parse(filename)
	root = tree.getroot()

	el = ElementTree.Element('Contact')

	id_tag = ElementTree.SubElement(el, 'ID')
	id_tag.text = str(len(root) + 1)

	name_tag = ElementTree.SubElement(el, 'Name')
	name_tag.text = name

	age_tag = ElementTree.SubElement(el, 'Age')
	age_tag.text = age

	phone_tag = ElementTree.SubElement(el, 'Phone')
	phone_tag.text = phone

	root.append(el)

	tree = ElementTree.ElementTree(root)
	tree.write(filename)


def update_contact():
	print('\nInform contact ID to update:')
	select_id = input('ID: ')
	selected_child = ''

	tree = ElementTree.parse(filename)
	root = tree.getroot()
	for child in root.findall('Contact'):
		if child.find('ID').text == select_id:
		#for element in child:
			#if (element.tag == 'ID' and element.text == select_id):
			print('\nContact selected:')
			selected_child = child
			for item in child:
				print('{} : {}'.format(item.tag,item.text))
	print('\nInsert new informations:')
	new_name = input('Name: ')
	new_age = input('Age: ')
	new_phone = input('Phone: ')

	selected_child[1].text = new_name
	selected_child[2].text = new_age
	selected_child[3].text = new_phone

	tree.write(filename)
	print('Contact updated')

	

def delete_contact():
	print('\nInform contact ID to delete:')
	select_id = input('ID: ')

	tree = ElementTree.parse(filename)
	root = tree.getroot()
	for child in root:
		for element in child:
			if (element.tag == 'ID' and element.text == select_id):
				#print('{}: {}'.format(element.tag, element.text))
				root.remove(child)
				print('Contact removed')
	tree.write(filename)
	

def list_contacts():
	print('\nContacts list:')
	tree = ElementTree.parse(filename)
	root = tree.getroot()
	for child in root:
		for element in child:
			print('{}: {}'.format(element.tag, element.text))
		print('\n')


def exit():
	print('Finished')


switch = {'1': insert_contact, '2': update_contact, '3': delete_contact, '4': list_contacts, '0': exit}

while int(op) != 0:
	print('\n\n#   Options')
	print('1 - Insert contact')
	print('2 - Update contact')
	print('3 - Delete contact')
	print('4 - List')
	print('0 - Exit')
	op = input('Choose an option:')

	if (int(op) <= 4):
		call = switch.get(op)
		call()
	else:
		print('Invalid option')
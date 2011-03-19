#!/usr/bin/python
# 
# dump the sparse 'Fields' mappings to an html report
#

Fields = (
	('IP Address', {'City':'probably', 'State':'yes', 'Zip':'yes', 'Country':'yes'}),
	('Given Name', {'Gender':'99%', 'Age':'50-90%', 'Ethnicity':'maybe', 'Religion':'maybe'}),
	('Family Name', {'Ethnicity':'maybe','Religion':'maybe'}),
	('Title', {'Gender':'yes', 'Relationship':'maybe'}),
	('Email', {'Given Name':'sometimes', 'Family Name':'sometimes', 'City':'sometimes', 'Hobby':'sometimes', 'D.O.B.':'maybe'}),
	('Age', {'Politics':'probably', 'Home Ownership':'maybe', 'Salary':'maybe'}),
	('D.O.B.', {'Age':'100%'}),
	('Address', {'Home Ownership':'sometimes'}),
	('City', {'State':'maybe'}),
	('State', {}),
	('Zip', {'City':'100%', 'State':'100%'}),
	('Country', {'Language':'probably','Ethnicity':'maybe','Religion':'maybe'}),
	('Gender', {}),
	('Language', {'Ethnicity':'maybe'}),
	('Ethnicity', {'Religion':'maybe', 'Employment':'maybe', 'Education':'maybe', 'Politics':'maybe', 'Language':'probably'}),
	('Religion', {'Ethnicity':'maybe','Holiday':'100%'}),
	('Holiday', {'Religion':'maybe','Country':'maybe'}),
	('Salary', {}),
	('Employment', {}),
	('Education', {}),
	('Hobby', {}),
	('Relationship', {}),
	('Home Ownership', {}),
	('Children', {}),
	('Politics', {}),
	('Writing', {'Gender':'probably', 'Education':'maybe', 'Ethnicity':'maybe', 'Relationship':'maybe', 'Hobby':'maybe'}),
	('Shopping History', {'Gender':'probably', 'Ethnicity':'maybe', 'Religion':'maybe', 'Salary':'maybe', 'Hobby':'probably', 'Relationship':'maybe','Home Ownership':'maybe'}),
)

def html():
	print("""
<html><head><style type="text/css">
table,th,td{border-collapse:collapse; font-family:Verdana,Arial}
th{background-color:#ccc; font-size:x-small}
td{padding:2px; font-size:x-small}
td.x{background-color:#fcc}
</style></head><body><table border="1">""")
	print('<tr><th><th>' + '<th>'.join([f for f,_ in Fields]))
	for k,d in Fields:
		print('<tr><th>%s' % (k))
		for k2,_ in Fields:
			print('<td%s>' % (' class="x"' if k2 in d else ''))
			if k2 == k:
				print('&mdash;')
			elif k2 in d:
				print(d[k2])
	print("""</table></body></html>""")

def graphviz():
	print('digraph {')
	for src,d in Fields:
		for dst,prob in d.items():
			print('"%s" -> "%s" [label="%s",style="%s",color="%s"]' % \
				(src,dst,
				 prob if prob not in ['probably','sometimes','maybe','yes','100%'] else '',
				 'dashed' if prob in ['maybe','sometimes'] else 'solid',
				 '#cccccc' if prob in ['maybe','sometimes'] else '#000000'))
	print('}')

if __name__ == '__main__':
	import sys
	if sys.argv[1:] == []:
		html()
 	else:
		if sys.argv[1].lower() == 'graphviz':
			graphviz()
		else:
			html()


import os

#direct = os.listdir('data')

#for name in direct:
#	if name.split('.')[1]=='JPG':
#		os.rename('data/'+name,'JPEGImages/'+name)
#	else:
#		os.rename('data/'+name,'Annotations/'+name)

direct = os.listdir('JPEGImages')
for i,name in enumerate(direct):
	os.rename('JPEGImages/'+name,'JPEGImages/{}.jpg'.format(i))
	os.rename('Annotations/'+name.split('.')[0]+'.lif','Annotations/{}.xml'.format(i))

	

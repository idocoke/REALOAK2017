import os
import numpy as np
import math

files = os.listdir('Annotations')
trainval = np.random.choice(np.array(files),int(math.ceil(len(files)/2.0)),replace=False)
test = [x for x in files if x not in trainval]

for i,el in enumerate(trainval):
	trainval[i] = el.split('.')[0]
for i,el in enumerate(test):
	test[i] = el.split('.')[0]
for i,el in enumerate(files):
	files[i] = el.split('.')[0]

f = open('trainval.txt','w')
f.write('\n'.join(trainval))
f.close()

f = open('test.txt','w')
f.write('\n'.join(test))
f.close()

#Eventually: just check if the objects are there, if so, add to cola_can = [] etc.

#f = open('cola_can.txt','w')
#f.write('\n'.join(files))
#f.close()

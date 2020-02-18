import sys
import os
from collections import Counter


filename = input('Which data file do you want to use? ')
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()
try:
	number = int(input('How many decilitres of water do you want to pour down? '))
	if number<0:
		raise Exception('')
except:
	print("Only nonnegative integer accepted.")
	
rainfile= open(filename,'r')
list = []
rows=0
columns=0

for line in rainfile:
	rows=rows+1
	for i in line:
		
		try:
			if (int(i)):
				list.append(int(i))
				if rows==1:
					columns=columns+1
		except:
			pass

#print(columns*rows)
count=Counter(list)
count_l=dict(count)
count_l=(dict(sorted(count.items())))
#print(count_l)
total=0
no=number

if no!=0:
	count=1
	#print(no)
	for i in count_l.keys():
		if(no==0):
			break
		val=count_l[i]
	#	print(val)
		total=total+val
		if((no-total)<0):
		#	print("IFFFFF")
			count=count+(no/total)
			no=0
			#print(count)
		else:
			#print("ELSEEEEE")
			no=no-total
			count=count+1
	if(no!=0):
		
		no=no/(columns*rows)
		count=count+no
else:
	count=0
			
print(f'The water rises to {count:.2f} centimetres.')
	





        



    


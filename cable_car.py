import sys
import os
from collections import Counter

def final(gr,nop):
    print("The longest good ride has a length of:",gr)
    print("The minimal number of pillars to remove to build a perfect ride from the rest is:",nop)
    exit()




filename = input('Please enter the name of the file you want to get data from: ')
if not os.path.exists(filename):
    print('Sorry, there is no such file.')
    sys.exit()

line_main = []

with open(filename, 'r') as f:
    content = f.readlines()

content = [x.strip() for x in content]

try:
    for line in content:
        s = line.split()
        for i in s:
            if (int(i) > 0):
                if all(int(i) > x for x in line_main):
                    line_main.append(int(i))
                else:
                    raise ValueError
            else:
                raise ValueError

    if len(line_main) < 2:
        raise ValueError
except ValueError:
    print("Sorry, input file does not store valid data.")
    exit()

count1 = 0
rem_list = []
while (count1 < len(line_main) - 1):
    sub = line_main[count1 + 1] - line_main[count1]
    rem_list.append(sub)
    count1 = count1 + 1
# print(rem_list)
z = dict(Counter(rem_list))
# print(z)
if len(z) == 1:
    print("The ride is perfect!")
    good_ride=len(line_main)-1
    number_pillars=0
    final(good_ride,number_pillars)


else:
    print("The ride could be better...")

a = dict()
count1 = len(line_main) - 1
while (count1 >=0):
    count2 = count1-1
    while (count2 >=0):
        rem = line_main[count1] - line_main[count2]

        if rem in a:
            a[rem] = a[rem] + 1
        else:
            a[rem] = 1
        count2 = count2 - 1
    count1 = count1 - 1
number=[]
for key, val in a.items():
    if val == max(a.values()):
        number.append(key)

number=min(number)


number_pillars=0
for i in line_main:
    if i%number!=0:
        number_pillars=number_pillars+1
#print(number_pillars)


rem123 = iter(rem_list)

count1=0
good_ride=[]
while(count1<len(rem_list)-1):
    count2=count1+1
    occ=1
    while(count2<len(rem_list) and rem_list[count2]==rem_list[count1]):
        occ=occ+1
        count2=count2+1
    good_ride.append(occ)
    count1=count1+1
good_ride= max(good_ride)
final(good_ride,number_pillars)

import sys
import os.path
from collections import deque

def final(wd,itd):
    print(f'From the west, one can see into the tunnel over a distance of {wd}.')
    print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {itd}.')
    exit(1)

def distance_from_west(l1,l2):
    count=0
    for i in l1:
        if i > l2[0]:
            count=count+1
        else:
            return count
    return count

def max_distance_thru_tunnel(l1,l2):
    A=deque()
    B=deque()
    count=0
    while (count < len(l1)):
            A.append((l1[count],count))
            B.append((l2[count],count))
            count=count+1


    # while(count<len(l1)):
    #     if count==0:
    #         A.append((l1[count],count))
    #         max=l1[count]
    #         count=count+1
    #     elif max>=l1[count]:
    #         A.append((l1[count],count))
    #         max=l1[count]
    #         count=count+1
    #     elif (count==len(l1)-1):
    #         A.append((l1[count], count))
    #         count = count + 1
    #     else:
    #         count=count+1
    # count=0
    # while (count < len(l2)):
    #     if count == 0:
    #         B.append((l2[count], count))
    #         max = l2[count]
    #         count = count + 1
    #     elif max <= l2[count]:
    #         B.append((l2[count], count))
    #         max = l2[count]
    #         count = count + 1
    #     elif (count==len(l2)-1):
    #         B.append((l2[count], count))
    #         count = count + 1
    #     else:
    #         count = count + 1
    # print(A)
    # print(B)
    count=0
    maxApos=0
    maxBpos=0
    # start=-1
    maxA=10
    maxB=-1
    distance=[]
    # while(count<len(A)):
    #     count1=start
    #     if(0):
    #         pass
    #     # if maxA >= B[count][0]:
    #     #     distance.append(A[count][1] - (start))
    #     #     start = A[count][1]
    #     # if maxB <= B[count][0]:
    #     #     distance.append(A[count][1] - (start))
    #     #     start = B[count][1]
    #     else:
    #         while(count1<=count and count1<len(B)):
    #             if A[count][0]<=B[count1][0]:
    #                 if start==-1:
    #                     distance.append(A[count][1]-(start))
    #                     start=B[count1][1]
    #                 else :
    #                     distance.append(A[count][1]-(start)-1)
    #                     start=B[count1][1]
    #
    #             if A[count][1]==B[count1][1] and A[count][1]==len(l2)-1:
    #                 if start==-1:
    #                     distance.append(A[count][1]-(start))
    #                     start=B[count1][1]
    #                 else :
    #                     distance.append(A[count][1]-(start)-1)
    #                     start=B[count1][1]
    #             count1=count1+1
    #     count =count +1
    # print(distance)



    # while (count < len(A)):
    #     count1 = 0
    #
    #     while (count1 <= count and count1 < len(B)):
    #             if A[count][0]<=B[count1][0]:
    #                 distance.append(A[count][1]-(start))
    #                 start=A[count][1]-start
    # print(distance)
    # print(A)
    # print(B)
    # count=0
    # start=-1
    # maxA=10
    # maxB=-1
    # distance=[]
    # while (count < len(A)):
    #     if A[count][0]<=maxA:
    #         counter=0
    #         maxA=A[count][0]
    #         distance.append(A[count][1]-start)
    #         while counter<count and counter<len(A):
    #             del A[0]
    #             counter=counter+1
    #
    #     count1=0
    #     while(count1<len(B) and count1<count):
    #         if B[count1][0]>=maxB:
    #             counter=0
    #             maxB=B[count1][0]
    #             distance.append(B[count1][1]-start)
    #             while counter<count1 and counter<len(B):
    #                 del B[0]
    #                 counter=counter+1
    #             count2=0
    #             while(count2<len(B)):
    #                 if A[count][0]<B[count2][0]:
    #                     maxA=A[count][0]
    #                     distance.append((A[count][1] - (start)))
    #                     start=A[count][1]
    #                 count2=count2+1
    #         count1 = count1 + 1
    #     count=count+1
    # print(distance)

#     count1=start
#     if(0):
#         pass
#     # if maxA >= B[count][0]:
#     #     distance.append(A[count][1] - (start))
#     #     start = A[count][1]
#     # if maxB <= B[count][0]:
#     #     distance.append(A[count][1] - (start))
#     #     start = B[count][1]
#     else:
#         while(count1<=count and count1<len(B)):
    while(count<len(A)):
        if A[count][0] <= maxA:
            if maxApos>=maxBpos:
                distance.append(A[count][1]- maxApos -1)
            else:
                distance.append(B[count][1] - maxBpos - 1)
                distance.append(A[count][1]- maxApos -1)
            maxApos=A[count][1]
            maxA=A[count][0]
        if B[count][0] >= maxB:
            if maxBpos>=maxApos:
                distance.append(B[count][1]-maxBpos-1)
            else:
                distance.append(A[count][1]-maxApos)
            maxBpos=B[count][1]
            maxB=B[count][0]

        if A[count][0] <=maxB:
            count1=maxBpos
            flag=0
            while count1<count:
                if B[count1][0]>=A[count][0]:
                    flag=1
                count1=count1+1
            if flag==0:
                distance.append(A[count][1]-maxBpos-1)
        elif B[count][0]>= maxA:
            distance.append(B[count][1]-maxApos)
        count=count+1
    if maxA<maxB:
        count=maxApos
        pos = maxApos
        while(count!=0):
            if B[count][0]>maxA:
                pos=B[count][1]
                break

            count=count-1
        distance.append(len(A)-pos-1)
    else:
        count = maxBpos
        pos=maxBpos
        while (count != 0):
            if A[count][0] < maxB:
                pos = A[count][1]
                break
            count = count - 1

        distance.append(len(B)-pos-1)

    return max(distance)



filename= input("Please enter the name of the file you want to get data from: ")
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

line1 = []
line2= []

with open(filename, 'r') as f:
    content = f.readlines()

content = [x.strip() for x in content]
count=0
try:
    for line in content:
        if not line:
            continue
        else:
            if count>3:
                raise ValueError
            else:
                s = line.split()
                for i in s:
                    if (isinstance(int(i),int)):
                        if count==0:
                            line1.append(int(i))
                        else:
                            line2.append(int(i))
                    else:
                        raise ValueError
                count=count+1

    if(len(line1)!=len(line2) or len(line1)<2 or len(line2)<2):
        raise ValueError
    else:
        count=0
        while(count<len(line2)):
            if line1[count]<=line2[count]:
                raise ValueError
            else:
                count=count+1

except ValueError:
    print("Sorry, input file does not store valid data.")
    exit()

#print(line2,line1)
sight_from_west=distance_from_west(line1,line2)
#print(sight_from_west)
max_distance=max_distance_thru_tunnel(line1,line2)
final(sight_from_west,max_distance)



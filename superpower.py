import sys

def final(smt,sho,nfc,anf):
    print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {smt}.')
    print(f'Flipping the power of the same hero at most once, the greatest achievable power is {sho}.')
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {nfc}.')
    print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {anf}.')
    exit()
def flip_many_times(nof,negative,positive):
    neg1=list(negative)
    pos1=list(positive)

    neg1.sort(reverse=True)
    pos1.sort()


    if (len(negative)%nof==0 or len(negative)>nof) and (len(negative)!=1 and len(negative)!=0):
        count=len(negative)-1
        for i in range(0,nof):
            neg1[count]=neg1[count]*-1
            count=count-1
        return sum(neg1)+sum(pos1)

    if len(neg1)==0:
        if len(pos1)%nof==0 and nof!=1:
            return sum(pos1)
        elif nof%2==0:
            return sum(pos1)
        else:
            pos1[0]=pos1[0]*-1
            return  sum(pos1)

    count = len(neg1) - 1
    a = min(neg1) * -1
    if a < min(pos1):
        minimum_value = [a, 'negative']
    else:
        minimum_value = [min(pos1), 'positive']

    while(count!=-1) :
        if nof!=0:
            neg1[count]=neg1[count]*-1
            count=count-1
            nof=nof-1

        if nof==0:
            break
    if nof%2==1:
        if minimum_value[1]=='positive':
            b=pos1.index(minimum_value[0])
            pos1[b]=pos1[b]*-1
        else :
            b=neg1.index(minimum_value[0]*-1)
            neg1[b]=neg1[b]*-1
    return sum(neg1)+sum(pos1)


def flip_am_once(negative, positive, nof):
    neg2 = []
    pos2 = []
    if len(negative) > 0:
        count = 0
        while count < len(negative) and nof > 0:
            neg2.append(negative[count] * (-1))
            count = count + 1
            nof = nof - 1
        while count < len(negative) and nof == 0:
            neg2.append(negative[count])
            count = count + 1
    if len(positive) > 0 and nof > 0:
        count = 0
        while count < len(positive) and nof > 0:
            pos2.append(positive[count] * (-1))
            count = count + 1
            nof = nof - 1
        while count < len(positive) and nof == 0:
            pos2.append(positive[count])
            count = count + 1
    sum_fao = sum(neg2) + sum(pos2)
    return sum_fao


def consec(hp, nof):
    sp = hp
    list_sum = []
    count1 = 0
    while count1 <= len(hp) - nof:
        count2 = count3 = 0
        sum = 0
        while (count1 != count2):
            sum = sum + sp[count2]
            count2 = count2 + 1

        while count3 < nof:
            sum = sum + sp[count2] * -1
            count2 = count2 + 1
            count3 = count3 + 1
        while count2 < len(hp):
            sum = sum + sp[count2]
            count2 = count2 + 1
        list_sum.append(sum)
        count1 = count1 + 1
    return max(list_sum)


4


def arbitrary(hp1):
    count = 0
    sum1 = []
    while (count < len(hp1)):
        count2 = 0
        if hp1[count] > 0:
            count=count+1
            continue
        else:
            cur_sum=0
            while (count2 < len(hp1)):
                sp = list(hp1)
                while (count2 < count):
                    cur_sum = cur_sum + sp[count2]
                    count2 = count2 + 1

                count3=count2
                while count3<len(hp1):
                    cur_sum3 = cur_sum
                    if sp[count3]<0:
                        cur_sum3=cur_sum3+(sp[count3]*-1)
                        count4=count3
                        cur_sum4=cur_sum3
                        if sp[count4]<0:
                            cur_sum4 = cur_sum4 + (sp[count4] * -1)
                            while count4<len(hp1):
                                cur_sum4 = cur_sum4 + sp[count4]
                                count4=count4+1
                            sum1.append(cur_sum4)
                            count3= count3+1

                    else:
                        count3 = count3 + 1

                count2=count2+1
        count=count+1
    if not sum1:
        sum1.append(sum(hp1))

    return max(sum1)


try:

    hp = input('Please input the heroes\' powers: ').split()
    hp = list(map(int, hp))
except ValueError:
    print('Sorry, these are not valid power values.')
    sys.exit()
try:

    power_flip = int(input('Please input the number of power flips: '))
    if power_flip < 0:
        raise ValueError
    if power_flip > len(hp):
        raise ValueError
except ValueError:
    print('Sorry, this is not a valid number of power flips.')
sp1 = list(hp)
hp.sort()

neg = []
pos = []
for i in hp:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

fmt=flip_many_times(power_flip,neg,pos)

fao = flip_am_once(neg, pos, power_flip)

nb_consec = consec(sp1, power_flip)



arb = arbitrary(sp1)

final(fmt,fao,nb_consec,arb)

num = [0]*32
FA = 0
HA = 0
stage = [13,9,6,4,3,2]

for i in range(32):
    if i >= 16:
        num[i] = 31-i
    else:
        num[i] = i+1
print("origin num is")
print(num)
# stage 1
for j in range(6):
    for i in range(31):
        if num[i] > stage[j]:
            while num[i] > stage[j]:
                if num[i] >= stage[j] + 2:
                    num[i] = num[i] - 2
                    num[i+1] = num[i+1] + 1
                    FA += 1
                else:
                    num[i] = num[i] - 1
                    num[i+1] = num[i+1] + 1
                    HA += 1
    print("the {}th num is {}".format(j,num))
    print("the number of HA is {}, the number of FA is {}".format(HA,FA))
    


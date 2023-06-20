num = [[0]*32 for _ in range(9)]
FA = [0]
HA = [0]

for i in range(9):
    if i == 0:
        for j in range(32):
            if j < 20:
                num[i][j] = 1
    elif i == 7:
        for j in range(32):
            if j >= 14:
                num[i][j] = 1
        num[i][2*(i-1)] = 1      
    elif i == 8:
        num[i][2*(i-1)] = 1      
            
    else:
        for j in range(32):
            if j < 19+2*i and j >= 2*i:
                num[i][j] = 1
        num[i][2*(i-1)] = 1  
        
# print num array
def print_num(num):
    for i in range(9):
        str_1 = ""
        for j in range(31,-1,-1):
            str_1 = str_1 + str(num[i][j])
        print(str_1)
        
print_num(num)

col_num = [0]*32
# count num for each colume
def count_num(col_num,num):
    for i in range(32):
        for j in range(9):
            col_num[i] += num[j][i]

count_num(col_num,num)
print(col_num)

def change_stage(col_num,FA,HA):
    flag = 0
    for i in range(31,-1,-1):
        HA_num = 0
        FA_num = 0
        if col_num[i] >= 3:
            flag = 1
        if flag == 1:
            FA_num = col_num[i] // 3
            if col_num[i] % 3 == 2:
                HA_num = 1
            col_num[i] = col_num[i] % 3 - HA_num*2 + FA_num + HA_num
            col_num[i+1] += FA_num + HA_num
            
            FA[0] += FA_num
            HA[0] += HA_num
for j in range(6):
    change_stage(col_num,FA,HA)
    print(col_num)
    print(FA[0],HA[0])
# all FA is not good
# def change_stage(col_num,FA):
#     for i in range(31,-1,-1):
#         if col_num[i] >= 3:
#             FA_num = col_num[i] // 3
#             col_num[i] = col_num[i] % 3 + FA_num
#             col_num[i+1] += FA_num
#             FA[0] += FA_num

 
# for i in range(4):
#     change_stage(col_num,FA)
#     print(col_num)
#     print(FA[0])

# dadda tree test
# stage = [13,9,6,4,3,2]

# num = col_num
# FA = 0
# HA = 0
# for j in range(6):
#     for i in range(31):
#         if num[i] > stage[j]:
#             while num[i] > stage[j]:
#                 if num[i] >= stage[j] + 2:
#                     num[i] = num[i] - 2
#                     num[i+1] = num[i+1] + 1
#                     FA += 1
#                 else:
#                     num[i] = num[i] - 1
#                     num[i+1] = num[i+1] + 1
#                     HA += 1
#     print("the {}th num is {}".format(j,num))
#     print("the number of HA is {}, the number of FA is {}".format(HA,FA))
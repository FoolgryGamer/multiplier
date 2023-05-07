num = [0]*32
FA = 0
HA = 0

for i in range(32):
    if i >= 16:
        num[i] = 31-i
    else:
        num[i] = i+1
print("origin num is")
print(num)
# stage 1



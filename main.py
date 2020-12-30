f = open("votes.txt")
lines = f.readlines()
Sum = 0
avg_list = []
print("lines in the text file is " + str(len(lines)))
for i in range(len(lines)):
    Sum = int(lines[i][0])+int(lines[i][3])+int(lines[i][6])
    avg = Sum/3
    avg_list.append(avg)
    print(str(avg))
print(avg_list)
max_avg=max(avg_list)
print("max avg is " + str(max_avg))
print("the column " +str(avg_list.index(max_avg))+" wins !")
f.close()
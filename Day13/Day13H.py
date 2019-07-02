def str_float(x):
    for i in range(4):
        x[i]=float(x[i])
    return(x)

import random
training_data=[]
test_data=[]
for line in open("iris.txt",'r'):
    temp=line[0:-1].split(',')
    if random.random()<=0.8:
        training_data.append(str_float(temp))
    else:
        test_data.append(str_float(temp))

print("data1:",len(training_data))
print("data2:",len(test_data))

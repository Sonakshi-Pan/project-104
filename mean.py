import csv

with open("height-weight.csv",newline="") as f:
    r = csv.reader(f)

    data=list(r)

#print(data) 

data.pop(0)

new_data = []
 
for i in range(len(data)):
    n = data[i][1]
    new_data.append(float(n))

total =0
l=len(new_data)

for j in new_data:
    total +=j

mean=total/l

print(mean)
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

l=len(new_data)

new_data.sort()

if l %2 ==0:
    m1 = float(new_data[l//2])
    m2 = float(new_data[l//2-1])
    m3 = (m1+m2)/2

else:
    m=  new_data(l//2)    
    print(l)

print("median is :"+str(m))    


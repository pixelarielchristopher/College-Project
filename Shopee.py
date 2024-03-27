data = [4,1,2,3,6]
print(data[len(data)-1])
total = data[0]
new_data = []
new_sum = 0

for i in range (1,len(data)-1):
    new_sum += i

if new_sum == data[len(data)-1]:
    print(new_sum)

1,3,5,7,9,10


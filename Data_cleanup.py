import pandas as pd 

file = open("discharge-coefficients.txt", "r+")
times = []
# Loop the file line by line
for line in file:
  only_times = line.split("->")
  # Add
  times.append(only_times[1])

a_times = []
b_times= [] 

final_a = [] 
final_b =[]
for line in times:

    a = line.split('2:')
    b = line.split('2:')

    a_times.append(a[0]) # times on 1
    b_times.append(b[1]) # times on 2 
   

for line in a_times:
    a = line.split ('1:')
    final_a.append(a[1])
for line in b_times:
    b = line.split('\n')
    final_b.append(b[0])

final_times = pd.DataFrame({

    'Time1' : final_a,
    'Time2' : final_b
})

print(final_times)
final_times.to_csv('discharge-coefficients.csv' , index = False, header= False)

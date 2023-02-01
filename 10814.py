import sys

t = int(input())
list = []
for i in range(t):
  [age, name] = sys.stdin.readline().split()
  list.append([int(age), name])

sorted_list = sorted(list, key=lambda x: x[0])

for i in sorted_list:
  print(i[0], i[1])
  
print("test")

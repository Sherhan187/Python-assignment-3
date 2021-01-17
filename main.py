# Python-assignment-3

#1)
num = int(input("enter num"))
x = 1
while x**2 <= num:
print(x**2, end = " ")
x += 1


#2)
x = input()
y = 0
for i in range(len(x)):
  if x[i].isdigit() == True:
    coun = 0
    for j in range(i + 1, len(x)):
      if x[j] == '!':
        coun += 1
      if coun > 2:
        break
      if coun == 2 and x[j].isdigit() == True:
        a = int(x[i]); b = int(x[j])
        if a + b == 6:
          y = 1
          break;
    if y == 1:
      break
if y != 0:
  print("True")
else:
  print("False")


#3)
x = [int(y) for y in input().split()]
coun= 0
for i in range(len(x)):
  if x[i] == 0:
    break;
  if x[i] % 2 == 0:
    coun += 1
print(coun)

#4)
x = int(input())
pow = 0
while 2**(pow + 1) <= x:
pow += 1
print(pow, 2**pow)


#5) 
def maxre(num_list):
        x, ctr = 0, 1
        
        for i in range(1, len(num_list)):
            if num_list[x] == num_list[i]:
                ctr += 1
            else:
                ctr -= 1
                if ctr == 0:
                    x = i
                    ctr = 1
        
        return num_list[x]

print(maxre([1,2,8,6,1,0,2,1]))


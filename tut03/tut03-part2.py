s = str(input("Enter String : "))
characters=list(s)
n=len(characters)

fact=1
for i in range(1,n+1):
  fact*=i

for i in range(fact):
  c=characters[:]
  permutation=""
  temp=i

  for j in range(n,0,-1):
    ind = temp % j
    permutation += c.pop(ind)
    temp //= j

  print(permutation)
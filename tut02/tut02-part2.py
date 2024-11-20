s = input("Enter string : ")

c = []
count = 1

for i in range(1, len(s)):
  if s[i] == s[i-1]:
    count += 1
  else:
    c.append(s[i-1])
    c.append(str(count))
    count = 1

c.append(s[-1])
c.append(str(count))

print(''.join(c))
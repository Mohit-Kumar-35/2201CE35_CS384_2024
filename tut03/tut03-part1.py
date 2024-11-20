def prime_or_not(n):
  if n<=1:
    return False
  if n<=2:
    return True
  if n%2==0 or n%3==0:
    return False
  i=5
  while i*i<=n:
    if n%i==0 or n%(i+2)==0:
      return False
    i+=6
  return True

def rotate_numbers(num):
  rotations = []
  s = str(num)
  for i in range(len(s)):
    rotated_number = s[i:]+s[:i]
    rotations.append(int(rotated_number))
  return rotations

def rotational_prime(num):
  rotations = rotate_numbers(num)
  for i in rotations:
    if(not prime_or_not(i)):
      return False
  return True

def main():
  num=int(input("Enter a Number : "))
  if(rotational_prime(num)):
    print(f"{num} is a Rotational Prime.")
  else:
    print(f"{num} is not a Rotational Prime.")

main()
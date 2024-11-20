def addStudent(students, name, grades):
  name = name.lower()
  if name in students:
    print(f"Student {name} already exists. Updating grades.")
    updateGrades(students, name, grades)
  else:
    students[name] = grades

def updateGrades(students, name, newGrades):
  name = name.lower()
  if name in students:
    students[name].extend(newGrades)
  else:
    print(f"Student {name} does not exist. Adding new student")
    student[name] = newGrades

def average(grades):
  return sum(grades)/len(grades)

def printing(students):
  for name, grades in students.items():
    avg = average(grades)
    print(f"{name.capitalize()} - Average: {avg:.2f}")

def sort(students):
  sorted = list(students.items())
  for i in range(len(sorted)):
    for j in range(0, len(sorted)-i-1):
      if average(sorted[j][1]) < average(sorted[j+1][1]):
        sorted[j], sorted[j+1] = sorted[j+1], sorted[j]

  return sorted

def main():
  students = {'anmol': [85, 90, 88],
              'naresh': [78, 81, 85],
              'neha': [92, 87, 90]}

  #print("Enter 1 for adding student else 0")
  ip = int(input("Enter 1 for adding student: "))

  if(ip==1):
    n1 = str(input("Enter name: "))
    marks=list(map(int,input("Enter grades: ").split()))
    addStudent(students, n1, marks)

  ip2 = int(input("Enter 1 for updating marks: "))
  if(ip2==1):
    updateGrades(students, str(input("Enter name: ")), int(input("marks 1: ","marks 2: ", "marks 3: ")))

  print("\nStudents with their average grades:")
  printing(students)

  sorted = sort(students)
  print("\nSorted way: ")
  for name, grades in sorted:
    avg = average(grades)
    print(f"{name.capitalize()} - Average: {avg:.2f}")

main()
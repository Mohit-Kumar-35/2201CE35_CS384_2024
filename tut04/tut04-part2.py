words = ["listen","silent","enlist","inlets","google","cat","tac","act"]
anagramsDictionary = {}

for word in words:
  sortedWord = ''.join(sorted(word))
  if sortedWord not in anagramsDictionary:
    anagramsDictionary[sortedWord]=[]
  anagramsDictionary[sortedWord].append(word)

print("Anagram Dictionary")
for key, value in anagramsDictionary.items():
  print(f"'{key}':{value}")
def is_balanced_or_not(s):
    matching = {')': '(', '}': '{', ']': '['}
    stack = []
    for char in s:
        if char in matching.values():
            stack.append(char)
        elif char in matching.keys():
            if stack == [] or matching[char] != stack.pop():
                return "The input string is NOT balanced."
        else:
            continue
    if stack:
        return "The input string is NOT balanced."
    else:
        return "The input string is balanced."

def main():
    s = input("Enter a string: ")
    print(is_balanced_or_not(s))

main()

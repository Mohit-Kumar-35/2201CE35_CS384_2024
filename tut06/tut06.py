def is_password_valid_or_not(password_list, criteria):
    allowed_special_chars = {'!', '@', '#'}
    results = []

    for password in password_list:
        if len(password) < 8:
            results.append(f"'{password}': Invalid password. Less than 8 Characters.")
            continue

        issues = []
        if 1 in criteria and not any(char.isupper() for char in password):
            issues.append("Missing Uppercase letters")
        if 2 in criteria and not any(char.islower() for char in password):
            issues.append("Missing Lowercase letters")
        if 3 in criteria and not any(char.isdigit() for char in password):
            issues.append("Missing Numbers")
        if 4 in criteria:
            special_chars_in_password = set(password) & allowed_special_chars
            if not special_chars_in_password:
                issues.append("Missing Special characters")
            elif not set(password).issubset(set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#')):
                issues.append("Contains invalid characters")
        if issues:
            results.append(f"'{password}': Invalid password. " + ", ".join(issues))
        else:
            results.append(f"'{password}': Valid password.")

    return results

print("Select criteria to validate passwords (enter numbers separated by commas):")
print("1. Uppercase letters (A-Z)")
print("2. Lowercase letters (a-z)")
print("3. Numbers (0-9)")
print("4. Special characters (!, @, #)")

while True:
    user_input = input("Enter your criteria: ")
    try:
        selected_criteria = list(map(int, user_input.split(',')))
        if all(criterion in {1, 2, 3, 4} for criterion in selected_criteria):
            break
        else:
            print("Invalid input. Please enter numbers from the list (1, 2, 3, 4) separated by commas.")
    except ValueError:
        print("Invalid input. Please enter numbers only (e.g., 1,3,4).")

password_list = input("Enter passwords to validate, separated by commas: ").split(',')

results = is_password_valid_or_not(password_list, selected_criteria)

for result in results:
    print(result)
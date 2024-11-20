criteria = [1 ,2 ,3 ,4]
# n =int(input("Enter the no. of criteria to be checked: "))
# for i in range(0,n):
#  cr = int(input("Enter criteria : "));
#  criteria.append(cr)
password_list = []

with open("password.txt", 'r') as file:
    password_list = file.readlines()
#password_list = input_pass_txt("/content/drive/MyDrive/Colab Notebooks/password.txt")

for password in password_list:
    password = password.strip()


# password_list = [
#     "abc12345",
#     "abc",
#     "123456789",
#     "abcdefg$",
#     "abcdefgABHD!@313",
#     "abcdefgABHD$$313"
# ]
# print(criteria)

special_characters = {'!', '@', '#'}

# print(password_list)

for password in password_list:
    if len(password) < 8:
        print(f"'{password}' is invalid. Reason: Less than 8 characters.")
        pass
    else:
        issues = []

        if 1 in criteria:
            if not any(c.isupper() for c in password):
                issues.append("Missing Uppercase letters")

        if 2 in criteria:
            if not any(c.islower() for c in password):
                issues.append("Missing Lowercase letters")

        if 3 in criteria:
            if not any(c.isdigit() for c in password):
                issues.append("Missing Numbers")

        if 4 in criteria:
            if not any(c in special_characters for c in password):
                issues.append("Missing Special characters")
            if any(c not in special_characters and not c.isalnum() for c in password):
                issues.append("Contains invalid special characters")

        if issues:
            print(f"'{password}' is invalid. Reason: {', '.join(issues)}")
        else:
            print(f"'{password}' is a valid password.")
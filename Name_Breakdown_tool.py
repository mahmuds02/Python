first_name =  input("Please enter your first name:")
last_name = input("Please enter your last name: ")
full_name = first_name+ " "+last_name
total_letters = len(first_name.replace(" ", "")) + len(last_name.replace(" ", ""))

vowels = "aeiouAEIOU"

vowel_count = sum( 1 for letter in full_name if letter in vowels)
capital_count = sum( 1 for letter in full_name if letter.isupper())

first_name_length = len(first_name)
last_name_length = len(last_name )

reveresd_letter = full_name[::-1]

print(f"\nHere are the details about your name: {first_name} {last_name}:")
print(f"1. Total number of letters: {total_letters}")
print(f"2. Number of vowels: {vowel_count}")
print(f"3. Number of capital letters: {capital_count}")
print(f"4. Number of letters in your First Name: {first_name_length}")
print(f"5. Number of letters in your Last Name: {last_name_length}")
print(f"6. Your name written backwards: {reveresd_letter}")
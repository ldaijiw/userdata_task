# userdata_task

'''
using input() to take trainee data from users
using casting and string methods to format them correctly
'''

first_name = input("What is your first name? ").lower().capitalize()

middle_name = input("What is your middle name? ").lower().capitalize()

last_name = input("What is your last name? ").lower().capitalize()

address = input("What is the first line of your address? ").lower().capitalize()

postcode = input("Please enter your postcode: ").upper()

ni_number = input("Please enter your NI number: ").upper()

course_applied = input("What course did you apply for? ").lower().capitalize()

most_recent_edu = input("What is your most recent education? ").lower().capitalize()

print(f"Hello {first_name} {middle_name} {last_name}. Your details have been saved.")
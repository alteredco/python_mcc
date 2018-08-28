# Create a greeting app. 
# It should ask the user for their name and then greet them using the name.
# eg. "Hello, (name)! How are you today?"

user_name = input("What is your name please? :")

print("Hello, " + user_name + "! How are you today?")

# below is an optional embelishment:
status = input()
if status == "bad" or status == "not good":
	print("Sorry to hear that. Hope today will get better for you.")
else:
	print("Great to hear! Have a good day!")

print("=============================")

# Create a ticket seller app.
# It should ask the user's age and then sell a ticket with the following prices:
# age 0 - 3 = free
# age 3 - 9 or 65+ = $12
# age 10 - 65 = $18
# eg."You are (age). Your ticket will be (price) dollars, please"

input_age = input("Welcome! What is the age of the person buying the ticket please?")
age = int(input_age)

if age >= 0  and age <=3:
	print("You can enter for free.")
elif (age > 3 and age <= 9) or age >= 65:
	print("That will be $12 to enter please")
else:
	print("That will be $18 to enter please")

print("=============================")

# Create an annoying backseat child app.
# The child should ask, "Are we there yet?" until the user inputs "Yes"
print("Yay! A family roadtrip!")
driver = input("Are we there yet? :")

while driver != "yes":
	print("Are we THERE YET?")
	driver = input("Are we there yet? :")
print("Yay! When are we going home?")



import os

def depression(userid):
	print(f"Hello, user #{userid}!\n")
	print("This is a depression screening survey, based on information from the MHA.\nPlease note that all fields are required. Answer honestly and to the best of your ability.\n")
	print("Over the last 2 weeks, how often have you been bothered by any of the following problems?\n")
	print("1: Never, 2: Somewhat, 3: Mostly, 4: Often\n")

	questions = ["1. Little interest or pleasure in doing things (1 - 4): ",
				 "2. Feeling down, depressed, or hopeless (1 - 4): ",
				 "3. Trouble falling or staying asleep, or sleeping too much (1 - 4): ",
				 "4. Feeling tired or having little energy (1 - 4): ",
				 "5. Poor appetite or overeating (1 - 4): ",
				 "6. Feeling bad about yourself - or that you are a failure or have let yourself or your family down (1 - 4): ",
				 "7. Trouble concentrating on things, such as reading the newspaper or watching television (1 - 4): ",
				 "8. Moving or speaking so slowly that other people could have noticed\nOr the opposite - being so fidgety or restless that you have been moving around a lot more than usual (1 - 4): ",
				 "9. Thoughts that you would be better off dead, or of hurting yourself (1 - 4): ",
				 "10. If you checked off any problems, how difficult have these problems made it for you at work, home, or with other people? (1 - 4): "]

	numsum = 0
	for q in questions:
		num = input(q)
		while (not num.isdigit()) and (num > 4 and num < 1):
			num = input("Enter a valid input from 1 to 4: ")
		if (q != questions[9]):
			numsum += int(num)-1
		if q == questions[8] and int(num) > 1:
			print("\nYour response to this question indicates that you may be at risk of harming yourself or someone else.\n",
				"If you are in need of immediate assistance, please call the National Suicide Prevention Hotline at 1-800-273-TALK, or",
				"text 'MHA' to 741-741 to talk to a trained counselor from the Crisis Text Line.\n")

	deptype = ["No", "Minimal", "Mild", "Moderate", "Moderately severe", "Severe"]
	final = 0
	if (numsum == 0):
		final = 0
	elif (numsum <= 4):
		final = 1
	elif (numsum <= 9):
		final = 2
	elif (numsum <= 14):
		final = 3
	elif (numsum <= 19):
		final = 4
	else:
		final = 5

	print(f"Your depression test score was: {deptype[final]} depression.\n")

	return final, deptype[final] 

















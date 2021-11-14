import os
import sys

def get_userinfo():
	if not(os.path.exists(".userid")):
		with open('.userid', 'w') as f:
			f.seek(0)
			f.write("0")
			f.close()

	with open(".userid", "r+") as f: # To mimic a new user being created everytime program is run
		userid = f.readline()
		f.seek(0)
		f.truncate()
		userid = int(userid)
		outnum = userid+1;
		f.write(str(outnum))
		f.close()
	age = input("Please enter your age: ")
	while (not age.isdigit()):
		age = input("Please enter a valid age (integer): ")

        # Front-end: connect all these prompts to survey interface.
		# Data: On submit, add this data to a database

	gender = input("Please indicate your gender : ").lower()

	race = input("Please indicate your race : ").lower()

	# h_i = input("Please indicate your approximate household income : ").capitalize()
	# print(h_i)

	mhc = input("Have you ever been diagnosed with a mental health condition by a professional (doctor, therapist, etc.)? (y/n) ").lower()
	while not(mhc == "y" or mhc == "n"):
		mhc = input("Please enter a valid response, either y or n: ").lower()

	mht = input("Have you ever received treatment/support for a mental health problem?? (y/n) ").lower()
	while not(mht == "y" or mht == "n"):
		mht = input("Please enter a valid response, either y or n: ").lower()

	outvec = [userid, age, gender, race, mhc, mht]
	return outvec
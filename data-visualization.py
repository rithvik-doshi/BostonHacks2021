#code is written with the data having been gathered in mind 
import matplotlib.pyplot as plt
import numpy as np
from userinfo import*

#outvec = get_userinfo() 
user_list = []
x = input("Continue? (y/n) \n")
while (x!= 'n'):
    user_list.append(get_userinfo)

def user_graph():
    print("How would you like to view your result compare to the average people surveyed in U.S?\n ")
    q = input("a. Gender, b. Race, c. Age\n").lower()
    while not( q == 'a' or q == 'b' or q == 'c'):
        q = input("Please enter valid response: (a/b/c)\n")
    if q == 'a':
        gender()
    elif q == 'b':
        race()
    elif q == 'c':
        age()
    
def depression_stats(): # base line stats that we will compare the average sample population with 
    all_x = ["male", "female", "other",
        "Natives", "Black", "Hispanic", "Pacific Islander", "White", "Asian",
        "10-17", "18-25", "26-49", "50+",
        "Diagnosed by dr",
        "treated"]
    all_stats = [ 6.2, 10.5, 22.1, 18.7, 17.3, 18.0, 16.6, 22.2, 14.4, 17.2, 20.3, 9.1, 5.4, 7.8, 32.2] 
    x_pos_all = [i for i, _ in enumerate(all_x)]
    fig, axes = plt.subplots(1, 1, figsize=(20, 11))
    plt.bar(x_pos_all[0:3], all_stats[0:3], color='green')
    plt.bar(x_pos_all[3:9], all_stats[3:9], color='cyan')
    plt.bar(x_pos_all[9:13], all_stats[9:13], color='pink')
    plt.bar(x_pos_all[13:14], all_stats[13:14], color='blue')
    plt.bar(x_pos_all[14:], all_stats[14:], color='purple')

    plt.xlabel("Categories", fontweight = "bold")
    plt.ylabel("Percentage diagnosed with depression", fontweight = "bold")
    plt.title("Depression statistics", color = 'red', fontweight = "bold")
    plt.xticks(x_pos_all, all_x)
    plt.show()
    #########################################################################################
    # Separated them out individually, in case we need to use them 
def race(): 
    # Bar Graph By race: 
    race = [ "American Natives", "Black/African American", "Hispanic/Latino", "Pacific Islander", "White", "Asian"] 
    y_race = [18.7, 17.3, 18.0, 16.6, 22.2, 14.4] #its matching the respective value of race list, source: https://www.nami.org/mhstats 
    x_pos_race = [i for i, _ in enumerate(race)]
    fig, axes = plt.subplots(1, 1, figsize=(13, 10))
    plt.bar(x_pos_race, y_race, color='green')
    plt.xlabel("Race")
    plt.ylabel("Percentage diagnosed with depression")
    plt.title("Depression: Race", color = 'red', fontweight = "bold")
    plt.xticks(x_pos_race, race)
    plt.show()
    return race, y_race
def gender():
    # Bar Graph By Gender 
    gender = ["male", "female", "other"]
    y_gender = [6.2, 10.5, 22.1 ]   # in the order of male, female, other. Source: https://www.nami.org/mhstats
    fig, axes = plt.subplots(1, 1, figsize=(13, 10))
    plt.bar(gender , y_gender, width=0.2, color='b', align='center')
    plt.xlabel("Gender")
    plt.ylabel("Percentage diagnosed with depression")
    plt.title("Depression: Gender", color = 'red', fontweight = "bold")
    plt.show()
    return gender, y_gender
def age():
    # Bar Graph by Age Group: 
    age = ["10-17", "18-25", "26-49", "50"] # age group survyed 
    y_age = [17.2, 20.3, 9.1, 5.4 ]       # in the order of the age group above. source: https://www.nami.org/mhstats
    fig, axes = plt.subplots(1, 1, figsize=(13, 10))
    plt.bar(age , y_age, width=0.2, color='b', align='center')
    plt.xlabel("Age")
    plt.ylabel("Percentage diagnosed with depression")
    plt.title("Depression: Age", color = 'red', fontweight = "bold")
    plt.show()

def cumulation(user_list):
    dep_score = 0
    for i in range(len(user_list)):
        dep_score += int(user_list[i][-1]) #im assuming the score is the last value of user
        ave_age = int(user_list[i][1])
    dep_score = dep_score / len(user_list)
    if dep_score < 19:
        print("The average person surveyed is: Not depressed")
    else:
        print("The average person surveyed is: Depressed")
    print("The average age group is: ", ave_age)
    user_graph()

user_graph()
depression_stats()
cumulation(user_list)

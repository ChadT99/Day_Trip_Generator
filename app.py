import random

destinations_list = ['Florida', 'California', 'Arizona']
restaurants_list = ['Red Lobster', 'Texas Roadhouse', 'Olive Garden']
transportation_list = ['Car', 'Plane', 'Train']
entertainment_list = ['Theme Park', 'Movie', 'Musical']

saved_destination = ''
saved_restaurant = ''
saved_transportation = ''
saved_entertainment = ''

def select_destination():
    random_number = random.randint(0,2)
    saved_destination = (destinations_list[random_number])

def select_restuarant():
    random_number = random.randint(0,2)
    saved_restaurant = (restaurants_list[random_number])

def select_transportation():
    random_number = random.randint(0,2)
    saved_transportation = (transportation_list[random_number])

def select_entertainment():
    random_number = random.randint(0,2)
    saved_entertainment = (entertainment_list[random_number])

def reroll():
    print(f'Current trip is: {saved_destination}, {saved_restaurant}, {saved_transportation}, {saved_entertainment}')
    user_choice = str(input("Do you like these options? (Yes or No): "))
    if user_choice == 'No':
         select_destination()
         select_restuarant()
         select_transportation()
         select_entertainment()
         reroll()
    print(f'Your trip is: {saved_destination}, {saved_restaurant}, {saved_transportation}, {saved_entertainment}')



select_destination()
select_restuarant()
select_transportation()
select_entertainment()
reroll()
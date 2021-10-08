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
    print(saved_destination)


select_destination()
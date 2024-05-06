# Dictionary in python is an ordered collection of key value pairs
# where each key is unique and can be assoicated with a value of any data type
# keys are restricted to integers or strings
# we create a dictionary by using {}

kitchen = {} # we did it!
print(kitchen)

# dict()
garage = dict()
print(garage)

# items in our dictionary
# the key, value pair
# key value pairs are separated by colons
# each key value pair is separated by a comma
kitchen = {
    # key   :    value
    "Spoons": "Top Drawer",
    "Plates": "Middle Shelf",
    "Cups": "Top Shelf"
}

# accessing values from a dictionary
# finding spoons
#     dictionary['key of the value we want to access']
print(kitchen["Spoons"])
# setting value from a dictionary to a variable
plate_location = kitchen["Plates"]
print(plate_location)

# be careful using integers as keys
# as it can easily be confused with indexing into a list
building = {
    1: "Reception",
    2: "Cafeteria",
    3: "Office"
}
# accessing integer keys
print(building[1])
print(building[2])

# consider using string numbers as the keys
building = {
    "1": "Reception",
    "2": "Cafeteria",
    "3": "Office"
}
print(building["1"])

# KeyError - happens when trying to access a key that doesn't exist in the dictionary
# print(kitchen["Toaster"]) #"Toaster doesnt exist"

# Adding and Updating key value pairs in a dictionary
community_center = {
    "Yoga": "8 am",
    "Art": "10 am"
}
print(community_center, "before additions")

# adding to a dictionary
# dictionary name["key to be added"] = "some value"
community_center["Karoake"] = "12 pm"
print(community_center)

community_center["Chess"] = "6 pm"

community_center["Pickup Basketball"] = "5 pm"
print(community_center)

# print(community_center[('Pickup Basketball', 'Ceramics')])
# print(community_center["Pickup Basketball"])
community_center["Pickup Soccer"] = "8 am"
print(community_center)

# Updating a value
# dictionary["key that already exists"] = "new value"
community_center["Yoga"] = "7 am"
print(community_center)
# dict.update() method
# if the key already exists it will update that key with a new value
community_center.update({"Pickup Basketball": "6 pm"})
print(community_center)
# if the key doesn't exist, it adds the new key value pair
community_center.update({"Golf": "10 am"})
print(community_center)

# SUPER COOL DICTIONARY ACTIVITY
# Organize a garage like we did with the kitchen example above
# create a dictionary called garage
# create keys in your dictionary for items you may find in a garage, like a mouse or a hammer
# the values will be the location of those items
# after you've created your dictionary with a few key value pairs
# add new items with locations either utilizing the dict["key"] = "value"
# or using dict.update()
# and also update some locations with the same methods

# removing items from a dictionary
# dictionary.pop("key to be popped", "optional default value")
# removed_activity = community_center.pop("Karoake")
# print(removed_activity)
print(community_center.pop("Karoake"))
print(community_center)

# using dict.pop() with a default value - this is a value that is returned if the key doesn't exist
print(community_center.pop("Ceramics", None))
# if a default value isnt provided and the key doesnt exist we get an error
# print(community_center.pop("Ceramics"))

# dict.popitem()
# remove the last item in our dictionary
print(community_center.popitem())
print(community_center)

# tuple - an immutable list - it is a collection of elements that cannot be changed
my_tuple = "Item 1", #tuple with a single item in it
print(my_tuple)
bigger_tuple = "Item 1", "Item 2", "Item 3"
print(bigger_tuple)
bigger_list = list(bigger_tuple)
print(bigger_list)
print(bigger_tuple[1]) #can index into a tuple
# bigger_tuple[1] = "Hello" #TypeError Tuple does not support item assignment
key_value = ("name", "Krillin")
key, value = key_value
print(key)
print(value)
# dict.items()
print(community_center.items())

# del
bookshelf = {"Fiction": 10, "Non-Fiction": 7, "Mystery": 6}
booklist = list(bookshelf) # list of dictionary keys
print(booklist)
# del dictionary["key"]
del bookshelf["Mystery"]
print(bookshelf)

# .clear()
# dictionary.clear()
bookshelf.clear()
print(bookshelf)

def add_activity(dictionary):
    item = input("What are you putting in the garage? ")
    location = input(f"Where is {item} going in the garage? ")
    dictionary[item] = location


# adding, removing from a dictionary with a while loop
def manage_schedule():
    # schedule to track events and times of our community center
    schedule = {}

    # loops until given a conidtion to break
    while True:
        # accepting user input for different options
        response = input("What would you like to do, add, update, remove, view, quit? ")

        # conditioals to check user input and see what we need to do with our dictionary
        if response == "add":
            add_activity(schedule)
            # activity = input("What activity would you like to add? ")
            # time = input("What time would you like to schedule that activity? ")
            # # sets the activity variable to the key and the time variable to value - both are storing user inputs
            # schedule[activity] = time
        elif response == "update":
            # activity to be updated
            activity = input("Which activity's time would you like to update? ")
            # checking if the activity is in our dictionary, checks that the key exists
            if activity in schedule:
                # if it does, we take time input
                time = input("What is the new time? ")
                # update the current activity key with a new time
                schedule[activity] = time
            # if it doesn't exist
            else: 
                # ask the user if they want to add it to the schedule
                response = input("That activity is not on the schedule, would you like to add it? ")
                # if they dont, we move on to other scheduling concerns
                if response == "no":
                    print("Ok, carry on")
                # if they do, then we add the new activity with a scheduled time
                elif response == "yes":
                    time = input("What time would you like to schedule that activity? ")
                    schedule[activity] = time
                else:
                    print("Please enter yes or no")
        # if response is remove
        elif response == "remove":
            # we take an activity to remove - key 
            removed_activity = input("Which activity would you like to remove? ")
            # we check if that activity is in our dictionary
            if removed_activity in schedule:
                # if it is, we set a removed variable equal to the popped value - pop by key
                removed = schedule.pop(removed_activity)
                #           key                  value
                print(f"{removed_activity} at {removed} has been removed from the schedule")
            # if it is not in the dictionary, then we tell them its not there
            else:
                print("That activity is not on the schedule!")
        # displays the dictionary
        elif response == "view":
            for activity, time in schedule.items():
                print(f"{activity} is scheduled for {time}")
        # breaks the loop
        elif response == "quit":
            print("Leaving schedule manager....")
            break
        # provides instructions in case an invalid response is entered
        else:
            print("Please enter a valid response, add, update, remove, view, quit...")
    return schedule
# manage_schedule()

# Create a program for organizing our garage
# Write a function that declares an empty dictionary
# use a while loop to accept user input to add, update an items location, remove an item, view garage, quit
# add an item with a location to the garage
# update an items location
# remove an item from the garage
# view and appreciate all your hard work
# quit cleaning the garage

# Looping through a dictionary
# .keys()
# .values()
# .items()

user_profile = {"name": "Alice", "age": 30, "email": "alice@gmail.com"}
for key in user_profile:
    print(key)
# .keys() returns a list with my dictionary's keys
print(user_profile.keys())
for key in user_profile.keys():
    print(key)

# .values() 
# accesssing values with a loop without .values()
for key in user_profile:
    print(user_profile[key])
print(user_profile.values())

for value in user_profile.values():
    print(value)

# .items()
temps = {"Monday": 70, "Tuesday": 67, "Wednesday": 60, "Thursday": 76, "Friday": 74}
print(temps.items())
for day, temp in temps.items():
    print(f"On {day} its going to be {temp} degrees")
# without items
for key in temps:
    print(f"On {key} its going to be {temps[key]} degrees")

# using sorted() a dictionaries keys
addresses = {
    "Ryan": "1123 Main st",
    "Victor": "12345 Cool St",
    "Andy": "7435 Tree st",
    "Farzin": "23465 Aurora Street"
}
print(sorted(addresses))
for key in sorted(addresses):
    print(f"{key}: {addresses[key]}")

# addresses.sort() Attribute Error: Dict object has no attribute sort

# A little extra sauce on the .update()
# combining two dictionaries
default_settings = {"theme": "light", "notifications": "on"}
user_settings = {"status": "active", "followers": 100}
default_settings.update(user_settings)
print(default_settings)

#.get()
addresses = {
    "Ryan": "1123 Main st",
    "Victor": "12345 Cool St",
    "Andy": "7435 Tree st",
    "Farzin": "23465 Aurora Street"
}
friends_address = addresses.get("Victor")
print(friends_address)
# what if the key doesnt exist?
potential_friends_address = addresses.get("Winter")
print(potential_friends_address)
# .get() with the second optional argument
be_my_friend = addresses.get("Winter", "Winter, pls")
print(be_my_friend)

# dictionary.setdefault()
another_friend = addresses.setdefault("Andy")
print(another_friend)
# no key is found in the dictionary
# because spencer is not in the dictionary and we're not giving the optional arugment to set the value to
# spencer is added as a key with a value of None
hopefully_friend = addresses.setdefault("Spencer")
print(hopefully_friend)
print(addresses)
# adding a second argument
# with the second argument, 172 Green Square gets added as the value to the key of Spencer
hopefully_friend = addresses.setdefault("Spencer", "172 Green Square")
# print(addresses)







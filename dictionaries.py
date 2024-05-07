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

# Shallow Copy vs Deep Copy
original_artists = {"Picasso": 1881, "Van Gogh": 1853, "Monet": 1840}
copied_artists = original_artists.copy()

copied_artists["Van Gogh"] = 1900
print("Original", original_artists) #original remains unchanged
print("Copied", copied_artists) #copy reflect that change

# creating a deep copy - create a totally new independent dictionary
import copy
original_paintings = {"The Starry Night": "Van Gogh", "The Scream": "Munch"}
reproduced_paintings = copy.deepcopy(original_paintings)
reproduced_paintings["The Starry Night"] = "Da Vinci"
print("Original", original_paintings) #Original remains unchanged
print("Copied", reproduced_paintings) # copy reflects the changes

# how does a change affect a shallow copy
# specifically with values that are mutable - such as a lost
museum_exhibit = {
    "Ancient Vase": ["Greece", "Egypt"],
    "Renaissance Painting": ["Italy", "France"]
}

# creating shallow copy
exhibit_copy = museum_exhibit.copy()
# adding a country to the ancient vase exhibit
# this will also alter the original dictionary
exhibit_copy['Ancient Vase'].append("China")
print("Original Exhibit", museum_exhibit)
print("Copied Exhibit", exhibit_copy)

# NESTED DICTIONARIES and LISTS
# Dictionaries with values that are other dictionaries
# Dictionaries with values that are lists

# Lists as values in dictionaries
library = {
    "Fantasy": ["The Hobbit", "The Lord of the Rings"],
    "Science Fiction": ["Dune", "Neuromancer", "The Name of the Wind"],
    "Mystery": ["Sherlock Holmes", "And Then There Were None"]
}

print(library["Fantasy"]) # accesses the list associated with the "Fantasy" key
# accessing The Lord of the Rings
print(library["Fantasy"][1])
# appending to a list in a dictionary
library["Science Fiction"].append("The Road")
print(library) # print whole dictionary
print(library["Science Fiction"]) #specifically accessing the value of the Science Fiction Key
library["Fantasy"].remove("The Hobbit")
print(library["Fantasy"])

# looping through lists in dictionaries
for book in library["Science Fiction"]:
    print(book)


# looping through our dictionary and then through the list values
# using dict.items()
print(library.items())
for genre, books in library.items():
    print(f"Genre: {genre}, Books: {books}")
    # for book in books:
    #     print(f" - {book}")
    # ^^^ this makes it pretty \(￣︶￣*\))

# dictionaries in lists
art_gallery = [
    {"Title": "Starry Night", "Artist": "Van Gogh", "Year": 1889},
    {"Title": "The Scream", "Artist": "Munch", "Year": 1893},
    {"Title": "Guernica", "Artist": "Picasso", "Year": 1937}
]

# adding to our list of dictionaries
art_gallery.append({"Title": "The Persistence of Memory", "Artist": "Dali", "Year": 1931})
# looping through a list of dictionaries
#   artwork represents each dictionary in my list
for artwork in art_gallery:
    print(f"Title: {artwork['Title']}, Artist: {artwork['Artist']}, Year: {artwork['Year']}")

# Nested dicionaries
# a dictionary where a key has a value that is another dictionary
museum_exhibit = {
    "Ancient Egypt": {
        "Artifacts": ["Sphinx", "Pyramids"],
        "Famous Pharaohs": ["King Tut", "Cleopatra"]
    },
    "Renaissance Art": {
        "Notable Artists": ["Da Vinci", "Michelangelo", "Donatello", "Rafael"],
        "Key Works": ["Mona Lisa", "The Last Supper", "That Cool Sculpture", "David", "Sistine Chapel"]
    }
}

# adding new key, value pairs to a nested dictionary
# accessing the Ancient Egypt Key and then adding another key to that dictionary called "Revent Discoveries"
# dictionary    Ancient Egypt Key   adds a new key called Recent Discovers 
museum_exhibit["Ancient Egypt"]["Recent Discoveries"] = ["New Tomb", "Ancient Scrolls"] # the value to the key of Recent Discoveries
print(museum_exhibit)
# accessing the newly added key,value pair 
print(museum_exhibit["Ancient Egypt"]["Recent Discoveries"])
# check point variables
renaissance_art = museum_exhibit["Renaissance Art"]
print(renaissance_art)
renaissance_art["Cool Weapons"] = ["Dope Sword", "Neat Pike", "Nice Axe"]

print(renaissance_art)

# looping through nested dictionaries
for exhibit, details in museum_exhibit.items():
    print(f"Exhibit: {exhibit}")
    for section, items in details.items():
        print(f"  {section}:")
        for item in items:
            print(f" - {item}")

for exhibit in museum_exhibit:
    print(f"Exhibit: {exhibit}")
    for section in museum_exhibit[exhibit]:
        print(f" {section}")
        for item in museum_exhibit[exhibit][section]:
            print(f" - {item}")


    
museum_exhibit = {
    # exhibit
    "Ancient Egypt": { #details
        # section        items
        "Artifacts": ["Sphinx", "Pyramids"],
                        # item     item
        # section        items
        "Famous Pharaohs": ["King Tut", "Cleopatra"]
        #                      item           item
    },
    # exhibit
    "Renaissance Art": { #details
        # section                    items
        "Notable Artists": ["Da Vinci", "Michelangelo", "Donatello", "Rafael"],
        #                      item            item         item         item
        # section                    items
        "Key Works": ["Mona Lisa", "The Last Supper", "That Cool Sculpture", "David", "Sistine Chapel"]
                        # item         item                  item                item       item
    }
}

#   iterator variable names                    keyword
for exhibit, details in museum_exhibit.items():
    print(f"Exhibit: {exhibit}")
    # iterator variable names           keyword
    for section, items in details.items():
        print(f"  {section}:")
    # iterator variable   variable
        for item in items:
            print(f" - {item}")

names = ["King Tut", "Cleopatra"]
for name in names:
    print(name)

# Creating a nested dictionary from an empty dictionary
book_shelf = {}
# adding a key to my book_shelf with a value that is an empty dictionary
book_shelf["Star Wars"] = {}
print(book_shelf)
# print(book_shelf["Star Wars"])
book_shelf["Pokemon"] = {} # book_shelf["Pokemon"] = {"Cards": ["Charizard", "Pichu", "Heracross"], "Bobble Head": "Charmander", "Toy": "Dragonite"}
book_shelf["Yugioh"] = {}
print(book_shelf)
# adding key value pairs to our nested dictionaries
# Star Wars
star_wars = book_shelf["Star Wars"]
print(star_wars)
# check point variable to get into the Star Wars Key - which is currently 
# an empty dictionary
star_wars["Legos"] = "Boba Fett Helmet"
print(book_shelf)
# book_shelf["Star Wars"]["Legos"] = "Boba Fett Helmet"
book_shelf["Pokemon"] = {"Cards": ["Charizard", "Pichu", "Heracross"], "Bobble Head": "Charmander", "Toy": "Dragonite"}
print(book_shelf)
print(book_shelf["Star Wars"]["Legos"])
print(book_shelf["Pokemon"]["Cards"][2])

# collection = input("What card collection do you have? ")
# card = input("What card would you like to add from the collection")
# book_shelf["Yugioh"] = {collection: card}

print(book_shelf)
print(book_shelf["Yugioh"])
# book_shelf["Pokemon"]["Book"] KeyError we need to add a value when adding a key


# create a function with a while loop that will add different shelf categories to your book shelf
# each category should have at least one value
# have at least one nested dictionary with at least 3 key value pairs
# if youre feelin saucy, make one of your nested dictionary values a list
# take some time to plan the structure of your dictionary
# have a nice time


















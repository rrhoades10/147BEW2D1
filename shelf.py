
def manage_shelf():
    # declares and empty dictionary
    shelf = {"Book": {}, "Nic Nacs": {}, "Photos": {}}
    

    while True:
        # ask the user what theyd like to do add category, add to category, view
        response = input("1. Add to Category 2. View 3. Quit")
        if response == "1":
            # takes user input for a shelf category
            category = input("What Category would you like to add to? 1. Book 2. Nic Nacs 3. Photos")
            # add the category as a key to the dictionary and give it a value of an empty dictionary
            if category == "1":
                author = input("What is the name of the author? ")
                book_title = input("What is the title of the book? ")
                shelf["Book"][author] = book_title
                print(shelf)
                print(shelf["Book"])
            elif category == "2":
                item = input("What is your special little Nic Nac? ")
                feelings = input("What does it mean to you? ")
                shelf["Nic Nacs"][item] = feelings
                print(shelf)
                print(shelf["Nic Nacs"])
            elif category == "3":
                year = input("What year was the picture taken? ")
                picture = input("What is the picture of? ")
                if year not in shelf["Photos"]:
                    shelf["Photos"][year] = [picture]
                    print(shelf["Photos"])
                else:
                    shelf["Photos"][year].append(picture) 
                    print(shelf["Photos"])            
                
                
                
            elif category == "2":
                pass
            elif category == "3":
                pass
        elif response == "2":
            for category, things in shelf.items():
                print(category)
                for item, description in things.items():
                    print(f"{item}: {description}")          
                     
            

          
        elif response == "3":
            print("Thats a nice shelf")
            break     
        else:
            print("Please enter a valid response")

# manage_shelf()


# contact_list = {
#     "ryuan@gmail.com": {"name": "Ryan Rhoades", "phone": "238746238764", "address": "7816oc2736"}
# }
  
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def update_ticket(ticket_dict, ticket_number):
    ticket_dict[ticket_number]["Status"] = "closed"
    return f"Updated ticked number {ticket_number}"

update_ticket(service_tickets, "Ticket001")
print(service_tickets)





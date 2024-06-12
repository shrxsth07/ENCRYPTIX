print('''=================================
 WELCOME TO CONTACT BOOK PROGRAM
=================================''')
print("\n")

contact_book = {}                                                              #A empty dictionary

while (True):
    choice = int(input('''1. Add a New Contact 
2. Search a Contact 
3. Display a Contact
4. Edit a Contact 
5. Delete a Contact
6. Exit
Enter your choice - '''))
    print("\n")
    if (choice==1):
        name=input("Please enter the Contact Name - ")
        number=input("Please enter the Mobile Number - ")
        print("\n")
        contact_book[name]=number                                              #Storing data

        
    elif (choice==2):
        search=input("Please provide the contact name - ")

        if search in contact_book:
            print(search," contact number is - ",contact_book[search])         #displaying a single contact
            print("\n")
            
        else:
            print("NOT FOUND, Please provide a valid name...")
            print("\n")

            
    elif (choice==3):
        
        if not contact_book:
            print("NO DATA")
            print("\n")
            
        else:
            print("Name\t\tContact Number")                                    #displaying all data
            for key in contact_book:
                print(key,"\t",contact_book.get(key))
            print("\n")

            
    elif (choice==4):
        edit_contact=input("Please enter the contact name you want to edit - ")
        
        if edit_contact in contact_book:
            phone=input("Please enter the new Mobile Number - ")
            contact_book[edit_contact]=phone                                    #edit contact
            print("Contact has been Updated")
            print("Name\t\tContact Number")                                    #displaying all data
            for key in contact_book:
                print(key,"\t",contact_book.get(key))
            print("\n")
            
        else:
            print("NOT FOUND, Please provide a valid name...")
            print("\n")

            
    elif (choice==5):
        del_contact=input("Please enter the contact you want to delete - ")
        
        if del_contact in contact_book:
            confirm=input("Are you sure you want to exit (Y/N) ? ")
            if (confirm=='y' or confirm=='Y'):
                contact_book.pop(del_contact)                                         #delete contact
            if not contact_book:
                print("NO DATA")
                print("\n")
                
            else:
                print("Name\t\tContact Number")                                    #displaying all data
                for key in contact_book:
                    print(key,"\t",contact_book.get(key))
                print("\n")
            
        else:
            print("NOT FOUND, Please provide a valid name...")
            print("\n")

            
    else:
        break                                                                    #exit the program   

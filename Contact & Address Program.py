print('''=================================
 WELCOME TO CONTACT BOOK PROGRAM
=================================''')
print("\n")

contact_book={}                                                              
address_book={}

while (True):
    choice = int(input('''1. Add a New Contact and Address
2. Search a Contact or Address
3. Display a Contact or Address
4. Edit a Contact or Address
5. Delete a Contact or Address
6. Exit
Enter your choice - '''))
    print("\n")
    if (choice==1):
        name=input("Please enter the Contact Name - ")
        number=input("Please enter the Mobile Number - ")
        add=input("Please enter the Address - ")
        print("\n")
        contact_book[name]=number                                              
        address_book[name]=add
        
        
    elif (choice==2):
        n=int(input("Press 1 for ADDRESS, 2 for CONTACT, 3 for BOTH - "))
        search=input("Please provide the contact name - ")

        if(n==1):
            if search in address_book:
                print(search," address is - ",address_book[search])              
                print("\n")
                
            else:
                print("Address NOT FOUND, Please provide a valid name...")
                print("\n")

        elif(n==2):
            if search in contact_book:
                print(search," contact number is - ",contact_book[search])  
                print("\n")
                
            else:
                print("Contact NOT FOUND, Please provide a valid name...")
                print("\n")

        else:
            if (search in contact_book and search in address_book):
                print(search," contact number is - ",contact_book[search])
                print(search," address is - ",address_book[search])
                print("\n")
                
            else:
                print("DATA NOT FOUND, Please provide a valid name...")
                print("\n")
        

        
            
    elif (choice==3):
        
        if not contact_book:
            print("NO Contacts")
        if not address_book:
            print("NO Address")
            
        else:
            print("Name\t   Contact Number")                                    
            for key in contact_book:
                print(key,"\t\t",contact_book.get(key))
            print("\n")
            print("Name\t\t Address")                                    
            for key in address_book:
                print(key,"\t\t",address_book.get(key))
            print("\n")

            
    elif (choice==4):
        n=int(input("Press 1 for ADDRESS, 2 for CONTACT - "))
        edit_contact=input("Please enter the contact name you want to edit - ")

        if(n==2):
            if edit_contact in contact_book:
                phone=input("Please enter the new Mobile Number - ")
                contact_book[edit_contact]=phone                                    
                print("Contact has been Updated")
                print("Name\t   Contact Number")                                    
                for key in contact_book:
                    print(key,"\t\t",contact_book.get(key))
                print("\n")
                
                
            else:
                print("NOT FOUND, Please provide a valid name...")
                print("\n")

        else:
            if edit_contact in address_book:
                address=input("Please enter the Address - ")
                address_book[edit_contact]=address                                   
                print("Address has been Updated")
                print("Name\t\t Address ")                                    
                for key in contact_book:
                    print(key,"\t\t",address_book.get(key))
                print("\n")
                
                
            else:
                print("NOT FOUND, Please provide a valid name...")
                print("\n")

            
    elif (choice==5):
        del_contact=input("Please enter the contact you want to delete - ")
        confirm=input("Are you sure you want to continue (Y/N) ? ")
        if (confirm=='y' or confirm=='Y'):
                contact_book.pop(del_contact)
                address_book.pop(del_contact)
                print("Contact deleted successfully")
                print("\n")
        

    else:
        print("Thank You !!!")
        exit(0)                                                                   


# Person to Shoe CLI

This CLI was created for a user to keep track of owners and their shoes. The application is a simple command line interface. It lists the shoe owners in the database and displays them to the user. In the main menu, the user has the ability to create an owner, select an owner or exit the program. If the user selects and owner they will be taken to the owner menu with new options. They can update or delete the owner. They can create, update or delete a shoe under that owner, they can also go back to the main menu or exit the program. 
## Features

- Main menu displays all of the owners. 
- Select owner - Goes to the owner menu for that owner
- Create owner - Creates a new owner
- Update owner - Change an existing owners name
- Delete owner - Delete an existing owner
- Create shoe - Create a new shoe
- Update shoe - Update an attribute(s) of an existing shoe
- Delete shoe - Delete an existing shoe
## Deployment

To deploy this project run the program and start adding owners and shoes with the avaliable options on screen.


## Authors

- [@Gonzo2510](https://github.com/Gonzo2510)


## Appendix

cli.py - is the application file that has the list of options to choose from and thier imports. 

__inin__.py initializes the database file

person.py contains the Person class and its properties and functions

shoe.py contains the Shoe class and its properties and functions

shoe_tracker.db is the database file that will store all of the shoe and owner data

helpers.py holds the main functions stored in import in the cli file. 
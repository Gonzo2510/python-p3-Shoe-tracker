# Owner to Shoe CLI

A brief description of what this project does and who it's for
This CLI was created for any user who would like to keep track of owners who have specific pairs of shoes. The application is a simple command line interface with options to create/update/delete owners and shoes. Additinally you can also view the owners and shoes in your database file. 

## Features

- Create owner - Create a new owner
- Update owner - Change an existing owners name
- Delete owner - Delete an existing owner
- List owners - View all owners in the database file
- Find owner by id - find a owner by their id
- Create shoe - Create a new shoe
- Update shoe - Update an attribute(s) of an existing shoe
- Delete shoe - Delete an existing shoe
- List shoes - List all shoes in the database
- List shoes by owner id - List all shoes of a specfic owners id
## Deployment

To deploy this project run the program and create the database with choice 11. Choose any option of your choice after that and follow the prompts on screen. 


## Authors

- [@Gonzo2510](https://github.com/Gonzo2510)


## Appendix

cli.py - is the application file that has the list of options to choose from and thier imports. 

__inin__.py initializes the database file

owner.py contains the Owner class and its properties and functions

shoe.py contains the Shoe class and its properties and functions

data.db is the database file that will hold all of the information

helpers.py holds the main functions stored in import in the cli file. 
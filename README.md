# Person to Shoe CLI

A brief description of what this project does and who it's for
This CLI was created for any user who would like to keep track of people who have specific pairs of shoes. The application is a simple command line interface with options to create/update/delete people and shoes. Additinally you can also view the people and shoes in your database file. 

## Features

- Create person - Create a new person
- Update person - Change an existing persons name
- Delete person - Delete an existing person
- List persons - View all people in the database file
- Find person by id - find a person by their id
- Create shoe - Create a new shoe
- Update shoe - Update an attribute(s) of an existing shoe
- Delete shoe - Delete an existing shoe
- List shoes - List all shoes in the database
- List shoes by person id - List all shoes of a specfic persons id
## Deployment

To deploy this project run the program and create the database with choice 11. Choose any option of your choice after that and follow the prompts on screen. 


## Authors

- [@Gonzo2510](https://github.com/Gonzo2510)


## Appendix

cli.py - is the application file that has the list of options to choose from and thier imports. 

__inin__.py initializes the database file

person.py contains the Person class and its properties and functions

shoe.py contains the Shoe class and its properties and functions

data.db is the database file that will hold all of the information

helpers.py holds the main functions stored in import in the cli file. 
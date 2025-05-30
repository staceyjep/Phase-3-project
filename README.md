# FILM DATABASE CLI APP
# AUTHOR
STACEY TAREI

# EXPLANATION
A command-line interface (CLI) application to manage a simple film database with **Movies**, **Directors**, **Actors**, and **Crew Members**, built using Python and SQLAlchemy ORM.



# PROJECT STRUCTURE 
Project folder/
        lib/
            models/
                   movie.py
                   actors.py
                   base.py
                   crew.py
                   directors.py
                   __init__.py
            helpers.py
        cli.py-for commandline interaction
        debug.py-test application as it is built
        seed.py-populate database
        helpers.py-store all functions for the project

# PROJECT STARTUP 
step 1 : Clone this repository into your local storage.
step 2 : install necessary dependancies 
step 3 : run python cli.py in your terminal

# FUNCTIONALITY 
COMMANDS 
1.Add New Entry-adds to the data in the database using a series of propmpts to the user
2.View all entries-Provides the user with a lsit of the data in the database showing the relationships between them.The user can choose what they want to be listen making it easier for them
3.Delete an entry-Provides the user with the ability to choose what to delete as the user can specify what exactly it is they want removed from the database by use of the select by name method
4.Clear entire database-Provides the user with the ability to clear the whole database in the event of they want to start afresh.
5.Exit-This is the input that allows the user to leave the loop.

# ACKNOWLEDGMENTS
Filmify was supported by resources and documentation from Python SQLite3 Documentation and Pipenv Documentation.

# CONTACTS
For any further questions or inquires, kindly contact the author at 
@staceyjepchumbarr@gmail.com / +245728668849
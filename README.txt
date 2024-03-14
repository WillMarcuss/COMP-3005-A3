William Marcus
COMP 3005 Assignment 3 Question 1
101219545

Video Link: https://youtu.be/iOhXH3cDaUI?si=w5aYb85k0OPTT8Av

Steps to compile and run application:

1. Set environemnt variables (steps for mac and linux)
    export DB_NAME=your_database_name
    export host=your_host_name
    export port=your_db_port
    export user=your_user_name
    export password=your_password

2. Run the program!
    Simply run the python script by executing: 
        python3 program.py
    The program will automatically create the table within the database provided in the environemnt
    variable, and insert the tuples if they do not exist.

3. Select 1,2,3,4,5 based on your desired query
    The program will prompt you to choose a number, (it does not check for invalid input) and once you
    choose one, it will either display the results of the query, or prompt you again for more required input.
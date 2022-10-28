- # 0x00. AirBnB clone - The console
## 1- Description of the project
        # Do this to show shell documentation
        >>> help(AirBnB_shell)

This is a clone project of the "AirBnB" web application. This first step consists in developing a command prompt allowing to manage (create, modify or delete) objects of the future projects. Note that we manage objects in a file system and a database.

## 2- Description of the Command Interpreter

#### a- How to start it
Position yourself in the project directory and then run the console

        $ cd AirBnB_clone/models/
        >>> ./console.py

### b- How to use it & Examples

This was an example for an object placed to create a new location in the filesystem


	>>> ./console.py
	------------------------------
	|                            |
	|  Welcome to the CLI AirBnB |
	------------------------------
	
	(hbnb) ?
	
	Documented commands (type help <topic>):
	========================================
	EOF  help  quit create_object update_object
	destroy_object print_all_objects State Place
	City

	(hbnb) create_object Place name="Douala"
	b6a6e15c-c67d-4312-9a75-9d084935e579



#!/usr/bin/python3
"""
Module that contains the class that is looped to take use input
and call the correct method based on user input
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import models
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that is looped to take use input and call the correct method

    Methods:
        do_create(args): Creates an instance of user given class
        do_show(args): Prints the dict of an instance give in args
        do_destroy(args): Deletes a specific (user given) instance
        do_all(args): Prints all instances or specific class instances
        do_quit(): Ends the program when user types "quit"
    """
    prompt = '(hbnb) '

    def validate_args(self, name, id):
        """Method to validate args given by user

        Args:
            name (str): Name of the class to check
            id (str): id for class instance to check

        Returns:
            True: if an error was found
        """
        if not name:
            print("** class name missing **")
            return True
        elif not id:
            print("** instance id missing **")
            return True
        elif name not in globals():
            print("** class doesn't exist **")
            return True

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.

        Args:
            args (str): <Class name>
        """
        # Check if no arguments were provided by the user.
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            # Attempt to evaluate 'args' to interpret the class name provided by the user as a class reference.
            name = eval(args)
            # Create an instance of the class referred to by 'args'.
            instance = name()
            # Print the unique ID of the newly created instance.
            print(instance.id)
            # Save the instance to the JSON file, as per method definition.
            instance.save()
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Method to update the attribute of an instance

        Args:
            args (str): <Class name> <id> <attribute to update> "<new value>"
        """
        command = args.split()
        # Assigns 1st part to 'name', if not present then defaults to empty string
        name = command[0] if len(command) > 0 else ""
        # Assigns 2nd part to 'id', if not present then defaults to empty string
        id = command[1] if len(command) > 1 else ""
        # Assigns 3rd part to 'attr_name', if not present then sets value will be assigned the value None.
        attr_name = command[2] if len(command) > 2 else None
        # Assigns 4th part to 'new_value', if not present then sets value will be assigned the value None.
        new_value = command[3] if len(command) > 3 else None

        # Validates the name and id args using custom 'validate_args'
        if self.validate_args(name, id):
            return
        # If attr_name is missing print error.
        elif attr_name is None:
            print("** attribute name missing **")
            return
        # If new_value is missing print error.
        elif new_value is None:
            print("** value missing **")
            return
        # Creates 'key' by concatenating 'name' with 'id'
        key = name + "." + id
        # Checks if the instances is in storage, if not print error.
        if key not in storage.all():
            print("** no instance found **")
            return
        # Retrieves the instance from storage using the [key]
        instance = storage.all()[key]
        # Checks if the instance has teh attributes to be updated.
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            # Got the type of the current value of the attribute.
            if attr_type == int:
                # Converts to int.
                new_value = int(new_value)
            elif attr_type == float:
                # Converts to float.
                new_value = float(new_value)
        # Update the instances of attributes with the 'new_value'
        setattr(instance, attr_name, new_value)
        # Save storage.save()
        storage.save()

    def do_show(self, args):
        """Method to show the user the str of a valid instance

        Args:
            args (str): <Class name> <id>
        """
        command = args.partition(" ")
        name = command[0]
        id = command[2]

        # Validate the provided class name and ID using a custom validation method
        # If the validation fails (method returns True), exit the method early
        if self.validate_args(name, id):
            return
        # Create a unique key by concatenating the class name and instance ID
        key = name + "." + id
        try:
            # Attempt to retrieve the instance from the storage using the unique key
            # 'storage.all()' is expected to return a dictionary of all instances
            # If the key is found, print the string representation of the instance
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Method to delete an instance

        Args:
            args (str): <Class name> <id>
        """
        command = args.partition(" ")
        # Method to delete an instance based on class name and instance ID

        # Split 'args' into the class name and instance ID using partition
        # 'command' will be a tuple: (class name, " ", instance ID)
        name = command[0]
        id = command[2]
        # Validate the provided arguments (class name and ID)
        # If validation fails, the function returns early
        if self.validate_args(name, id):
            return
        # Construct the key by concatenating class name and instance ID
        key = name + "." + id
        # Attempt to remove the instance from the storage
        # 'storage.all()' returns a dictionary of all instances
        # '.pop(key)' removes the item with the key and returns its value
        try:
            # Save changes to the storage
            storage.all().pop(key)
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Method to print all instances or all of specific class

        Args:
            args (str): optional[<Class name>]
        """
        # Retrieve a dictionary of all instances from the storage.
        obj_dict = storage.all()
        # Initialize an empty list to hold the formatted string representations of instances.
        obj_list = []
        # If no arguments were provided, process all instances regardless of their class.
        if not args:
            for value in obj_dict.values():
                # For each instance, format a string with its class name, id, and a dictionary representation.
                # Add this formatted string to the list of instance representations.
                obj_list.append(f"[{value.__class__.__name__}] ({value.id})\
                                 {str(value.to_dict())}")
            # Print the list of all instance representations.
            print(obj_list)
            return

        # If an argument was provided, it's considered the name of the class to filter by.
        class_name = args
        # Check if there is any instance of the specified class in the storage.
        if not any(key.startswith(class_name + ".") for key in obj_dict):
            # If no instances of the class exist, notify the user and exit.
            print("** class doesn't exist **")
            return
        # If instances of the specified class exist, filter and process them.
        for key, value in obj_dict.items():
            # Check if the instance belongs to the specified class based on the key.
            if class_name in key:
                # Format a string with the class name, id, and a dictionary representation of the instance.
                # Add this formatted string to the list of instance representations.
                obj_list.append(f"[{class_name}] ({value.id})\
                                 {str(value.to_dict())}")
        print(obj_list)

    def do_quit(self, arg):
        """Gives the user the ability to end the program

        Args:
            args (str): quit

        Returns:
            Bool: True ends the cmdloop method and stops the console
        """
        return True

    def do_EOF(self, arg):
        """Ends the program when use types ctrl-d

        Returns:
            Bool: True ends the cmdloop method and stops the console
        """
        return True

    def emptyline(self):
        """Used if no command is given by user
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

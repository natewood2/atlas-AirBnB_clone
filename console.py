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
            args (str): String of the commands given by the user
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            name = eval(args)
            instance = name()
            print(instance.id)
            instance.save()
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Method to update the attribute of an instance

        Args:
            args (str): <Class name> <id> <attribute to update> "<new value>"
        """
        command = args.split()
        name = command[0] if len(command) > 0 else ""
        id = command[1] if len(command) > 1 else ""
        attr_name = command[2] if len(command) > 2 else None
        new_value = command[3] if len(command) > 3 else None

        if self.validate_args(name, id):
            return
        elif attr_name is None:
            print("** attribute name missing **")
            return
        elif new_value is None:
            print("** value missing **")
            return
        key = name + "." + id
        try:
            instance = storage._FileStorage__objects[key]
            if hasattr(instance, attr_name):
                setattr(instance, attr_name, type(getattr(instance, attr_name))(new_value))
                instance.save()
        except KeyError:
            print("** no instance found **")

    def do_show(self, args):
        """Method to show the user the str of a valid instance

        Args:
            args (str): Contains the name of the class and
                the id of the instance to show
        """
        command = args.partition(" ")
        name = command[0]
        id = command[2]
        if self.validate_args(name, id):
            return
        key = name + "." + id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """Method to delete an instance

        Args:
            args (str): Contains the name of the class and
                the id of the instance to delete
        """
        command = args.partition(" ")
        name = command[0]
        id = command[2]
        if self.validate_args(name, id):
            return
        key = name + "." + id
        try:
            storage._FileStorage__objects.pop(key)
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, args):
        """Method to print all instances or all of specific class

        Args:
            args (str): Optional to state class  to print
        """
        obj_dict = storage._FileStorage__objects
        obj_list = []
        if not args:
            for value in obj_dict.values():
                obj_list.append(f"[{value.__class__.__name__}] ({value.id}) {str(value.to_dict())}")
            print(obj_list)
            return

        class_name = args
        if not any(key.startswith(class_name + ".") for key in obj_dict):
            print("** class doesn't exist **")
            return
        for key, value in obj_dict.items():
            if class_name in key:
                obj_list.append(f"[{class_name}] ({value.id}) {str(value.to_dict())}")
        print(obj_list)

    def do_quit(self, arg):
        """Gives the user the ability to end the program

        Args:
            arg (_type_): _description_

        Returns:
            Bool: True ends the cmdloop method and stops the console
        """
        return True

    def do_EOF(self, arg):
        """Ends the program if the eof is reached

        Args:
            arg (_type_): _description_

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

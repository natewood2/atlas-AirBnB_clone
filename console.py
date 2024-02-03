#!/usr/bin/python3
"""
Module that contains the class that is looped to take use input
and call the correct method based on user input
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that is looped to take use input and call the correct method

    Methods:
        do_create(args): Creates an instance of user given class
        do_show(args): Prints the dict of an instance give in args
        do_quit(): Ends the program when user types "quit"
    """
    prompt = '(hbnb) '

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
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Method to show the user the str representation of a valid instance

        Args:
            args (str): String of the commands given by the user
        """
        command = args.partition(" ")
        name = command[0]
        id = command[2]
        if len(args) == 0:
            print("** class name missing **")
            return
        elif not id:
            print("** instance id missing **")
            return
        elif name not in globals():
            print("** class doesn't exist **")
            return
        key = name + "." + id
        try:
            print(storage._FileStorage__objects[key])
        except:
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
        if len(args) == 0:
            print("** class name missing **")
            return
        elif not id:
            print("** instance id missing **")
            return
        elif name not in globals():
            print("** class doesn't exist **")
            return
        key = name + "." + id
        try:
            storage._FileStorage__objects.pop(key)
            storage.save()
        except:
            print("** no instance found **")

    def do_all(self, args):
        """Method to print all instances or all instances of specific class

        Args:
            args (str): Optional argument to state class of instances to print
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

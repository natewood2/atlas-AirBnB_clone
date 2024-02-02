#!/usr/bin/python3
""" THE CONSOLE. """
import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """ cmd module. """
    prompt = '(hbnb) '

    def do_create(self, args):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """

        if len(args) == 0:
            print("** class name missing **")
            return

        try:
            model = eval(args)
            instance = model()
            print(instance.id)
            instance.save()
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        command = args.partition(" ")
        model = command[0]
        id = command[2]
        if len(args) == 0:
            print("** class name missing **")
            return
        elif not id:
            print("** instance id missing **")
            return
        key = model + "." + id
        try:
            print(storage._FileStorage__objects[key])
        except:
            print("** no instance found **")

    def do_quit(self, arg):
            return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

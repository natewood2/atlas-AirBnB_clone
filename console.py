#!/usr/bin/python3
""" THE CONSOLE. """
import cmd
from models.base_model import BaseModel


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

    def do_quit(self, arg):
            return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
""" THE CONSOLE. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ cmd module. """
    prompt = '(hbnb) '

    def create(self, args):
        """ Creates a new instance of BaseModel, saves it 
        (to the JSON file) and prints the id. 
        """
        arguments = args.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        try:
            instance = eval(arguments[0])
            instance.save()
            print(instance.id)
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
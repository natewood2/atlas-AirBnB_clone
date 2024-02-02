#!/usr/bin/python3
""" THE CONSOLE. """
import cmd


class HBNBCommand(cmd.Cmd):
    """ cmd module. """
    prompt = '(hbnb) '


    def do_destroy(self):
        return

    def do_quit(self, arg):
            return True

    def do_EOF(self, arg):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

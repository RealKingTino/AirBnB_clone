#!/usr/bin/env python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        return True

    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()


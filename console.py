#!/usr/bin/python3
"""
Console module for HBNB project
"""

import cmd
import models
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Handles EOF (Ctrl+D) to exit the program
        """
        print()  # Print a new line before exiting
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if not hasattr(models, class_name):
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if not hasattr(models, class_name):
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        if not arg:
            print([str(value) for value in models.storage.all().values()])
        else:
            class_name = arg.split()[0]
        if hasattr(models, class_name):
            print([str(value) for key, value in models.storage.all().items() if class_name in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in models.storage._FileStorage__objects:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = args[0] + "." + args[1]
                if key not in models.storage._FileStorage__objects:
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    instance = models.storage._FileStorage__objects[key]
                    setattr(instance, args[2], eval(args[3]))
                    models.storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

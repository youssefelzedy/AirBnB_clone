#!/usr/bin/python3
"""
Console module for HBNB project
"""

import cmd
import models
import shlex
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
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
            print([str(value) for key,
                   value in models.storage.all().items() if class_name in key])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and\
        id by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
        else:
            args = shlex.split(arg)
            args_size = len(args)
            if args_size == 0:
                print('** class name missing **')
            elif args[0] not in self.allowed_classes:
                print("** class doesn't exist **")
            elif args_size == 1:
                print('** instance id missing **')
            else:
                key = args[0] + '.' + args[1]
                inst_data = models.storage.all().get(key)
                if inst_data is None:
                    print('** no instance found **')
                elif args_size == 2:
                    print('** attribute name missing **')
                elif args_size == 3:
                    print('** value missing **')
                else:
                    args[3] = self.analyze_parameter_value(args[3])
                    setattr(inst_data, args[2], args[3])
                    setattr(inst_data, 'updated_at', datetime.now())
                    models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

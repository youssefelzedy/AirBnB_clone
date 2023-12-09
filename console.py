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

    def emptyline(self):
        """Do nothing if line is empty"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        else:
            try:
                new_instance = models.classes_dict[args[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
        print(new_instance().id)
        models.storage.save()

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        """
        args = shlex.split(arg)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + '.' + args[1] not in obj_dict:
            print("** no instance found **")
            return
        print(obj_dict[args[0] + '.' + args[1]])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """
        args = shlex.split(arg)
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if args[0] + '.' + args[1] not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[args[0] + '.' + args[1]]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        """
        args = shlex.split(arg)
        if len(args) != 0 and args[0] not in models.classes_dict:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in models.storage.all().values():
            if len(args) == 0:
                obj_list.append(obj.__str__())
            elif args[0] == obj.__class__.__name__:
                obj_list.append(obj.__str__())
        print(obj_list)

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

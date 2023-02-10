#!/usr/bin/env python3
"""entry to the program
"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """cmd class
    """
    prompt = "(hbnb) "
    class_dict = {"BaseModel":BaseModel}

    def do_create(self, line):
        """creates a class instance"""
        
        if not line:
            print("** class name missing **")
        else:
            if line not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                my_model = HBNBCommand.class_dict[line]()
                my_model.save()
                print(my_model.id)

    def do_show(self, line):
        """prints string repr of an instance
        """
        my_list = parse(line)
        if len(my_list) == 0:
            print("** class name missing **")
        elif len(my_list) == 1:
            if my_list[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(my_list) == 2:
            if my_list[0] not in HBNBCommand.class_dict:
                print("** class doesn't exist **")
            else:
                obj = storage.all()
                my_id = my_list[1]
                my_in = None
                for value in obj.values():
                    value = value.to_dict()
                    if value["id"] == my_id:
                        my_in = HBNBCommand.class_dict[my_list[0]](**value)
                if my_in is None:
                    print("** no instance found **")
                else:
                    print(my_in)

    def do_EOF(self, line):
        """Command to end the program
        """
        return True

    def do_quit(self, line):
        """command to end the program
        """
        return True

    def emptyline(self):
        pass

def parse(arg):
    return arg.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

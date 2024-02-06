#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command line interface"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt = '(hbnb) '
        self.classes = ["BaseModel", "User"]
        self.objects = storage.all()
        storage.reload()

    def emptyline(self):
        pass

    def do_EOF(self, line):
        if len(line) == 0:
            return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_quit(self, line):
        if len(line) == 0:
            return True

    def do_create(self, line):
        """Function to create a new instance of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            new_instance = BaseModel()
            print(new_instance.id)
            new_instance.save()

    def do_show(self, line):
        """Function to show an instance of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{} {}".format(args[0], args[1])
            if key in self.objects.keys():
                print(self.objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Function to destroy an instance of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            key = "{} {}".format(args[0], args[1])
            if key in self.objects:
                del self.objects[key]
                storage.save()  # Save after deleting the instance
            else:
                print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

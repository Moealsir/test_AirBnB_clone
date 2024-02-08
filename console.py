#!/usr/bin/python3
import json
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

    def help_EOF(self):
        print("Quit command to exit the program\n")

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
        """Prints the string representation of an instance"""
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
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                obj = storage.all()[key]
                print(obj)
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
            key = "{}.{}".format(args[0], args[1])
            if key in self.objects.keys():
                del self.objects[key]
                storage.__objects = self.objects
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        all_instances = []

        if not args:
            for obj_key, obj in storage.all().items():
                all_instances.append(str(obj))
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            class_name = args[0]
            for obj_key, obj in storage.all().items():
                if obj_key.split(".")[0] == class_name:
                    all_instances.append(str(obj))
        print(all_instances)

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        args = line.split()
        obj_dict = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(args) == 4:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = valtype(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = obj_dict["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

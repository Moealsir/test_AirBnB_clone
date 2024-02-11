#!/usr/bin/python3
"""Console, the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """Command line interface"""

    def __init__(self, *args, **kwargs):
        """initialize  variables and start the shell"""
        super().__init__(*args, **kwargs)
        self.prompt = "(hbnb) "
        self.all_classes = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review",
        ]
        self.classes = storage.class_dict()
        self.objects = storage.all()
        storage.reload()

    def emptyline(self):
        """empty input"""
        pass

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Function to create a new instance of a class"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Retrieve an instance based on its ID"""
        args = line.split()
        if len(args) == 2:
            class_name = args[0]
            instance_id = args[1]
            if class_name in self.all_classes:
                key = "{}.{}".format(class_name, instance_id)
                if key in storage.all():
                    obj = storage.all()[key]
                    print(obj)
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid command **")


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
        """Prints all string representation of all instances of a class"""
        args = line.split()
        if len(args) == 1:
            class_name = args[0]
            if class_name in self.all_classes:
                all_instances = [str(obj) for obj in storage.all().values() if isinstance(obj, eval(class_name))]
                print(all_instances)
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid command **")


    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        args = line.split()
        if len(args) == 1:
            class_name = args[0]
            if class_name in self.all_classes:
                count = sum(
                    1 for obj in storage.all().values() if isinstance(
                        obj, eval(class_name)))
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid command **")

    def parseline(self, line):
        """Parse the line to handle <class name>.all() and <class name>.count()"""
        orig_line = line
        line = line.strip()
        class_name = None
        command = None

        # Check if the line matches the pattern <class name>.all() or <class name>.count()
        match = re.match(r'^(\w+)\.(all|count)\(\)$', line)
        if match:
            class_name = match.group(1)
            command = match.group(2)
            return command, class_name, orig_line

        return cmd.Cmd.parseline(self, orig_line)

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
                if k in obj.__class__.__dict__.keys() and type(
                    obj.__class__.__dict__[k]
                ) in {str, int, float}:
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

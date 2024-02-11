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

    def default(self, line):
        """Handle unrecognized commands"""
        args = line.split('(')
        if len(args) != 2:
            print("** invalid command **")
            return

        cmd_args = args[1].split(')')[0]
        cmd_name = args[0].strip()

        if not cmd_args:
            print("** invalid command **")
            return

        class_name, action = cmd_name.split('.')

        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return

        instance_id = None
        update_dict = None

        if action == 'show':
            instance_id = cmd_args.strip().strip('"')
            self.do_show(f"{class_name} {instance_id}")

        elif action == 'destroy':
            instance_id = cmd_args.strip().strip('"')
            self.do_destroy(f"{class_name} {instance_id}")

        elif action == 'update':
            cmd_args = cmd_args.split(',', 1)
            if len(cmd_args) != 2:
                print("** invalid command **")
                return
            instance_id = cmd_args[0].strip().strip('"')
            update_dict = eval(cmd_args[1].strip())
            self.do_update(f"{class_name} {instance_id}", update_dict)

        else:
            print("** invalid command **")

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

    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        args = line.split()
        if len(args) == 1:
            class_name = args[0]
            if class_name in self.all_classes:
                count = sum(
                    1 for obj in storage.all().values()
                    if isinstance(obj, eval(class_name)))
                print(count)
            else:
                print("** class doesn't exist **")
        else:
            print("** invalid command **")

    def parseline(self, line):
        """Parse the line to handle <class name>.all()
        and <class name>.count()"""
        orig_line = line
        line = line.strip()
        class_name = None
        command = None

        match = re.match(r'^(\w+)\.(all|count)\(\)$', line)
        if match:
            class_name = match.group(1)
            command = match.group(2)
            return command, class_name, orig_line

        return cmd.Cmd.parseline(self, orig_line)

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

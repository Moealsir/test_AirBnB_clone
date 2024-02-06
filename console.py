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
        
    def do_all(self, line):
        """Prints all string representation of all instances"""
        args = line.split()
        if not args:
            # Print all instances of all classes
            for obj_key, obj in self.objects.items():
                print(obj)
        elif args[0] not in self.classes:
            # Print error message if class name doesn't exist
            print("** class doesn't exist **")
        else:
            # Print instances of the specified class
            class_name = args[0]
            instances = [str(obj) for obj_key, obj in self.objects.items() if obj_key.startswith(class_name)]
            print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        elif len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = " ".join(args[3:])

        key = "{} {}".format(class_name, instance_id)
        if key not in self.objects:
            print("** no instance found **")
            return

        instance = self.objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()

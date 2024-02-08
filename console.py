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
        elif len(args) < 1:
            print(args)
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
            if key in self.test:
                # del  self.test[key]
                # storage.__objects = self.test
                # storage.save()
                
                print('** destryed')
            else:
                print("** no such object exists **")

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
        attribute_value = args[3]

        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.get(key)
        setattr(obj, attribute_name, attribute_value)
        storage.save(obj)
            

    
if __name__ == "__main__":
    HBNBCommand().cmdloop()

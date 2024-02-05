import cmd
class  command(cmd.Cmd):
    # intro = "Welcome to the Command Line Interface.\nType help or ? to list commands."
    FRIENDS = [ 'Alice', 'Adam', 'Barbara', 'Bob' ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prompt = '> '
    
    def emptyline(self):
        print("")
    
    def do_great(self, line):
        if person:
            print ("hi,", person)
        else:
            print ('hi')
    
    def help_great(self):
        print ('\n'.join(['great [person]', 'great the named person']))
    
    def do_EOF(self, line):
        return True
    
    
    def can_exit(self):
        return True

    def onecmd(self, line):
        r = super().onecmd(line)
        if r and (self.can_exit() or
        input('exit anyway? (yes/no):') == 'yes'):
            return True
        return False

    def do_exit(self, s):
        return True
    def help_exit(self):
        print ("Exit the interpreter.")
        print ("You can also use the Ctrl-D shortcut.")
    do_EOF = do_exit
    help_EOF= help_exit
    
    def preloop(self):
        print ('Hello')
        super().preloop()
    def postloop(self):
        print ('Goodbye')
        super().postloop()

if  __name__ == "__main__":
    person = "Moe"
    command().cmdloop()
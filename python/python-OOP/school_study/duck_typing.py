#Examples of Duck Typing

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class VSCode:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute() #doesnt matter what class the ide is coming from, as long as it possess a execute method then thats all we need


ide1 = PyCharm()
ide2 = VSCode()
myLap = Laptop()

for ide in (ide1,ide2):
    myLap.code(ide)
    print("-"*50)
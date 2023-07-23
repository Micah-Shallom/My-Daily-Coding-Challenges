#Implementing a stack with a list


class Stack:
    def __init__(self) -> None:
        self.list = []

    def __str__(self) -> str:
        values = self.list.reverse
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #isEmpty
    
class MyArray:
    def __init__(self):
        self.data = []

    # Append an element to the end of the array.
    def append(self, item):
        self.data.append(item)

    # Access an element at a specific index.
    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        else:
            return None

    # Update an element at a specific index.
    def set(self, index, value):
        if 0 <= index < len(self.data):
            self.data[index] = value

    # Insert an element at a specific index.
    def insert(self, index, value):
        if 0 <= index <= len(self.data):
            self.data.insert(index, value)

    # Remove the first occurrence of an element from the array.
    def remove(self, value):
        if value in self.data:
            self.data.remove(value)

    # Delete an element at a specific index.
    def delete(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]

    # Get the length (number of elements) of the array.
    def length(self):
        return len(self.data)

    # Print the elements of the array.
    def display(self):
        print(self.data)

# Example usage:
my_array = MyArray()

# Append elements to the array.
my_array.append(10)
my_array.append(20)
my_array.append(30)
my_array.display()  # Output: [10, 20, 30]

# Access and update elements.
print(my_array.get(1))  # Output: 20
my_array.set(1, 25)
my_array.display()  # Output: [10, 25, 30]

# Insert and remove elements.
my_array.insert(1, 15)
my_array.display()  # Output: [10, 15, 25, 30]
my_array.remove(15)
my_array.display()  # Output: [10, 25, 30]

# Delete an element by index.
my_array.delete(1)
my_array.display()  # Output: [10, 30]

# Get the length of the array.
print(my_array.length())  # Output: 2

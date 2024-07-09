class Book:
    def __init__(self,id,name,quantity, borrowed = 0):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.borrowed = borrowed


    def __str__(self):
        return f'Book name: {self.name}\t\t-id: {self.id} - total quantity: {self.quantity} - total borrowed: {self.borrowed}'


    def __repr__(self):
        return f'Book({self.id}, {self.name}, {self.quantity}, {self.borrowed})'





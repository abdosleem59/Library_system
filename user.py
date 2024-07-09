class User:
    def __init__(self, id, name): 
        self.id = id
        self.name = name


    def __str__(self):
        return f'User name: {self.name}\t\t- id: {self.id}'
    

    def __repr__(self):
        return f'User({self.id}, {self.name})'
    


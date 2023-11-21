from random import choice

# Create a class of the drunk 
class Drunk:
    # Define a name to the drunk
    def __init__(self, name):
        """
        Create an drunken object with the name 
        """
        self.name = name

# Inherit from the parent class Drunk
class TraditionalDrunk(Drunk):
    def __init__(self, name):
        super().__init__(name) # Get the name of the drunk from the parent class
        
    def walk(self): # Simulate walking with a random choice
        """
        Simulate drunk walking with a random choice in a tuple
        """
        return choice([(0,1), (0,-1), (1,0), (-1,0)])
    
    
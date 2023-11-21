class Field:
    def __init__(self):
        """
        Create a new object Field
        """
        self.coordenate_of_drunk = {} # Create a empty dictionary 
        
    def add_drunk(self, drunk, coordenate): # Add the coordenates of the drunks
        """
        Add the name of the drunk like a key and the coordenate of the drunk as the value
        """
        self.coordenate_of_drunk[drunk] = coordenate
        
    def move_drunk(self, drunk): 
        """
        Move the position of the drunks
        """
        delta_x, delta_y = drunk.walk() # Get the aleatory moves for the drunk
        actual_coordenate = self.coordenate_of_drunk[drunk] # Get the actual coordinates of the drunk
        new_coordenate = actual_coordenate.move(delta_x, delta_y) # Get the new coordinates of the drunk
        
        self.coordenate_of_drunk[drunk] = new_coordenate # Update the coordinates of the drunk in the dictionary
        
    def get_coordenate(self, drunk):
        """"
        Give the coordinates of the drunk in the dictionary
        """
        return self.coordenate_of_drunk[drunk]
class Coordinates:
    def __init__(self, x, y): # Obtain the coordinates
        """
        Initialize an object coordenate with the given coordinates
        """
        self.x = x
        self.y = y
        
    def move(self, delta_x, delta_y): # Simulare the move operation
        """
        Simulate the move operation with the given delta_x and delta_y coordinates
        """
        return Coordinates(self.x + delta_x, self.y + delta_y)
    
    def calculate_distance(self, other_coordinate):
        """
        Calculates the distance between the two coordinates given
        """
        
        delta_x = self.x - other_coordinate.x # Distance X
        delta_y = self.y - other_coordinate.y # Distance Y
        
        return (delta_x**2 + delta_y**2)**0.5 # Pitagoras method to calculate distance
    
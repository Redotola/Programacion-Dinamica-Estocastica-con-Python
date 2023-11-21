from drunk import TraditionalDrunk
from field import Field
from coordinates import Coordinates
from bokeh.plotting import figure, show

def walking(field, drunk, steps):
    start = field.get_coordenate(drunk)
    
    for _ in range(steps):
        field.move_drunk(drunk)
        
    return start.calculate_distance(field.get_coordenate(drunk))

def simulate_walking(steps, number_of_try, type_of_drunk):
    drunk = type_of_drunk(name = 'David')
    origin = Coordinates(0,0)
    distances = []
    
    for _ in range(number_of_try):
        field = Field()
        field.add_drunk(drunk, origin)
        walking_simulation = walking(field, drunk, steps)
        distances.append(round(walking_simulation, 1))
    
    return distances

def draw_simulation(x, y):
    """
    Draw a simulation of every final step of the simulation with a given coordinates
    """
    graph = figure(title='Aleatory path', x_axis_label='steps', y_axis_label='distance')
    graph.line(x, y)
    
    show(graph)

def main(walking_distances, number_of_try, type_of_drunk):
    average_distance_per_walk = [] # We save the average distance of every iteration
    
    for steps in walking_distances:
        distances = simulate_walking(steps, number_of_try, type_of_drunk)
        avg_distance = round(sum(distances)/ len(distances), 4)
        max_distance = max(distances)
        min_distance = min(distances)
        average_distance_per_walk.append(avg_distance)
        
        print(f'{type_of_drunk.__name__} aleatory walk of {steps} steps')
        print(f'Average distance = {avg_distance}')
        print(f'Min distance = {min_distance}')
        print(f'Max distance = {max_distance}')
    draw_simulation(walking_distances, average_distance_per_walk)
    
if __name__ == '__main__':
    walking_distances = [10,100,1000,10000]
    number_of_try = 100
    
    main(walking_distances, number_of_try, TraditionalDrunk)
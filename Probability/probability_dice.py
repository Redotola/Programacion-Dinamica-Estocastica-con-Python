import random

def roll_the_dice(number_of_throw: int) -> list[int]:
    """
    With a given number of throws it store every random result from the faces of a dice and return a list with the results
    """
    secuence_of_throws = []
    
    for _ in range(number_of_throw):
        throw = random.choice([1, 2, 3, 4, 5, 6])
        secuence_of_throws.append(throw)
    return secuence_of_throws
    
def main(number_of_throw:int, number_of_tries:int):
    """
    It simulates the throws of a dice with the number of throws and number of tries
    """
    throws = []
    
    for _ in range(number_of_tries):
        secuence_of_throws = roll_the_dice(number_of_throw)
        throws.append(secuence_of_throws)
    throw_with_1 = 0
    for throw in throws:
        if 1 in throw: # "not in" in case to obtain the negative probability
            throw_with_1 += 1
            
    probability_throw_with_1 = throw_with_1 / number_of_tries
    print(f'Probability of obtain at least 1 in {number_of_tries} throws {number_of_throw} = {probability_throw_with_1}')
    
    
if __name__ == '__main__':
    number_of_throw = int(input('How many times will you roll the dice: '))
    number_of_tries = int(input('How many times will run the simulation: '))
    
    main(number_of_throw, number_of_tries)
    
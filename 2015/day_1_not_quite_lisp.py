from typing import Optional, Dict
import argparse

def find_number_of_floors(arr: str) -> Dict[str, Optional[int]]:
    """
    Calculate the net floor Santa ends up on based on instructions.

    Args:
        arr (str): A string consisting of '(' and ')' indicating up and down movements.
    
    Return:
        Dict[str, Optional[int]]: A dictionary with:
            - 'first_basement_position' (Optional[int]): The position of the character that 
              causes Santa to first enter the basement (or None if he never enters).
            - 'net_floor' (int): The net floor Santa ends up on.
    Raises:
        ValueError: If the input contains characters other than '(' or ')'.
    """
    floor: int = 0
    position: Optional[int] = None
    position = None
    for index, char in enumerate(arr, start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            raise ValueError(f"Invalid character '{char}' in input. Only '(' and ')' are allowed.")
        if floor == -1 and position is None: # Ensure we capture the first occurrence only
            position = index
    return {
        'first_basement_position': position,
        'net_floor': floor
    }

if __name__ == '__main__':
    # Setting up the argument parser
    parser = argparse.ArgumentParser(description="Determine the final floor Santa ends up on based on instructions.")
    parser.add_argument("instructions", type=str, help="A list of string tat contain '(' and ')' representing instructions.")

    # Parsing the arguments
    args = parser.parse_args()
    
    try:
        result = find_number_of_floors(args.instructions)
        print(f"Instructions floor to take by Santa: {result['net_floor']}")
        print(f"The position of the character that causes Santa to first enter the basement: {result['first_basement_position']}")
    except ValueError as e:
        print(e)

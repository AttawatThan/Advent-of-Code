from typing import List, Tuple, Dict

def find_min_value(numbers: List[int]) -> int:
    """
    Finds the minimum value in a list of numbers

    Args:
        numbers (List[int]): A list of numbers (integers).

    Returns:
        int: The smallest number in the list.
    
    Raises:
        ValueError: If the list is empty
        TypeError: If the input is not a list of numbers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not numbers:
        raise ValueError("Can't find the minimum of an empty list.")
    if not all(isinstance(x, int) for x in numbers):
        raise TypeError("List must contain only integer")
    
    min_value = numbers[0]
    for number in numbers[1:]:
        if number < min_value:
            min_value = number
    return min_value

def prepare_str_to_list_of_lwh(string_message: str) -> List[str]:
    """
    Converts a multi-line string into a list of stripped lines.

    Args:
        string_message (str): A multi-line string input.

    Returns:
        List[str]: A list of stripped strings, one per line.

    """
    string_message_list = string_message.strip().split('\n')
    lwh_list = [line.strip() for line in string_message_list]
    return lwh_list

def mapping_str_to_list_of_dict_of_lwh(lwh_list: list) -> List[Dict[str, str]]:
    dict_list: list = []
    for lwh in lwh_list:
        lwh_tmp: list = lwh.split('x')
        dict_list.append({
            'l': int(lwh_tmp[0]),
            'w': int(lwh_tmp[1]),
            'h': int(lwh_tmp[2])
        })
    return dict_list        

def calculate_surface_area(lwh_dict: dict) -> int:
    total_area: int = 0
    for lwh in lwh_dict:
        total_area += 2*(lwh['l']*lwh['w'] + lwh['w']*lwh['h'] + lwh['l']*lwh['h']) + calculate_little_extra_paper(lwh)
    return total_area

def calculate_little_extra_paper(lwh_dict: dict) -> int:
    return min(lwh_dict['l']*lwh_dict['w'], lwh_dict['w']*lwh_dict['h'], lwh_dict['l']*lwh_dict['h'])

if __name__ == '__main__':
    string_message = """
    1x1x10
    1x9x10
    1x1x15
    """
    a = prepare_str_to_list_of_lwh(string_message)
    print(a)
    # b = mapping_str_to_list_of_dict_of_lwh(a)
    # c = calculate_surface_area(b)
    # print(c)
    # number = [8, 9, 32, 19, -1, 0, -9, 1,]
    # print(find_min_value(number))

from typing import Tuple, Dict, List

def prepare_str_to_list_of_lwh(string_message: str) -> List[Tuple[str]]:
    string_message_list = string_message.strip().split('\n')
    lwh_list = [_.strip() for _ in string_message_list]
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
    """
    a = prepare_str_to_list_of_lwh(string_message)
    b = mapping_str_to_list_of_dict_of_lwh(a)
    c = calculate_surface_area(b)
    print(c)

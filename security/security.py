'''The module'''
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].\
strip()) for line in file if len(line.split(',')) == 2}
def rescue_people(smarties, limit_iq):
    '''
    (dict,int)->tuple
    The function returns a tuple of the number of required trips and a list of lists,
    where each inner list represents a trip and contains the names of the people 
    transported on that trip in the order in which they were chosen by the aliens.
    >>> rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']])
    '''
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    if not smarties:
        return 0, []
    smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))
    lst2 = []
    while smarties:
        lst1 = []
        remaining_iq = limit_iq
        for key, value in smarties.items():
            if value <= remaining_iq:
                lst1.append(key)
                remaining_iq -= value
        lst2.append(lst1)
        smarties = {key: value for key, value in smarties.items() if key not in lst1}
    count = len(lst2)
    return count, lst2

basic_x = 0
basic_y = 0
diff = 15


# |1|2|3|
# |4|5|6|
# |7|8|9|
def process_ang(data):
    output = 5
    real_x = data['AngX'] - basic_x
    real_y = data['AngY'] - basic_y
    if real_x <= -diff and real_y >= diff:
        output = 1
    elif real_x >= diff and real_y >= diff:
        output = 3
    elif real_x <= -diff and real_y <= -diff:
        output = 7
    elif real_x >= diff and real_y <= -diff:
        output = 9
    elif real_y >= diff:
        output = 2
    elif real_y <= -diff:
        output = 8
    elif real_x <= -diff:
        output = 4
    elif real_x >= diff:
        output = 6
    else:
        output = 5
    return output



# if __name__ == '__main__':
#     print(process_ang({'AngX': 0, 'AngY': 0, 'AngZ': 0}))
#     print(process_ang({'AngX': 20.0, 'AngY': 0, 'AngZ': 0}))
#     print(process_ang({'AngX': 0, 'AngY': 20.0, 'AngZ': 0}))
#     print(process_ang({'AngX': -20.0, 'AngY': 0, 'AngZ': 0}))
#     print(process_ang({'AngX': 0, 'AngY': -20.0, 'AngZ': 0}))
#     print(process_ang({'AngX': 20, 'AngY': -20.0, 'AngZ': 0}))
#     print(process_ang({'AngX': -20.3, 'AngY': 20.4, 'AngZ': 0}))
#     print(process_ang({'AngX': 20.0, 'AngY': 20.0, 'AngZ': 0}))
#     print(process_ang({'AngX': -20.0, 'AngY': -20.0, 'AngZ': 0}))

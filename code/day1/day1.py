f = open("day1_input.txt", "r")

total_sum = 0
total_sum_pt2 = 0
test_val = '1'
digit_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
              '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}


def try_int(val: str) -> bool:
    if not val:
        return False
    try:
        int(val)
        return True
    except ValueError:
        return False

def detect_digit(input_str: str) -> int:
    min_ind = len(input_str)
    max_ind = 0

    first_val = ''
    last_val = ''
    final_val = ''
    for key, value in digit_dict.items():
        first_current_ind = input_str.find(str(key))
        last_current_ind = input_str.rfind(str(key))
        if first_current_ind >= 0 or last_current_ind >= 0:
            if first_current_ind < min_ind:
                min_ind = first_current_ind
                first_val = value

            if last_current_ind >= max_ind:
                max_ind = last_current_ind
                last_val = value

    final_val = first_val + last_val
    return final_val


for item in f:
    row_val = int(detect_digit(item.lower()))
    print(row_val)
    total_sum_pt2 += int(detect_digit(item.lower()))
    

# for item in f:
#     item = item.lower()
#     current_val = ''
#     print(len(item))
#     for ind in range(0, len(item), 1):
#         if try_int(item[ind]):
#             current_val += item[ind]
#             break
        
#     for ind in range(len(item) -1, -1, -1):
#         if try_int(item[ind]):
#             current_val += item[ind]
#             break
    
#     total_sum += int(current_val)

print(total_sum_pt2)



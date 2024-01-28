msg="send cheese"
tups_msg=tuple(msg)
print(tuple(tups_msg))
str_msg='xy'.join(str(item) for item in tups_msg)
print(str_msg)
decr=list(tuple(str_msg))
print(decr)
filtered_list = [item for item in decr if item not in ('x', 'y')]

print(filtered_list)
decrt=''.join(str(item) for item in tups_msg)
print(decrt)

original_list = ['s', 'x', 'y', 'e', 'x', 'y', 'x', 'x', 'y', 'y', 'x', 'y', ' ', 'x', 'y', 'c', 'x', 'y', 'h', 'x', 'y', 'e', 'x', 'y', 'e', 'x', 'y', 's', 'x', 'y', 'e']

filtered_list = []
i = 0
while i < len(original_list):
    if i + 3 <= len(original_list) and original_list[i:i+4] == ['s', 'e', 'x', 'y']:
        # Preserve 'sexy'
        filtered_list.extend(original_list[i:i+4])
        i += 4
    elif i + 5 <= len(original_list) and original_list[i:i+6] == ['c', 'h', 'e', 'e', 's', 'e']:
        # Preserve 'cheese'
        filtered_list.extend(original_list[i:i+6])
        i += 6
    else:
        # Remove standalone 'x' and 'y'
        if original_list[i] not in ['x', 'y']:
            filtered_list.append(original_list[i])
        elif i > 0 and filtered_list[-1] != ' ':
            # Preserve space between words
            filtered_list.append(original_list[i])
        i += 1

output_string = ''.join(filtered_list)
print(output_string)


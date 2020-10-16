import re

with open('fileTask6.txt', 'r', encoding='utf-8') as f:
    text_list = f.readlines()

my_dict = dict()

for line in text_list:
    key = line.split(':')[0]
    item = re.findall(r'\d+', line)
    item = sum(list(map(int, item)))
    my_dict[key] = item

print(my_dict)

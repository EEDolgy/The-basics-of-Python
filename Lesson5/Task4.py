my_dict = {'One':'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'}

with open('fileTask4.txt', 'r', encoding='utf-8') as f:
    text_list = f.readlines()

with open('fileTask4prog.txt', 'w', encoding='utf-8') as f:
    for st in text_list:
        line = st.split()
        line[0] = my_dict[line[0]]
        line = ' '.join(line)
        f.write(line + '\n')


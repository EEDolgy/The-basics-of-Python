with open('fileTask2.txt', 'r', encoding='utf-8') as f:
    text_list = f.readlines()
    print(f'Number of lines: {len(text_list)}')
    for i, st in enumerate(text_list, 1):
        print(f'Number of words in {i} line: {len(st.split())}')

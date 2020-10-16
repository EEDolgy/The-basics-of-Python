with open('fileTask3.txt', 'r', encoding='utf-8') as f:
    text_list = f.readlines()

pers_count = len(text_list)
sum = 0

for item in text_list:
    salary = int(item.strip().split()[1])
    person = item.strip().split()[0]
    if salary < 20:
        print(person)
    sum += salary
print(f'Average sallary is {int(sum/pers_count)}')
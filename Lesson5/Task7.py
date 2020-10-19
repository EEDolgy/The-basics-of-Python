import json

my_list = [{}, {}]
avg_prof = 0

with open('fileTask7.txt', 'r+') as f:
    content = f.readlines()

    comp_count = len(content)
    for item in content:
            item = item.split()
            prof = int(item[2]) - int(item[3])
            my_list[0][item[0]] = prof
            avg_prof += prof

    my_list[1]['average_profit'] = avg_prof/comp_count

    f.write('\n')
    json.dump(my_list, f)



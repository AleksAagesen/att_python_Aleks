def get_score(my_dict):
    for sub_dict in my_dict.values():
        points =0
        for subkey in sub_dict:
            if subkey == 'calls':
                points += 10*sub_dict[subkey]
                if sub_dict[subkey]>150:
                    points+=100
            elif subkey == 'meetings':
                points += 30*sub_dict[subkey]
                if sub_dict[subkey]>20:
                    points+=100
            elif subkey == 'sales':
                points += 100*sub_dict[subkey]
                if sub_dict[subkey]>5:
                    points+=100
        sub_dict['points'] = points
    return my_dict

all_employees = {
    'jordan_belfort':{
        'calls': 178,
        'meetings':17,
        'sales':6
    },
    'warren_buffett':{
        'calls': 137,
        'meetings':28,
        'sales':4
    },
    'peter_lynch':{
        'calls': 128,
        'meetings':14,
        'sales':3
    }
}


x = get_score(all_employees)
print(x)
for keyval in x.items():
    print(keyval)


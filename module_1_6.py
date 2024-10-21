my_dict = {'Evgen': 1994, 'Nastya;': 1995}
print("Dict:", my_dict)
existing_key = "Evgen"
print("Existing value:", my_dict.get(existing_key))
not_existing_key = "Alisa"
print("Not existing value:", my_dict.get(not_existing_key))
my_dict.update({'Sasha': 1996 ,
                'Arina': 2024})
deleted_key = 'Sasha'
Deleted_value = my_dict.pop(deleted_key, None)
print("Deleted value:", Deleted_value)
print("Modified dictionary:", my_dict)



my_set = {5,'груша', 77.628, 5, 'груша'}
print('set:', my_set)
my_set.add(99)
my_set.add((6,7,12.800))
my_set.remove(77.628)
print('Modified set:', my_set)
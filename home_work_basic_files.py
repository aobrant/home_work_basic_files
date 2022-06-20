from itertools import count
from pprint import pprint
import readline
file_name = 'reciept.txt'


def catalog_reader(filename:str) -> dict:
    result  = {}
    with open(file_name) as file_obj:
        for line in file_obj:
             dish = line.strip()
             list = []
             quantit = file_obj.readline()
             for item in range(int(quantit)):
                next_str = file_obj.readline()
                n_str = next_str.split("|")
                ingredient_name = n_str[0].strip()
                quantity = n_str[1].strip()
                measure = n_str[2].strip()
                ingr = {}
                ingr['ingredient_name'] = ingredient_name
                ingr["quantity"] = quantity
                ingr["measure"] = measure
                list.append(ingr)
             result[dish] = list
             file_obj.readline()
    return result


def get_shop_list_by_dishes(dishes, person_count) ->dict:
    result = {}
    for dish in dishes :
        book_dish = catalog[dish]
        for ingr in book_dish:
            if ingr['ingredient_name'] in result:
                #  res['quantity'] = ingr['quantity']*person_count+result['ingredient_name']['quantity']
                 res['quantity'] = int(ingr['quantity'])*person_count+int(result['ingredient_name']['quantity'])
                 result[ingr['ingredient_name']] = res
            else:
                res = {}
                res['quantity'] = int(ingr['quantity'])*person_count
                res['measure'] = ingr['measure']
                result[ingr['ingredient_name']] = res
    return result


def make_sorted_tuple(lst:list) -> tuple:
    dic = {}
    for file_name in lst:
        with open(file_name) as file_obj:
            number = sum(1 for line in file_obj)
            dic[file_name] = number
    result = sorted(dic.items(), key = lambda x:x[1])
    return result


def print_in_file_head(file_name,count):
    with open('data.txt', 'a') as file_wt:
        file_wt.write(f'{file_name} \n {count} \n')
    return


def print_in_file(tuple_sorted): 
    for i in tuple_sorted:
         file_name = i[0]
         count = i[1]
         with open('data.txt', 'a') as file_wt:
             file_wt.write(f'{file_name} \n {count} \n')
             with open(file_name) as file_rd:
                 for line in file_rd:
                     prt = line
                     file_wt.write(prt)
    return


           
catalog = catalog_reader(file_name)
pprint (catalog)
get = get_shop_list_by_dishes(['Запеченный картофель','Омлет'], 2)
pprint(get)

#         3я задача

lst = []
lst = ['1.txt','2.txt','3.txt']
tpl_sworted = make_sorted_tuple(lst)

with open('data.txt', 'w') as file_wt:
    file_wt.write('')
print_in_file(tpl_sworted)




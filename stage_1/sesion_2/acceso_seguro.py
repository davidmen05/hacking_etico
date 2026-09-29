def get_item(lst, index):
    if index < 0 or index >= len(lst):
        return None
    return lst[index]


frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]

print(get_item(frutas, 0))
print(get_item(frutas, 2))
print(get_item(frutas, 10))
print(get_item(frutas, -1))
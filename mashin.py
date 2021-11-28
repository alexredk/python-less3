mashin = []
mashin.append("bmv")
mashin.append("leksus")
mashin.append("suzuki")
mashin.append("subaru")
print(mashin)
massage = f"my mashin is {mashin[0].title()}"
print(massage)
mashin.insert(1, "ducati")
print(mashin)
del mashin[3]
print(mashin)
del_item = mashin.pop(2)
print(mashin)
print(del_item)
print(f"Удален, но сохранен елемент списка {del_item.title()}")

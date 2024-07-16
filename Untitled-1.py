""" x = "kosi"

result = list(x)

print(result) """ 



""" items = ["food", "water", "air", "coal"]

print(items[0]) 
print("-" * 4)
print(items[3])  """


fruits = ["apples", "bananas", "mangoes", "cherry"]
print("Fruits: ", fruits)

fruits.append("grapes")
print("Updated List: ", fruits)

fruits.insert(3, "guava")
print("Updated again:", fruits)

vegetables = ["cabbage", "lettuce", "broccoli"]
fruits.extend(vegetables)
print("Fruits and vegetables: ", fruits)

fruits[1] = "melon"
print("Melon update: ", fruits)

fruits.remove("melon")
print("melon removed:", fruits)

for fruit in fruits:
    print(fruits)
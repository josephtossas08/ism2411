# 1. The most surprising thing about Python lists is that you can store multiple types of information in the same list and easily add, remove, or change items. I originally thought lists would be more complicated to manage, but they make organizing information much easier.

# 2. At a retail job, I could have used a Python list to keep track of inventory, such as clothing sizes, colors, and quantities. Instead of manually entering and updating every item in Excel, I could have used Python to quickly organize the inventory and find which products needed to be restocked.




# Excercise 1: Build a list  

print("-- Exercise 1: Build a list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#Excercise 2: Index Practice

print("-- Exercise 2: Index Practice ---")
print(inventory[0])  #always grabs the first item
print(inventory[-1]) #always grabs the last item

middle = len(inventory) // 2
print(inventory[middle])


print("-- Exercise 3: List slicing ---")
print(inventory[:3])  #grabs the first three items
print(inventory[-2:]) #grabs the last two items 
print(inventory[::2]) #grabs every other item


print("-- Exercise 4: List methods ---")

inventory.append("envelope") #adds an item to the end of the list
print(inventory)

inventory.remove("tape") #removes an item from the list
print(inventory)
inventory.sort()
print(inventory) #sorts the list in alphabetical order

print("-- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060) #New York City coordinates

# coords [0] = 99
try:
    coords[0] = 99
except TypeError as e:
    print(f"TypeError caught: {e}")
    print("Tuples coordinates are immutable")

print ("--- Excercise 6: List Average Sales ---  ")

sales = [100, 250, 75, 480, 200]
total =sum(sales)
count = len(sales)
average = total / count
print(f"Total Sales: ${total}")
print(f"Number of Sales: {count}")
print(f"Average Sale: ${average:.2f}")      
print(f"Best Sale: ${max(sales)}")
print(f"Worst Sale: ${min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

        print(f"Best sale (loop): ${best}")
        print(f"Worst sale (loop): ${worst}")

        print("-- Exercise 7: Accumulator Pattern ---")

        prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

    print(prices)
    print(discounted)


    print("--- Excercise 8: Filter ----")
    sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

    high_sales = []

    for amount in sales:
        if amount > 300:
            high_sales.append(amount)

            print(high_sales)
            print(f"Count: {len(high_sales)}")
            print (f"Average: ${sum(high_sales)/len(high_sales):.2f}")


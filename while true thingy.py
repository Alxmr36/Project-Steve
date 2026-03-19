
item_types = ['Hardware', 'Lumber', 'Paint']
selected_items = []

while True:
    # Print available item types
    print("\nAvailable item types:")  
    for i, item_type in enumerate(item_types, start=1):
        print(f"{i}. {item_type}")

    print(f"{len(item_types) + 1}. Quit")

    # Ask the user for the index of the item type to select
    selected_index = int(input("Please enter the index of the item type you want to select: "))

    # Check if the selected index is for quitting
    if selected_index == len(item_types) + 1:
        print("Quitting...")
        break

    # Check if the selected index is valid
    if 1 <= selected_index <= len(item_types):
        # Get the selected item type
        selected_item_type = item_types[selected_index - 1]
        selected_items.append(selected_item_type)
        print(f"\nYou selected: {selected_item_type}")
    else:
        print("Invalid index. Please try again.")       

print("Paint count is", selected_items.count("Paint"))
print("Hardware count is", selected_items.count("Hardware"))
print("Lumber count is", selected_items.count("Lumber"))


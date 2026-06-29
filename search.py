def search_element(data, element):
    for i, item in enumerate(data):
        if item == element:
            return i  # Returns the index if found
    return 'nf'  # Returns -1 if not found

my_list = [10, 20, 30, 40, 50]
index = search_element(my_list, 30)

if index != nf:
    print(f"Element found at index: {index}")
else:
    print("Element not found")

index = search_element(my_list, 60)
if index != nf:
    print(f"Element found at index: {index}")
else:
    print("Element not found")

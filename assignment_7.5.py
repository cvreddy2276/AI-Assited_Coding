# Fixed: Using items=None as default to avoid mutable default argument issue
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item(1))
print(add_item(2))

def check_sum():
    # Use a tolerance when comparing floating-point sums
    return abs((0.1 + 0.2) - 0.3) < 1e-9
print(check_sum())

 
def get_value():
    data = {"a": 1, "b": 2}
    return data.get("c", None)
print(get_value())

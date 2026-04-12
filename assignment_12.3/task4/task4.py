from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Product:
    product_id: str
    name: str
    price: float
    stock_quantity: int


class Inventory:
    """Inventory system with fast search and stable sorting."""

    def __init__(self, products: List[Product]):
        self.products = products
        self.id_index: Dict[str, Product] = {}
        self.name_index: Dict[str, List[Product]] = {}
        self._build_indices()

    def _build_indices(self) -> None:
        """Build lookup dictionaries for fast product search."""
        for product in self.products:
            self.id_index[product.product_id] = product
            key = product.name.lower()
            self.name_index.setdefault(key, []).append(product)

    def search_by_id(self, product_id: str) -> Optional[Product]:
        """Search a product by its ID in O(1) average time."""
        return self.id_index.get(product_id)

    def search_by_name(self, name: str) -> List[Product]:
        """Search products by name in O(1) average time for exact name lookup."""
        return self.name_index.get(name.lower(), [])

    def sort_by_price(self, descending: bool = False) -> List[Product]:
        """Sort products by price using merge sort for stable O(n log n) performance."""
        return merge_sort(self.products, key=lambda p: p.price, descending=descending)

    def sort_by_quantity(self, descending: bool = False) -> List[Product]:
        """Sort products by quantity using merge sort for stable O(n log n) performance."""
        return merge_sort(self.products, key=lambda p: p.stock_quantity, descending=descending)


def merge_sort(items: List[Product], key, descending: bool = False) -> List[Product]:
    """Stable merge sort implementation for sorting product lists."""
    if len(items) <= 1:
        return items[:]

    mid = len(items) // 2
    left = merge_sort(items[:mid], key, descending=descending)
    right = merge_sort(items[mid:], key, descending=descending)
    return merge(left, right, key, descending=descending)


def merge(left: List[Product], right: List[Product], key, descending: bool) -> List[Product]:
    merged: List[Product] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if descending:
            condition = key(left[i]) >= key(right[j])
        else:
            condition = key(left[i]) <= key(right[j])

        if condition:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


if __name__ == "__main__":
    sample_products = [
        Product(product_id="P1001", name="Widget", price=9.99, stock_quantity=120),
        Product(product_id="P1002", name="Gadget", price=14.99, stock_quantity=80),
        Product(product_id="P1003", name="Widget", price=9.99, stock_quantity=50),
        Product(product_id="P1004", name="Thingamajig", price=24.99, stock_quantity=200),
        Product(product_id="P1005", name="Doodad", price=4.99, stock_quantity=30),
    ]

    inventory = Inventory(sample_products)

    print("Search by ID P1002:")
    product = inventory.search_by_id("P1002")
    print(product)

    print("\nSearch by name 'widget':")
    for match in inventory.search_by_name("widget"):
        print(match)

    print("\nProducts sorted by price ascending:")
    for item in inventory.sort_by_price():
        print(item)

    print("\nProducts sorted by stock quantity descending:")
    for item in inventory.sort_by_quantity(descending=True):
        print(item)

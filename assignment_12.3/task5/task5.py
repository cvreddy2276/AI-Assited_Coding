import random
import string
import time
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Stock:
    symbol: str
    opening_price: float
    closing_price: float

    @property
    def percentage_change(self) -> float:
        """Compute percentage gain/loss from opening to closing price."""
        if self.opening_price == 0:
            return 0.0
        return ((self.closing_price - self.opening_price) / self.opening_price) * 100


def generate_stock_data(count: int) -> List[Stock]:
    """Generate simulated stock data for analysis."""
    symbols = set()
    stocks: List[Stock] = []
    while len(stocks) < count:
        symbol = ''.join(random.choices(string.ascii_uppercase, k=3))
        if symbol in symbols:
            continue
        symbols.add(symbol)
        opening_price = round(random.uniform(10.0, 500.0), 2)
        change = random.uniform(-0.2, 0.2)
        closing_price = round(opening_price * (1 + change), 2)
        stocks.append(Stock(symbol=symbol, opening_price=opening_price, closing_price=closing_price))
    return stocks


def build_symbol_index(stocks: List[Stock]) -> Dict[str, Stock]:
    """Create a hash-map for instant symbol lookup."""
    return {stock.symbol: stock for stock in stocks}


def heapify(stocks: List[Stock], heap_size: int, root_index: int) -> None:
    """Ensure the subtree rooted at root_index satisfies the max-heap property."""
    largest = root_index
    left = 2 * root_index + 1
    right = 2 * root_index + 2

    if left < heap_size and stocks[left].percentage_change > stocks[largest].percentage_change:
        largest = left
    if right < heap_size and stocks[right].percentage_change > stocks[largest].percentage_change:
        largest = right
    if largest != root_index:
        stocks[root_index], stocks[largest] = stocks[largest], stocks[root_index]
        heapify(stocks, heap_size, largest)


def heap_sort(stocks: List[Stock], descending: bool = True) -> List[Stock]:
    """Sort stocks by percentage change using heap sort."""
    data = stocks.copy()
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)

    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heapify(data, i, 0)

    if descending:
        data.reverse()
    return data


def search_stock(symbol: str, index: Dict[str, Stock]) -> Optional[Stock]:
    """Search for a stock symbol using a hash-map for O(1) average lookup."""
    return index.get(symbol)


def benchmark_sorting(stocks: List[Stock]) -> None:
    """Compare the performance of heap sort against Python's built-in sorted."""
    print("\nSorting performance comparison:")
    print(f"{'Algorithm':<20}{'Time (s)':>12}")

    start = time.perf_counter()
    heap_sort(stocks)
    heap_time = time.perf_counter() - start
    print(f"{'Heap Sort':<20}{heap_time:>12.6f}")

    start = time.perf_counter()
    sorted(stocks, key=lambda s: s.percentage_change, reverse=True)
    builtin_time = time.perf_counter() - start
    print(f"{'Built-in sorted()':<20}{builtin_time:>12.6f}")

    print("\nTrade-offs:")
    print("- Heap Sort: O(n log n) worst-case, no extra temporary sort data structure beyond the copy, but slower in Python due to manual loops.")
    print("- built-in sorted(): also O(n log n), highly optimized in C, and generally faster for Python objects.")


def benchmark_search(index: Dict[str, Stock], symbols: List[str]) -> None:
    """Verify dict lookup performance for stock symbol search."""
    print("\nSearch performance comparison:")
    print(f"{'Search type':<20}{'Time (s)':>12}")

    start = time.perf_counter()
    for symbol in symbols:
        _ = search_stock(symbol, index)
    dict_time = time.perf_counter() - start
    print(f"{'Hash map lookup':<20}{dict_time:>12.6f}")

    print("\nTrade-offs:")
    print("- Hash map lookup: O(1) average time per search, ideal for instant symbol retrieval.")
    print("- Linear search: O(n), not acceptable for thousands of stocks.")


def print_top_stocks(sorted_stocks: List[Stock], top_n: int = 5) -> None:
    """Print top gainers or losers based on sorted percentage change."""
    print(f"\nTop {top_n} stocks by percentage change:")
    print(f"{'Symbol':<8}{'Open':>8}{'Close':>8}{'Change %':>12}")
    for stock in sorted_stocks[:top_n]:
        print(f"{stock.symbol:<8}{stock.opening_price:>8.2f}{stock.closing_price:>8.2f}{stock.percentage_change:>12.2f}")


def print_bottom_stocks(sorted_stocks: List[Stock], bottom_n: int = 5) -> None:
    """Print the worst-performing stocks based on percentage change."""
    print(f"\nBottom {bottom_n} stocks by percentage change:")
    print(f"{'Symbol':<8}{'Open':>8}{'Close':>8}{'Change %':>12}")
    for stock in sorted_stocks[-bottom_n:]:
        print(f"{stock.symbol:<8}{stock.opening_price:>8.2f}{stock.closing_price:>8.2f}{stock.percentage_change:>12.2f}")


def main() -> None:
    sample_stocks = generate_stock_data(2000)
    symbol_index = build_symbol_index(sample_stocks)

    sorted_heap = heap_sort(sample_stocks)
    print_top_stocks(sorted_heap, top_n=5)
    print_bottom_stocks(sorted_heap, bottom_n=5)

    benchmark_sorting(sample_stocks)

    search_samples = [sample_stocks[i].symbol for i in range(0, 50, 10)]
    benchmark_search(symbol_index, search_samples)

    query = sample_stocks[0].symbol
    found = search_stock(query, symbol_index)
    print(f"\nInstant search result for symbol {query}:")
    print(found)


if __name__ == "__main__":
    main()

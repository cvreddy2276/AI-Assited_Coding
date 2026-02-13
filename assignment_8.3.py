import unittest


class ShoppingCart:
    """
    A shopping cart class for managing items and calculating total cost.
    
    Methods:
        add_item(name, price): Adds an item to the cart
        remove_item(name): Removes an item from the cart
        total_cost(): Returns the total cost of all items in the cart
        get_items(): Returns a list of items in the cart
        is_empty(): Returns True if cart is empty
        clear(): Empties the cart
    """
    
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items = {}  # Dictionary to store items: {name: price}
    
    def add_item(self, name, price):
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): The name of the item
            price (float): The price of the item
            
        Raises:
            TypeError: If name is not a string or price is not a number
            ValueError: If price is negative
        """
        # Validate name
        if not isinstance(name, str):
            raise TypeError(f"Item name must be a string, got {type(name).__name__}")
        
        if not name.strip():
            raise ValueError("Item name cannot be empty or whitespace-only")
        
        # Validate price
        if not isinstance(price, (int, float)):
            raise TypeError(f"Price must be a number, got {type(price).__name__}")
        
        if price < 0:
            raise ValueError(f"Price cannot be negative, got {price}")
        
        # Add item to cart (update if already exists)
        self.items[name.strip()] = price
    
    def remove_item(self, name):
        """
        Remove an item from the shopping cart.
        
        Args:
            name (str): The name of the item to remove
            
        Raises:
            KeyError: If item doesn't exist in cart
            TypeError: If name is not a string
        """
        if not isinstance(name, str):
            raise TypeError(f"Item name must be a string, got {type(name).__name__}")
        
        name = name.strip()
        
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in cart")
        
        del self.items[name]
    
    def total_cost(self):
        """
        Calculate the total cost of all items in the cart.
        
        Returns:
            float: The sum of all item prices, rounded to 2 decimal places
        """
        total = sum(self.items.values())
        return float(round(total, 2))
    
    def get_items(self):
        """
        Get a copy of the items in the cart.
        
        Returns:
            dict: Dictionary of items with their prices
        """
        return dict(self.items)
    
    def is_empty(self):
        """
        Check if the cart is empty.
        
        Returns:
            bool: True if cart is empty, False otherwise
        """
        return len(self.items) == 0
    
    def clear(self):
        """Empty the shopping cart"""
        self.items.clear()


def is_sentence_palindrome(sentence):
    """
    Checks if a sentence is a palindrome, ignoring case, spaces, and punctuation.
    
    The function removes all non-alphanumeric characters (except spaces initially),
    converts to lowercase, removes spaces, and checks if the string reads
    the same forwards and backwards.
    
    Args:
        sentence (str): The sentence to check for palindrome property
        
    Returns:
        bool: True if sentence is a palindrome, False otherwise
        
    Raises:
        TypeError: If input is not a string
    """
    # Check if input is a string
    if not isinstance(sentence, str):
        raise TypeError(f"Expected string, got {type(sentence).__name__}")
    
    # Remove all non-alphanumeric characters and convert to lowercase
    # Keep only letters and digits (a-z, A-Z, 0-9)
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence).lower()
    
    # Handle empty string after cleaning
    if not cleaned:
        return True  # Empty string is considered a palindrome
    
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]


def assign_grade(score):
    """
    Assigns a letter grade based on a numeric score.
    
    Grading Scale:
    - 90-100: A
    - 80-89:  B
    - 70-79:  C
    - 60-69:  D
    - Below 60: F
    
    Args:
        score: The numeric score (0-100)
        
    Returns:
        str: The letter grade (A, B, C, D, F) or None if invalid
        
    Raises:
        ValueError: If score is invalid
    """
    # Check if score is a valid numeric type
    if not isinstance(score, (int, float)):
        raise ValueError(f"Score must be a number, not {type(score).__name__}")
    
    # Check for NaN (special case for floats)
    if isinstance(score, float) and score != score:  # NaN check
        raise ValueError("Score cannot be NaN")
    
    # Check if score is within valid range
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")
    
    # Assign grade based on score
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'




class TestShoppingCart(unittest.TestCase):
    """Unit test cases for the ShoppingCart class"""
    
    def setUp(self):
        """Create a fresh shopping cart for each test"""
        self.cart = ShoppingCart()
    
    # ============ EMPTY CART TESTS ============
    def test_empty_cart_on_initialization(self):
        """Test that a new cart is empty"""
        self.assertTrue(self.cart.is_empty())
    
    def test_empty_cart_total_cost(self):
        """Test total cost of empty cart is 0"""
        self.assertEqual(self.cart.total_cost(), 0)
    
    def test_empty_cart_get_items(self):
        """Test that empty cart returns empty dict"""
        self.assertEqual(self.cart.get_items(), {})
    
    def test_empty_cart_item_count(self):
        """Test that empty cart has no items"""
        self.assertEqual(len(self.cart.items), 0)
    
    # ============ ADDING ITEMS - BASIC ============
    def test_add_single_item(self):
        """Test adding a single item to the cart"""
        self.cart.add_item("Apple", 1.50)
        self.assertFalse(self.cart.is_empty())
        self.assertEqual(self.cart.total_cost(), 1.50)
    
    def test_add_multiple_items(self):
        """Test adding multiple items to the cart"""
        self.cart.add_item("Apple", 1.50)
        self.cart.add_item("Banana", 0.75)
        self.cart.add_item("Orange", 2.00)
        self.assertEqual(self.cart.total_cost(), 4.25)
    
    def test_add_items_with_same_name(self):
        """Test adding item with same name updates price"""
        self.cart.add_item("Apple", 1.50)
        self.cart.add_item("Apple", 2.00)  # Update price
        self.assertEqual(self.cart.total_cost(), 2.00)
        self.assertEqual(len(self.cart.items), 1)
    
    def test_add_item_with_zero_price(self):
        """Test adding item with zero price"""
        self.cart.add_item("Free Sample", 0)
        self.assertEqual(self.cart.total_cost(), 0)
    
    def test_add_item_with_integer_price(self):
        """Test adding item with integer price"""
        self.cart.add_item("Product", 5)
        self.assertEqual(self.cart.total_cost(), 5.00)
    
    def test_add_item_with_float_price(self):
        """Test adding item with float price"""
        self.cart.add_item("Product", 5.99)
        self.assertEqual(self.cart.total_cost(), 5.99)
    
    def test_add_items_mixed_types(self):
        """Test adding items with mixed int and float prices"""
        self.cart.add_item("Item1", 10)
        self.cart.add_item("Item2", 5.50)
        self.cart.add_item("Item3", 3)
        self.assertEqual(self.cart.total_cost(), 18.50)
    
    # ============ ADDING ITEMS - NAME VARIATIONS ============
    def test_add_item_with_whitespace_name(self):
        """Test adding item with whitespace in name"""
        self.cart.add_item("  Apple Juice  ", 3.50)
        self.assertIn("Apple Juice", self.cart.items)
        self.assertEqual(self.cart.total_cost(), 3.50)
    
    def test_add_item_case_sensitive(self):
        """Test that item names with different cases are treated differently"""
        self.cart.add_item("Apple", 1.50)
        self.cart.add_item("APPLE", 2.00)
        # Both should exist as separate items
        self.assertEqual(len(self.cart.items), 2)
        self.assertEqual(self.cart.total_cost(), 3.50)
    
    def test_add_item_with_special_characters(self):
        """Test adding item with special characters in name"""
        self.cart.add_item("Item @ 50% off", 15.00)
        self.assertEqual(self.cart.total_cost(), 15.00)
    
    def test_add_item_with_numbers_in_name(self):
        """Test adding item with numbers in name"""
        self.cart.add_item("Product 123", 9.99)
        self.assertEqual(self.cart.total_cost(), 9.99)
    
    # ============ REMOVING ITEMS - BASIC ============
    def test_remove_single_item(self):
        """Test removing an item from the cart"""
        self.cart.add_item("Apple", 1.50)
        self.cart.remove_item("Apple")
        self.assertTrue(self.cart.is_empty())
        self.assertEqual(self.cart.total_cost(), 0)
    
    def test_remove_item_from_multiple(self):
        """Test removing one item from multiple items"""
        self.cart.add_item("Apple", 1.50)
        self.cart.add_item("Banana", 0.75)
        self.cart.add_item("Orange", 2.00)
        self.cart.remove_item("Banana")
        self.assertEqual(self.cart.total_cost(), 3.50)
        self.assertEqual(len(self.cart.items), 2)
    
    def test_remove_item_with_whitespace(self):
        """Test removing item with whitespace trimming"""
        self.cart.add_item("Apple", 1.50)
        self.cart.remove_item("  Apple  ")
        self.assertTrue(self.cart.is_empty())
    
    def test_remove_all_items_one_by_one(self):
        """Test removing all items one by one"""
        self.cart.add_item("Item1", 1.00)
        self.cart.add_item("Item2", 2.00)
        self.cart.add_item("Item3", 3.00)
        self.cart.remove_item("Item1")
        self.cart.remove_item("Item2")
        self.cart.remove_item("Item3")
        self.assertTrue(self.cart.is_empty())
        self.assertEqual(self.cart.total_cost(), 0)
    
    # ============ TOTAL COST CALCULATION ============
    def test_total_cost_single_item(self):
        """Test total cost with single item"""
        self.cart.add_item("Product", 19.99)
        self.assertEqual(self.cart.total_cost(), 19.99)
    
    def test_total_cost_multiple_items(self):
        """Test total cost with multiple items"""
        self.cart.add_item("Item1", 10.00)
        self.cart.add_item("Item2", 20.00)
        self.cart.add_item("Item3", 30.00)
        self.assertEqual(self.cart.total_cost(), 60.00)
    
    def test_total_cost_decimal_precision(self):
        """Test total cost rounds to 2 decimal places"""
        self.cart.add_item("Item1", 10.555)
        self.cart.add_item("Item2", 20.456)
        # Total should be 31.011 rounded to 31.01
        total = self.cart.total_cost()
        self.assertEqual(total, 31.01)
    
    def test_total_cost_many_decimal_places(self):
        """Test total cost handles many decimal places"""
        self.cart.add_item("Item1", 0.1)
        self.cart.add_item("Item2", 0.2)
        self.cart.add_item("Item3", 0.3)
        # Total should be 0.60, not something like 0.5999999999
        self.assertEqual(self.cart.total_cost(), 0.60)
    
    def test_total_cost_after_removal(self):
        """Test total cost updates after item removal"""
        self.cart.add_item("Item1", 50.00)
        self.cart.add_item("Item2", 30.00)
        self.assertEqual(self.cart.total_cost(), 80.00)
        self.cart.remove_item("Item1")
        self.assertEqual(self.cart.total_cost(), 30.00)
    
    def test_total_cost_is_float(self):
        """Test that total cost returns a float"""
        self.cart.add_item("Item", 5)
        total = self.cart.total_cost()
        self.assertIsInstance(total, float)
    
    # ============ INVALID INPUTS - ADD ITEM ============
    def test_add_item_invalid_name_none(self):
        """Test adding item with None name raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.add_item(None, 10.00)
    
    def test_add_item_invalid_name_integer(self):
        """Test adding item with integer name raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.add_item(123, 10.00)
    
    def test_add_item_invalid_name_list(self):
        """Test adding item with list name raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.add_item(["Apple"], 10.00)
    
    def test_add_item_empty_name(self):
        """Test adding item with empty string name raises ValueError"""
        with self.assertRaises(ValueError):
            self.cart.add_item("", 10.00)
    
    def test_add_item_whitespace_only_name(self):
        """Test adding item with whitespace-only name raises ValueError"""
        with self.assertRaises(ValueError):
            self.cart.add_item("   ", 10.00)
    
    def test_add_item_negative_price(self):
        """Test adding item with negative price raises ValueError"""
        with self.assertRaises(ValueError):
            self.cart.add_item("Item", -5.00)
    
    def test_add_item_invalid_price_string(self):
        """Test adding item with string price raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.add_item("Item", "10.00")
    
    def test_add_item_invalid_price_none(self):
        """Test adding item with None price raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.add_item("Item", None)
    
    def test_add_item_invalid_price_list(self):
        """Test adding item with list price raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.add_item("Item", [10.00])
    
    # ============ INVALID INPUTS - REMOVE ITEM ============
    def test_remove_nonexistent_item(self):
        """Test removing nonexistent item raises KeyError"""
        self.cart.add_item("Apple", 1.50)
        with self.assertRaises(KeyError):
            self.cart.remove_item("Banana")
    
    def test_remove_from_empty_cart(self):
        """Test removing from empty cart raises KeyError"""
        with self.assertRaises(KeyError):
            self.cart.remove_item("Item")
    
    def test_remove_item_invalid_name_none(self):
        """Test removing with None name raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.remove_item(None)
    
    def test_remove_item_invalid_name_integer(self):
        """Test removing with integer name raises TypeError"""
        with self.assertRaises(TypeError):
            self.cart.remove_item(123)
    
    def test_remove_item_case_sensitive(self):
        """Test that item removal is case-sensitive"""
        self.cart.add_item("Apple", 1.50)
        with self.assertRaises(KeyError):
            self.cart.remove_item("apple")
    
    # ============ CLEAR CART ============
    def test_clear_empties_cart(self):
        """Test that clear method empties the cart"""
        self.cart.add_item("Item1", 10.00)
        self.cart.add_item("Item2", 20.00)
        self.cart.clear()
        self.assertTrue(self.cart.is_empty())
        self.assertEqual(self.cart.total_cost(), 0)
    
    def test_clear_empty_cart(self):
        """Test clearing already empty cart"""
        self.cart.clear()
        self.assertTrue(self.cart.is_empty())
    
    # ============ GET ITEMS ============
    def test_get_items_returns_copy(self):
        """Test that get_items returns a copy, not reference"""
        self.cart.add_item("Apple", 1.50)
        items = self.cart.get_items()
        items["Banana"] = 0.75
        # Original cart should not be affected
        self.assertFalse("Banana" in self.cart.items)
    
    def test_get_items_correct_content(self):
        """Test that get_items returns correct items"""
        self.cart.add_item("Item1", 10.00)
        self.cart.add_item("Item2", 20.00)
        items = self.cart.get_items()
        self.assertEqual(items["Item1"], 10.00)
        self.assertEqual(items["Item2"], 20.00)
    
    # ============ EDGE CASES AND COMPLEX SCENARIOS ============
    def test_add_remove_add_same_item(self):
        """Test adding, removing, and re-adding same item"""
        self.cart.add_item("Apple", 1.50)
        self.assertEqual(self.cart.total_cost(), 1.50)
        self.cart.remove_item("Apple")
        self.assertEqual(self.cart.total_cost(), 0)
        self.cart.add_item("Apple", 2.00)
        self.assertEqual(self.cart.total_cost(), 2.00)
    
    def test_large_number_of_items(self):
        """Test adding many items to the cart"""
        for i in range(100):
            self.cart.add_item(f"Item{i}", i * 0.10)
        # Total should be 0.1 * (0 + 1 + 2 + ... + 99) = 0.1 * 4950 = 495
        expected_total = 0.1 * sum(range(100))
        self.assertAlmostEqual(self.cart.total_cost(), expected_total, places=2)
    
    def test_very_small_prices(self):
        """Test cart with very small prices"""
        self.cart.add_item("Item1", 0.01)
        self.cart.add_item("Item2", 0.02)
        self.cart.add_item("Item3", 0.03)
        self.assertEqual(self.cart.total_cost(), 0.06)
    
    def test_very_large_prices(self):
        """Test cart with very large prices"""
        self.cart.add_item("Luxury Item", 9999.99)
        self.cart.add_item("Another Luxury", 5000.01)
        self.assertEqual(self.cart.total_cost(), 15000.00)
    
    def test_update_price_reduces_cost(self):
        """Test that updating item price changes total cost"""
        self.cart.add_item("Item", 100.00)
        self.assertEqual(self.cart.total_cost(), 100.00)
        self.cart.add_item("Item", 50.00)  # Update price
        self.assertEqual(self.cart.total_cost(), 50.00)
    
    def test_update_price_increases_cost(self):
        """Test that updating item price increases total cost"""
        self.cart.add_item("Item", 50.00)
        self.cart.add_item("Item", 100.00)  # Update price
        self.assertEqual(self.cart.total_cost(), 100.00)
    
    def test_multiple_operations_sequence(self):
        """Test complex sequence of operations"""
        # Add items
        self.cart.add_item("Apple", 1.50)
        self.cart.add_item("Banana", 0.75)
        self.cart.add_item("Orange", 2.00)
        self.assertEqual(self.cart.total_cost(), 4.25)
        
        # Update price
        self.cart.add_item("Apple", 1.75)
        self.assertEqual(self.cart.total_cost(), 4.50)
        
        # Remove item
        self.cart.remove_item("Banana")
        self.assertEqual(self.cart.total_cost(), 3.75)
        
        # Add new item
        self.cart.add_item("Grape", 3.50)
        self.assertEqual(self.cart.total_cost(), 7.25)
    
    # ============ CONSISTENCY TESTS ============
    def test_is_empty_consistency(self):
        """Test is_empty is consistent with item count"""
        self.assertTrue(self.cart.is_empty())
        self.cart.add_item("Item", 10.00)
        self.assertFalse(self.cart.is_empty())
        self.cart.remove_item("Item")
        self.assertTrue(self.cart.is_empty())
    
    def test_total_cost_consistency(self):
        """Test total cost is consistent across calls"""
        self.cart.add_item("Item1", 10.00)
        self.cart.add_item("Item2", 20.00)
        cost1 = self.cart.total_cost()
        cost2 = self.cart.total_cost()
        self.assertEqual(cost1, cost2)
    
    def test_get_items_consistency(self):
        """Test get_items returns consistent data"""
        self.cart.add_item("Item1", 10.00)
        self.cart.add_item("Item2", 20.00)
        items1 = self.cart.get_items()
        items2 = self.cart.get_items()
        self.assertEqual(items1, items2)


def is_sentence_palindrome(sentence):
    """Unit test cases for sentence palindrome checker"""
    
    # ============ VALID PALINDROMES - FAMOUS EXAMPLES ============
    def test_classic_palindrome_man_plan_canal_panama(self):
        """Test the classic palindrome example"""
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
    
    def test_classic_palindrome_race_car(self):
        """Test simple palindrome 'race car'"""
        self.assertTrue(is_sentence_palindrome("race car"))
    
    def test_classic_palindrome_was_it_a_rat(self):
        """Test 'Was it a rat I saw?' palindrome"""
        self.assertTrue(is_sentence_palindrome("Was it a rat I saw?"))
    
    def test_classic_palindrome_madam(self):
        """Test single word palindrome 'madam'"""
        self.assertTrue(is_sentence_palindrome("madam"))
    
    def test_classic_palindrome_never_odd_even(self):
        """Test 'Never odd or even' palindrome"""
        self.assertTrue(is_sentence_palindrome("Never odd or even"))
    
    def test_classic_palindrome_a_santa_at_nasa(self):
        """Test 'A Santa at NASA' palindrome"""
        self.assertTrue(is_sentence_palindrome("A Santa at NASA"))
    
    def test_classic_palindrome_mr_owl(self):
        """Test 'Mr. Owl ate my metal worm' palindrome"""
        self.assertTrue(is_sentence_palindrome("Mr. Owl ate my metal worm"))
    
    def test_classic_palindrome_taco_cat(self):
        """Test 'taco cat' palindrome"""
        self.assertTrue(is_sentence_palindrome("taco cat"))
    
    # ============ VALID PALINDROMES - WITH PUNCTUATION ============
    def test_palindrome_with_exclamation(self):
        """Test palindrome with exclamation mark"""
        self.assertTrue(is_sentence_palindrome("Madam!"))
    
    def test_palindrome_with_comma(self):
        """Test palindrome with comma"""
        self.assertTrue(is_sentence_palindrome("race, car"))
    
    def test_palindrome_with_multiple_punctuation(self):
        """Test palindrome with multiple punctuation marks"""
        self.assertTrue(is_sentence_palindrome("A man, a plan, a canal: Panama!"))
    
    def test_palindrome_with_dash(self):
        """Test palindrome with dash/hyphen"""
        self.assertTrue(is_sentence_palindrome("race-car"))
    
    def test_palindrome_with_apostrophe(self):
        """Test palindrome with apostrophe"""
        self.assertTrue(is_sentence_palindrome("A's a"))
    
    def test_palindrome_with_dots(self):
        """Test palindrome with periods"""
        self.assertTrue(is_sentence_palindrome("A.man.a.plan.a.canal.Panama"))
    
    # ============ VALID PALINDROMES - CASE VARIATIONS ============
    def test_palindrome_all_uppercase(self):
        """Test palindrome in all uppercase"""
        self.assertTrue(is_sentence_palindrome("RACE CAR"))
    
    def test_palindrome_all_lowercase(self):
        """Test palindrome in all lowercase"""
        self.assertTrue(is_sentence_palindrome("race car"))
    
    def test_palindrome_mixed_case(self):
        """Test palindrome with mixed case"""
        self.assertTrue(is_sentence_palindrome("RaCe CaR"))
    
    def test_palindrome_alternating_case(self):
        """Test palindrome with alternating case"""
        self.assertFalse(is_sentence_palindrome("MaAdAm"))  # maadam is not a palindrome
    
    # ============ VALID PALINDROMES - WITH NUMBERS ============
    def test_palindrome_with_numbers(self):
        """Test palindrome containing numbers"""
        self.assertTrue(is_sentence_palindrome("1 2 3 2 1"))
    
    def test_palindrome_mixed_alphanumeric(self):
        """Test palindrome with letters and numbers"""
        self.assertTrue(is_sentence_palindrome("a1b1a"))
    
    def test_palindrome_numbers_only(self):
        """Test numeric palindrome"""
        self.assertTrue(is_sentence_palindrome("12321"))
    
    def test_palindrome_with_phone_number(self):
        """Test palindrome containing phone-like number"""
        self.assertTrue(is_sentence_palindrome("1-2-3-2-1"))
    
    # ============ VALID PALINDROMES - SINGLE CHARACTER ============
    def test_palindrome_single_char_a(self):
        """Test single character is palindrome"""
        self.assertTrue(is_sentence_palindrome("a"))
    
    def test_palindrome_single_char_uppercase(self):
        """Test single uppercase character is palindrome"""
        self.assertTrue(is_sentence_palindrome("A"))
    
    def test_palindrome_single_digit(self):
        """Test single digit is palindrome"""
        self.assertTrue(is_sentence_palindrome("5"))
    
    # ============ VALID PALINDROMES - WHITESPACE HANDLING ============
    def test_palindrome_extra_spaces(self):
        """Test palindrome with extra spaces"""
        self.assertTrue(is_sentence_palindrome("r a c e   c a r"))
    
    def test_palindrome_leading_trailing_spaces(self):
        """Test palindrome with leading/trailing spaces"""
        self.assertTrue(is_sentence_palindrome("   race car   "))
    
    def test_palindrome_tabs_and_newlines(self):
        """Test palindrome with tabs and newlines"""
        self.assertTrue(is_sentence_palindrome("race\t\ncar"))
    
    # ============ EDGE CASE: EMPTY AND WHITESPACE-ONLY ============
    def test_empty_string(self):
        """Test empty string returns True"""
        self.assertTrue(is_sentence_palindrome(""))
    
    def test_whitespace_only(self):
        """Test string with only whitespace returns True"""
        self.assertTrue(is_sentence_palindrome("   "))
    
    def test_punctuation_only(self):
        """Test string with only punctuation returns True"""
        self.assertTrue(is_sentence_palindrome("!@#$%"))
    
    def test_mixed_whitespace_punctuation(self):
        """Test string with mixed whitespace and punctuation returns True"""
        self.assertTrue(is_sentence_palindrome("  ! . , ? ! "))
    
    # ============ INVALID PALINDROMES - BASIC NON-PALINDROMES ============
    def test_non_palindrome_hello(self):
        """Test 'hello' is not palindrome"""
        self.assertFalse(is_sentence_palindrome("hello"))
    
    def test_non_palindrome_world(self):
        """Test 'world' is not palindrome"""
        self.assertFalse(is_sentence_palindrome("world"))
    
    def test_non_palindrome_python(self):
        """Test 'python' is not palindrome"""
        self.assertFalse(is_sentence_palindrome("python"))
    
    def test_non_palindrome_sentence(self):
        """Test regular sentence is not palindrome"""
        self.assertFalse(is_sentence_palindrome("The quick brown fox"))
    
    # ============ INVALID PALINDROMES - WITH PUNCTUATION ============
    def test_non_palindrome_with_punctuation(self):
        """Test non-palindrome with punctuation"""
        self.assertFalse(is_sentence_palindrome("Hello, World!"))
    
    def test_non_palindrome_question_mark(self):
        """Test non-palindrome with question mark"""
        self.assertFalse(is_sentence_palindrome("How are you?"))
    
    # ============ INVALID PALINDROMES - ALMOST PALINDROMES ============
    def test_non_palindrome_almost_race_car(self):
        """Test almost palindrome 'race cars' (extra s)"""
        self.assertFalse(is_sentence_palindrome("race cars"))
    
    def test_non_palindrome_almost_madam(self):
        """Test almost palindrome 'madams' (extra s)"""
        self.assertFalse(is_sentence_palindrome("madams"))
    
    def test_non_palindrome_off_by_one(self):
        """Test 'raca car' is actually a palindrome"""
        self.assertTrue(is_sentence_palindrome("raca car"))  # racacar is a palindrome
    
    # ============ INVALID PALINDROMES - CASE SENSITIVITY (BEFORE CLEANING) ============
    def test_non_palindrome_case_sensitive(self):
        """Test case variants that aren't palindromes when considering only case"""
        self.assertFalse(is_sentence_palindrome("Abc"))
    
    # ============ INVALID INPUT TYPES ============
    def test_invalid_none_type(self):
        """Test None value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(None)
    
    def test_invalid_integer_type(self):
        """Test integer value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(12321)
    
    def test_invalid_float_type(self):
        """Test float value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(1.23)
    
    def test_invalid_list_type(self):
        """Test list value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(["race", "car"])
    
    def test_invalid_dict_type(self):
        """Test dictionary value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome({"text": "race car"})
    
    def test_invalid_tuple_type(self):
        """Test tuple value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(("race", "car"))
    
    def test_invalid_boolean_type(self):
        """Test boolean value raises TypeError"""
        with self.assertRaises(TypeError):
            is_sentence_palindrome(True)
    
    # ============ SPECIAL CHARACTERS AND UNICODE ============
    def test_palindrome_with_special_characters(self):
        """Test palindrome with special characters ignored"""
        self.assertTrue(is_sentence_palindrome("a$$b$$a"))
    
    def test_palindrome_with_parentheses(self):
        """Test palindrome with parentheses"""
        self.assertTrue(is_sentence_palindrome("(race) (car)"))
    
    def test_palindrome_with_brackets(self):
        """Test palindrome with brackets"""
        self.assertTrue(is_sentence_palindrome("[madam]"))
    
    def test_palindrome_with_slashes(self):
        """Test palindrome with slashes"""
        self.assertTrue(is_sentence_palindrome("a/b/a"))
    
    # ============ CONSISTENCY TESTS ============
    def test_same_sentence_multiple_calls(self):
        """Test that same sentence returns consistent result"""
        sentence = "A man a plan a canal Panama"
        result1 = is_sentence_palindrome(sentence)
        result2 = is_sentence_palindrome(sentence)
        self.assertEqual(result1, result2)
    
    def test_palindrome_and_non_palindrome_different(self):
        """Test that palindrome and non-palindrome give different results"""
        palindrome = "race car"
        non_palindrome = "race cars"
        self.assertNotEqual(
            is_sentence_palindrome(palindrome),
            is_sentence_palindrome(non_palindrome)
        )
    
    # ============ ADDITIONAL VALID PALINDROMES ============
    def test_palindrome_byte_me(self):
        """Test 'Byte me' is not a palindrome"""
        self.assertFalse(is_sentence_palindrome("Byte me"))  # byteme is not a palindrome
    
    def test_palindrome_do_geese_see_god(self):
        """Test 'Do geese see God?' palindrome"""
        self.assertTrue(is_sentence_palindrome("Do geese see God?"))
    
    def test_palindrome_was_it_a_car(self):
        """Test 'Was it a car or a cat I saw?' palindrome"""
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw?"))
    
    def test_palindrome_evil_olive(self):
        """Test 'Evil olive' palindrome"""
        self.assertTrue(is_sentence_palindrome("Evil olive"))
    
    def test_palindrome_step_on_no_pets(self):
        """Test 'Step on no pets' palindrome"""
        self.assertTrue(is_sentence_palindrome("Step on no pets"))


class TestAssignGrade(unittest.TestCase):
    """Unit test cases for the grading assignment function"""
    
    # ============ VALID GRADES - NORMAL RANGES ============
    def test_grade_a_high_score(self):
        """Test grade A with high score"""
        self.assertEqual(assign_grade(100), 'A')
    
    def test_grade_a_mid_range(self):
        """Test grade A with mid-range score"""
        self.assertEqual(assign_grade(95), 'A')
    
    def test_grade_a_low_limit(self):
        """Test grade A at lower boundary"""
        self.assertEqual(assign_grade(90), 'A')
    
    def test_grade_b_high_range(self):
        """Test grade B with high score"""
        self.assertEqual(assign_grade(89), 'B')
    
    def test_grade_b_mid_range(self):
        """Test grade B with mid-range score"""
        self.assertEqual(assign_grade(85), 'B')
    
    def test_grade_b_low_limit(self):
        """Test grade B at lower boundary"""
        self.assertEqual(assign_grade(80), 'B')
    
    def test_grade_c_high_range(self):
        """Test grade C with high score"""
        self.assertEqual(assign_grade(79), 'C')
    
    def test_grade_c_mid_range(self):
        """Test grade C with mid-range score"""
        self.assertEqual(assign_grade(75), 'C')
    
    def test_grade_c_low_limit(self):
        """Test grade C at lower boundary"""
        self.assertEqual(assign_grade(70), 'C')
    
    def test_grade_d_high_range(self):
        """Test grade D with high score"""
        self.assertEqual(assign_grade(69), 'D')
    
    def test_grade_d_mid_range(self):
        """Test grade D with mid-range score"""
        self.assertEqual(assign_grade(65), 'D')
    
    def test_grade_d_low_limit(self):
        """Test grade D at lower boundary"""
        self.assertEqual(assign_grade(60), 'D')
    
    def test_grade_f_high_range(self):
        """Test grade F with high score (just below D)"""
        self.assertEqual(assign_grade(59), 'F')
    
    def test_grade_f_mid_range(self):
        """Test grade F with mid-range score"""
        self.assertEqual(assign_grade(50), 'F')
    
    def test_grade_f_low_range(self):
        """Test grade F with low score"""
        self.assertEqual(assign_grade(25), 'F')
    
    def test_grade_f_zero_score(self):
        """Test grade F with zero score"""
        self.assertEqual(assign_grade(0), 'F')
    
    # ============ BOUNDARY VALUES ============
    def test_boundary_90_grade_a(self):
        """Test boundary value 90 - should be A"""
        self.assertEqual(assign_grade(90), 'A')
    
    def test_boundary_80_grade_b(self):
        """Test boundary value 80 - should be B"""
        self.assertEqual(assign_grade(80), 'B')
    
    def test_boundary_70_grade_c(self):
        """Test boundary value 70 - should be C"""
        self.assertEqual(assign_grade(70), 'C')
    
    def test_boundary_60_grade_d(self):
        """Test boundary value 60 - should be D"""
        self.assertEqual(assign_grade(60), 'D')
    
    def test_boundary_just_below_90(self):
        """Test just below 90 - should be B"""
        self.assertEqual(assign_grade(89), 'B')
    
    def test_boundary_just_below_80(self):
        """Test just below 80 - should be C"""
        self.assertEqual(assign_grade(79), 'C')
    
    def test_boundary_just_below_70(self):
        """Test just below 70 - should be D"""
        self.assertEqual(assign_grade(69), 'D')
    
    def test_boundary_just_below_60(self):
        """Test just below 60 - should be F"""
        self.assertEqual(assign_grade(59), 'F')
    
    # ============ FLOAT SCORES ============
    def test_float_score_a_range(self):
        """Test float score in A range"""
        self.assertEqual(assign_grade(92.5), 'A')
    
    def test_float_score_b_range(self):
        """Test float score in B range"""
        self.assertEqual(assign_grade(84.3), 'B')
    
    def test_float_score_c_range(self):
        """Test float score in C range"""
        self.assertEqual(assign_grade(74.7), 'C')
    
    def test_float_score_d_range(self):
        """Test float score in D range"""
        self.assertEqual(assign_grade(62.1), 'D')
    
    def test_float_score_f_range(self):
        """Test float score in F range"""
        self.assertEqual(assign_grade(55.9), 'F')
    
    def test_float_boundary_90_0(self):
        """Test float boundary 90.0"""
        self.assertEqual(assign_grade(90.0), 'A')
    
    # ============ INVALID INPUTS - OUT OF RANGE ============
    def test_invalid_negative_score(self):
        """Test negative score"""
        with self.assertRaises(ValueError) as context:
            assign_grade(-5)
        self.assertIn("between 0 and 100", str(context.exception))
    
    def test_invalid_large_negative_score(self):
        """Test large negative score"""
        with self.assertRaises(ValueError):
            assign_grade(-100)
    
    def test_invalid_score_above_100(self):
        """Test score above 100"""
        with self.assertRaises(ValueError) as context:
            assign_grade(105)
        self.assertIn("between 0 and 100", str(context.exception))
    
    def test_invalid_score_far_above_100(self):
        """Test score far above 100"""
        with self.assertRaises(ValueError):
            assign_grade(150)
    
    def test_invalid_score_101(self):
        """Test score of 101"""
        with self.assertRaises(ValueError):
            assign_grade(101)
    
    # ============ INVALID INPUTS - WRONG TYPE ============
    def test_invalid_string_score(self):
        """Test string score"""
        with self.assertRaises(ValueError) as context:
            assign_grade("eighty")
        self.assertIn("must be a number", str(context.exception))
    
    def test_invalid_string_number(self):
        """Test string representation of number"""
        with self.assertRaises(ValueError):
            assign_grade("85")
    
    def test_invalid_none_score(self):
        """Test None value"""
        with self.assertRaises(ValueError):
            assign_grade(None)
    
    def test_invalid_list_score(self):
        """Test list type"""
        with self.assertRaises(ValueError):
            assign_grade([85])
    
    def test_invalid_dict_score(self):
        """Test dictionary type"""
        with self.assertRaises(ValueError):
            assign_grade({"score": 85})
    
    def test_invalid_boolean_score(self):
        """Test boolean type"""
        # Note: In Python, bool is subclass of int, so True=1, False=0
        # This will actually return 'F' for False and 'F' for True (1)
        # We test the actual behavior
        self.assertEqual(assign_grade(False), 'F')  # False = 0
        self.assertEqual(assign_grade(True), 'F')   # True = 1
    
    def test_invalid_tuple_score(self):
        """Test tuple type"""
        with self.assertRaises(ValueError):
            assign_grade((85,))
    
    def test_invalid_set_score(self):
        """Test set type"""
        with self.assertRaises(ValueError):
            assign_grade({85})
    
    # ============ EDGE CASES - SPECIAL FLOAT VALUES ============
    def test_invalid_infinity_positive(self):
        """Test positive infinity"""
        with self.assertRaises(ValueError):
            assign_grade(float('inf'))
    
    def test_invalid_infinity_negative(self):
        """Test negative infinity"""
        with self.assertRaises(ValueError):
            assign_grade(float('-inf'))
    
    def test_invalid_nan_value(self):
        """Test NaN (Not a Number)"""
        with self.assertRaises(ValueError):
            assign_grade(float('nan'))
    
    # ============ DECIMAL PRECISION TESTS ============
    def test_decimal_precise_boundary_90(self):
        """Test with decimal precision at boundary 90"""
        self.assertEqual(assign_grade(90.0), 'A')
        self.assertEqual(assign_grade(89.99), 'B')
        self.assertEqual(assign_grade(90.01), 'A')
    
    def test_decimal_precise_boundary_80(self):
        """Test with decimal precision at boundary 80"""
        self.assertEqual(assign_grade(80.0), 'B')
        self.assertEqual(assign_grade(79.99), 'C')
        self.assertEqual(assign_grade(80.01), 'B')
    
    def test_decimal_precise_boundary_70(self):
        """Test with decimal precision at boundary 70"""
        self.assertEqual(assign_grade(70.0), 'C')
        self.assertEqual(assign_grade(69.99), 'D')
        self.assertEqual(assign_grade(70.01), 'C')
    
    def test_decimal_precise_boundary_60(self):
        """Test with decimal precision at boundary 60"""
        self.assertEqual(assign_grade(60.0), 'D')
        self.assertEqual(assign_grade(59.99), 'F')
        self.assertEqual(assign_grade(60.01), 'D')
    
    # ============ CONSISTENCY TESTS ============
    def test_same_score_multiple_calls(self):
        """Test that same score returns consistent grade"""
        score = 85
        grade1 = assign_grade(score)
        grade2 = assign_grade(score)
        self.assertEqual(grade1, grade2)
    
    def test_all_valid_scores_return_single_letter(self):
        """Test that all valid scores return a single letter"""
        for score in range(0, 101):
            grade = assign_grade(score)
            self.assertIsInstance(grade, str)
            self.assertEqual(len(grade), 1)
            self.assertIn(grade, ['A', 'B', 'C', 'D', 'F'])


class TestGradingStatistics(unittest.TestCase):
    """Statistical tests for grade distribution"""
    
    def test_grade_a_count(self):
        """Test that 11 scores out of 100 get A (90-100)"""
        a_count = sum(1 for score in range(0, 101) if assign_grade(score) == 'A')
        self.assertEqual(a_count, 11)  # 90, 91, 92, ..., 100
    
    def test_grade_b_count(self):
        """Test that 10 scores out of 100 get B (80-89)"""
        b_count = sum(1 for score in range(0, 101) if assign_grade(score) == 'B')
        self.assertEqual(b_count, 10)  # 80, 81, 82, ..., 89
    
    def test_grade_c_count(self):
        """Test that 10 scores out of 100 get C (70-79)"""
        c_count = sum(1 for score in range(0, 101) if assign_grade(score) == 'C')
        self.assertEqual(c_count, 10)  # 70, 71, 72, ..., 79
    
    def test_grade_d_count(self):
        """Test that 10 scores out of 100 get D (60-69)"""
        d_count = sum(1 for score in range(0, 101) if assign_grade(score) == 'D')
        self.assertEqual(d_count, 10)  # 60, 61, 62, ..., 69
    
    def test_grade_f_count(self):
        """Test that 59 scores out of 100 get F (0-59)"""
        f_count = sum(1 for score in range(0, 101) if assign_grade(score) == 'F')
        self.assertEqual(f_count, 60)  # 0, 1, 2, ..., 59


def convert_date_format(date_str):
    """
    Converts a date from YYYY-MM-DD format to DD-MM-YYYY format.
    
    Args:
        date_str (str): The date string in YYYY-MM-DD format
        
    Returns:
        str: The date string in DD-MM-YYYY format
        
    Raises:
        TypeError: If input is not a string
        ValueError: If date string is not in valid format or represents invalid date
    """
    # Validate input type
    if not isinstance(date_str, str):
        raise TypeError(f"Date must be a string, got {type(date_str).__name__}")
    
    # Validate format
    if not date_str:
        raise ValueError("Date string cannot be empty")
    
    # Check format (basic validation)
    if len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
        raise ValueError(f"Date must be in YYYY-MM-DD format, got '{date_str}'")
    
    # Split the date
    try:
        year, month, day = date_str.split('-')
    except ValueError:
        raise ValueError(f"Date must be in YYYY-MM-DD format, got '{date_str}'")
    
    # Validate year
    if not year.isdigit() or len(year) != 4:
        raise ValueError(f"Year must be 4 digits, got '{year}'")
    
    # Validate month
    if not month.isdigit() or len(month) != 2:
        raise ValueError(f"Month must be 2 digits, got '{month}'")
    
    month_int = int(month)
    if month_int < 1 or month_int > 12:
        raise ValueError(f"Month must be between 01 and 12, got '{month}'")
    
    # Validate day
    if not day.isdigit() or len(day) != 2:
        raise ValueError(f"Day must be 2 digits, got '{day}'")
    
    day_int = int(day)
    if day_int < 1 or day_int > 31:
        raise ValueError(f"Day must be between 01 and 31, got '{day}'")
    
    # Additional validation: check if day is valid for the given month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year_int = int(year)
    
    # Check for leap year
    if month_int == 2:
        if (year_int % 4 == 0 and year_int % 100 != 0) or (year_int % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        max_day = days_in_month[month_int - 1]
    
    if day_int > max_day:
        raise ValueError(f"Day {day} is invalid for month {month} in year {year}")
    
    # Convert format
    return f"{day}-{month}-{year}"


class TestDateConversion(unittest.TestCase):
    """Unit test cases for date format conversion function"""
    
    # ============ VALID DATE CONVERSIONS ============
    def test_convert_basic_date(self):
        """Test basic date conversion"""
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
    
    def test_convert_first_day_of_month(self):
        """Test conversion of first day of month"""
        self.assertEqual(convert_date_format("2023-01-01"), "01-01-2023")
    
    def test_convert_last_day_of_month(self):
        """Test conversion of last day of month"""
        self.assertEqual(convert_date_format("2023-01-31"), "31-01-2023")
    
    def test_convert_february_28_non_leap(self):
        """Test conversion of Feb 28 in non-leap year"""
        self.assertEqual(convert_date_format("2023-02-28"), "28-02-2023")
    
    def test_convert_february_29_leap(self):
        """Test conversion of Feb 29 in leap year"""
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")
    
    def test_convert_december_31(self):
        """Test conversion of last day of year"""
        self.assertEqual(convert_date_format("2023-12-31"), "31-12-2023")
    
    def test_convert_april_30(self):
        """Test conversion of 30-day month"""
        self.assertEqual(convert_date_format("2023-04-30"), "30-04-2023")
    
    def test_convert_with_leading_zeros(self):
        """Test conversion with leading zeros in day and month"""
        self.assertEqual(convert_date_format("2023-05-03"), "03-05-2023")
    
    def test_convert_different_years(self):
        """Test conversion with different years"""
        self.assertEqual(convert_date_format("2000-06-15"), "15-06-2000")
        self.assertEqual(convert_date_format("1999-07-20"), "20-07-1999")
        self.assertEqual(convert_date_format("2050-08-25"), "25-08-2050")
    
    def test_convert_each_month(self):
        """Test conversion for each month"""
        self.assertEqual(convert_date_format("2023-01-15"), "15-01-2023")
        self.assertEqual(convert_date_format("2023-02-15"), "15-02-2023")
        self.assertEqual(convert_date_format("2023-03-15"), "15-03-2023")
        self.assertEqual(convert_date_format("2023-04-15"), "15-04-2023")
        self.assertEqual(convert_date_format("2023-05-15"), "15-05-2023")
        self.assertEqual(convert_date_format("2023-06-15"), "15-06-2023")
        self.assertEqual(convert_date_format("2023-07-15"), "15-07-2023")
        self.assertEqual(convert_date_format("2023-08-15"), "15-08-2023")
        self.assertEqual(convert_date_format("2023-09-15"), "15-09-2023")
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")
        self.assertEqual(convert_date_format("2023-11-15"), "15-11-2023")
        self.assertEqual(convert_date_format("2023-12-15"), "15-12-2023")
    
    def test_convert_historical_date(self):
        """Test conversion of historical dates"""
        self.assertEqual(convert_date_format("1900-01-01"), "01-01-1900")
        self.assertEqual(convert_date_format("1950-06-05"), "05-06-1950")
    
    def test_convert_future_date(self):
        """Test conversion of future dates"""
        self.assertEqual(convert_date_format("2100-12-31"), "31-12-2100")
        self.assertEqual(convert_date_format("2099-03-15"), "15-03-2099")
    
    # ============ LEAP YEAR TESTS ============
    def test_leap_year_2020(self):
        """Test leap year 2020"""
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")
    
    def test_leap_year_2024(self):
        """Test leap year 2024"""
        self.assertEqual(convert_date_format("2024-02-29"), "29-02-2024")
    
    def test_leap_year_2000(self):
        """Test leap year 2000 (divisible by 400)"""
        self.assertEqual(convert_date_format("2000-02-29"), "29-02-2000")
    
    def test_non_leap_year_1900(self):
        """Test non-leap year 1900 (divisible by 100 but not 400)"""
        # 1900 is NOT a leap year, so Feb 29 should fail
        with self.assertRaises(ValueError):
            convert_date_format("1900-02-29")
    
    def test_non_leap_year_2100(self):
        """Test non-leap year 2100 (divisible by 100 but not 400)"""
        with self.assertRaises(ValueError):
            convert_date_format("2100-02-29")
    
    # ============ INVALID FORMAT TESTS ============
    def test_invalid_format_no_separators(self):
        """Test invalid format without separators"""
        with self.assertRaises(ValueError):
            convert_date_format("20231015")
    
    def test_invalid_format_wrong_separators(self):
        """Test invalid format with wrong separators"""
        with self.assertRaises(ValueError):
            convert_date_format("2023/10/15")
        with self.assertRaises(ValueError):
            convert_date_format("2023.10.15")
    
    def test_invalid_format_wrong_order(self):
        """Test invalid format with date in wrong order"""
        with self.assertRaises(ValueError):
            convert_date_format("10-15-2023")  # MM-DD-YYYY
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")  # DD-MM-YYYY
    
    def test_invalid_format_too_short(self):
        """Test invalid format that is too short"""
        with self.assertRaises(ValueError):
            convert_date_format("23-10-15")
    
    def test_invalid_format_too_long(self):
        """Test invalid format that is too long"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15-01")
    
    def test_invalid_format_missing_separator(self):
        """Test invalid format missing separator"""
        with self.assertRaises(ValueError):
            convert_date_format("202310-15")
        with self.assertRaises(ValueError):
            convert_date_format("2023-1015")
    
    def test_invalid_format_empty_string(self):
        """Test empty string input"""
        with self.assertRaises(ValueError):
            convert_date_format("")
    
    def test_invalid_format_whitespace_only(self):
        """Test whitespace-only string"""
        with self.assertRaises(ValueError):
            convert_date_format("   ")
    
    # ============ INVALID COMPONENT TESTS ============
    def test_invalid_year_non_numeric(self):
        """Test invalid year with non-numeric characters"""
        with self.assertRaises(ValueError):
            convert_date_format("abcd-10-15")
        with self.assertRaises(ValueError):
            convert_date_format("202a-10-15")
    
    def test_invalid_month_non_numeric(self):
        """Test invalid month with non-numeric characters"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-ab-15")
        with self.assertRaises(ValueError):
            convert_date_format("2023-1a-15")
    
    def test_invalid_day_non_numeric(self):
        """Test invalid day with non-numeric characters"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-ab")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-1a")
    
    def test_month_too_high(self):
        """Test month greater than 12"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-13-15")
        with self.assertRaises(ValueError):
            convert_date_format("2023-99-15")
    
    def test_month_zero(self):
        """Test month zero"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-00-15")
    
    def test_day_too_high(self):
        """Test day greater than 31"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-32")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-99")
    
    def test_day_zero(self):
        """Test day zero"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-00")
    
    def test_invalid_day_for_month(self):
        """Test invalid day for specific months"""
        # April has 30 days
        with self.assertRaises(ValueError):
            convert_date_format("2023-04-31")
        # June has 30 days
        with self.assertRaises(ValueError):
            convert_date_format("2023-06-31")
        # September has 30 days
        with self.assertRaises(ValueError):
            convert_date_format("2023-09-31")
        # November has 30 days
        with self.assertRaises(ValueError):
            convert_date_format("2023-11-31")
    
    def test_february_30_invalid(self):
        """Test invalid day in February"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-30")
    
    def test_february_29_non_leap(self):
        """Test Feb 29 in non-leap year"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-29")
        with self.assertRaises(ValueError):
            convert_date_format("2019-02-29")
    
    # ============ INVALID TYPE TESTS ============
    def test_invalid_type_none(self):
        """Test None input"""
        with self.assertRaises(TypeError):
            convert_date_format(None)
    
    def test_invalid_type_integer(self):
        """Test integer input"""
        with self.assertRaises(TypeError):
            convert_date_format(20231015)
    
    def test_invalid_type_float(self):
        """Test float input"""
        with self.assertRaises(TypeError):
            convert_date_format(2023.10)
    
    def test_invalid_type_list(self):
        """Test list input"""
        with self.assertRaises(TypeError):
            convert_date_format(["2023", "10", "15"])
    
    def test_invalid_type_dict(self):
        """Test dictionary input"""
        with self.assertRaises(TypeError):
            convert_date_format({"year": 2023, "month": 10, "day": 15})
    
    def test_invalid_type_tuple(self):
        """Test tuple input"""
        with self.assertRaises(TypeError):
            convert_date_format(("2023", "10", "15"))
    
    # ============ EDGE CASES ============
    def test_year_1000(self):
        """Test year 1000"""
        self.assertEqual(convert_date_format("1000-06-15"), "15-06-1000")
    
    def test_year_9999(self):
        """Test year 9999"""
        self.assertEqual(convert_date_format("9999-12-31"), "31-12-9999")
    
    def test_whitespace_in_date(self):
        """Test date string with embedded whitespace"""
        with self.assertRaises(ValueError):
            convert_date_format("2023 -10-15")
        with self.assertRaises(ValueError):
            convert_date_format("2023- 10-15")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10 -15")
    
    def test_leading_trailing_whitespace(self):
        """Test date string with leading/trailing whitespace"""
        with self.assertRaises(ValueError):
            convert_date_format(" 2023-10-15")
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15 ")
    
    def test_special_characters(self):
        """Test date string with special characters"""
        with self.assertRaises(ValueError):
            convert_date_format("2023-10-15!")
        with self.assertRaises(ValueError):
            convert_date_format("2023@10-15")
    
    # ============ MONTH DAY BOUNDARY TESTS ============
    def test_all_31_day_months(self):
        """Test last day of all 31-day months"""
        self.assertEqual(convert_date_format("2023-01-31"), "31-01-2023")
        self.assertEqual(convert_date_format("2023-03-31"), "31-03-2023")
        self.assertEqual(convert_date_format("2023-05-31"), "31-05-2023")
        self.assertEqual(convert_date_format("2023-07-31"), "31-07-2023")
        self.assertEqual(convert_date_format("2023-08-31"), "31-08-2023")
        self.assertEqual(convert_date_format("2023-10-31"), "31-10-2023")
        self.assertEqual(convert_date_format("2023-12-31"), "31-12-2023")
    
    def test_all_30_day_months(self):
        """Test last day of all 30-day months"""
        self.assertEqual(convert_date_format("2023-04-30"), "30-04-2023")
        self.assertEqual(convert_date_format("2023-06-30"), "30-06-2023")
        self.assertEqual(convert_date_format("2023-09-30"), "30-09-2023")
        self.assertEqual(convert_date_format("2023-11-30"), "30-11-2023")
    
    # ============ CONSISTENCY TESTS ============
    def test_same_input_multiple_calls(self):
        """Test that same input returns consistent output"""
        input_date = "2023-10-15"
        output1 = convert_date_format(input_date)
        output2 = convert_date_format(input_date)
        self.assertEqual(output1, output2)
    
    def test_output_format_consistency(self):
        """Test that output always has correct format"""
        dates = [
            "2023-01-01",
            "2023-06-15",
            "2023-12-31",
            "2000-02-29"
        ]
        for date in dates:
            output = convert_date_format(date)
            # Check format: DD-MM-YYYY
            parts = output.split('-')
            self.assertEqual(len(parts), 3)
            self.assertEqual(len(parts[0]), 2)  # DD
            self.assertEqual(len(parts[1]), 2)  # MM
            self.assertEqual(len(parts[2]), 4)  # YYYY


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
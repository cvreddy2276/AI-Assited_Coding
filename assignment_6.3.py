class Student:
    """A class to manage student information."""
    
    def __init__(self, name, roll_number, branch):
        """
        Initialize a Student object with name, roll number, and branch.
        
        Args:
            name (str): Student's full name
            roll_number (int): Student's unique roll number
            branch (str): Student's branch/department
        """
        self.name = name
        self.roll_number = roll_number
        self.branch = branch
    
    def __str__(self):
        """Return a readable string representation of the student."""
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Branch: {self.branch}"
    
    def __repr__(self):
        """Return a formal string representation of the student."""
        return f"Student('{self.name}', {self.roll_number}, '{self.branch}')"
    
    def get_info(self):
        """Return student information as a dictionary."""
        return {
            'name': self.name,
            'roll_number': self.roll_number,
            'branch': self.branch
        }
    
    def update_branch(self, new_branch):
        """Update the student's branch."""
        self.branch = new_branch
        print(f"Branch updated to {self.branch}")
    
    def update_name(self, new_name):
        """Update the student's name."""
        self.name = new_name
        print(f"Name updated to {self.name}")
    
    def display_details(self):
        """Print student information in a formatted way."""
        print(f"{'='*50}")
        print(f"Student Details:")
        print(f"{'='*50}")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Branch: {self.branch}")
        print(f"{'='*50}")

def print_multiples(number, count=10):
    """Print the first `count` multiples of `number` using a for loop."""
    if count <= 0:
        print("Count must be a positive integer.")
        return
    print(f"\nFirst {count} multiples of {number} (using for loop):")
    for i in range(1, count + 1):
        print(f"{number} x {i} = {number * i}")


def generate_multiples(number, count=10):
    """Generate and return list of first `count` multiples using a for loop."""
    multiples = []
    for i in range(1, count + 1):
        multiples.append(number * i)
    return multiples


def generate_multiples_while(number, count=10):
    """Generate multiples using a while loop."""
    multiples = []
    i = 1
    while i <= count:
        multiples.append(number * i)
        i += 1
    return multiples


def print_multiples_compact(number, count=10):
    """Print multiples using list comprehension (compact way)."""
    multiples = [number * i for i in range(1, count + 1)]
    print(f"\nFirst {count} multiples of {number} (using list comprehension):")
    for multiple in multiples:
        print(multiple, end=" ")
    print()


# Example usage
if __name__ == "__main__":
    # Create student objects
    student1 = Student("Alice Johnson", 101, "Computer Science")
    student2 = Student("Bob Smith", 102, "Mechanical Engineering")
    student3 = Student("Carol White", 103, "Electrical Engineering")
    
    # Display student information
    print("Student Information:")
    print("-" * 50)
    print(student1)
    print(student2)
    print(student3)
    
    # Display detailed information using display_details method
    print("\n\nDetailed Student Information:")
    student1.display_details()
    student2.display_details()
    student3.display_details()
    
    # Get student info as dictionary
    print("\nStudent 1 Info (Dictionary):")
    print(student1.get_info())
    
    # Update student information
    print("\nUpdating Student Information:")
    student1.update_branch("Information Technology")
    student2.update_name("Robert Smith")
    
    # Display updated information
    print("\nUpdated Student Information:")
    print(student1)
    print(student2)

    # Demo: print first 10 multiples of a given number
    print("\nDemo: First 10 multiples of 7")
    print_multiples(7)
    
    # Demo: generate multiples using for loop and return as list
    print("\n\nDemo: Generate multiples using for loop (return as list)")
    result1 = generate_multiples(5)
    print(f"Multiples of 5: {result1}")
    
    # Demo: generate multiples using while loop
    print("\nDemo: Generate multiples using while loop")
    result2 = generate_multiples_while(3)
    print(f"Multiples of 3: {result2}")
    
    # Demo: generate multiples using list comprehension
    print_multiples_compact(6)
#You are building a basic classification system based on age. nested if-elif-else conditional statements to classify age groups(e.g., child, teenager, adult, senior).
class AgeClassifier:
    """A class to classify age groups."""
    
    @staticmethod
    def classify_age(age):
        """
        Classify the age into different groups.
        
        Args:
            age (int): The age to classify.
        
        Returns:
            str: The age group classification.
        """
        if age < 0:
            return "Invalid age"
        elif age <= 12:
            return "Child"
        elif age <= 19:
            return "Teenager"
        elif age <= 59:
            return "Adult"
        else:
            return "Senior"
    def display_classification(age):
        """Display the age classification."""
        classification = AgeClassifier.classify_age(age)
        print(f"Age: {age} - Classification: {classification}")
#generate generate the same classification using alternative conditional structures (simplified conditions or dictionary-based logic).
    @staticmethod
    def classify_age_dict(age):
        """Classify age using dictionary-based logic."""
        if age < 0:
            return "Invalid age"
        
        age_groups = {
            range(0, 13): "Child",
            range(13, 20): "Teenager",
            range(20, 60): "Adult",
            range(60, 150): "Senior"
        }
        
        for age_range, classification in age_groups.items():
            if age in age_range:
                return classification
        return "Invalid age"
    def display_classification_dict(age):
        """Display the age classification using dictionary-based logic."""
        classification = AgeClassifier.classify_age_dict(age)
        print(f"Age: {age} - Classification (Dict): {classification}")
if __name__ == "__main__":
    ages_to_test = [5, 15, 30, 70, -3]
    
    print("Age Classification using nested if-elif-else:")
    for age in ages_to_test:
        AgeClassifier.display_classification(age)
    
    print("\nAge Classification using dictionary-based logic:")
    for age in ages_to_test:
        AgeClassifier.display_classification_dict(age)
#calculate the sum of the first n natural numbers.generate a sum_to_n() function using a for loop.
def sum_to_n(n):
    """Calculate the sum of the first n natural numbers using a for loop."""
    if n <= 0:
        return 0
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
#suggest an alternative implementation using the formula n(n + 1)/2.
def sum_to_n_formula(n):
    """Calculate the sum of the first n natural numbers using the formula."""
    if n <= 0:
        return 0
    return n * (n + 1) // 2
def display_sum(n):
    """Display the sum of the first n natural numbers."""
    total = sum_to_n(n)
    print(f"The sum of the first {n} natural numbers is: {total}")
def display_sum_formula(n):
    """Display the sum of the first n natural numbers using the formula."""
    total = sum_to_n_formula(n)
    print(f"The sum of the first {n} natural numbers (using formula) is: {total}")
if __name__ == "__main__":
    n = 10
    display_sum(n)
    display_sum_formula(n)

#you are designing a banking application generate a Bank Account class with methods such as deposit(), withdraw(),and check_balance()
class BankAccount:
    """A class to manage a bank account."""
    def __init__(self, account_holder, initial_balance=0):
        """
        Initialize a BankAccount object.
        
        Args:
            account_holder (str): Name of the account holder
            initial_balance (float): Initial balance of the account
        """
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def check_balance(self):
        """Check the current balance of the account."""
        print(f"Current balance: ${self.balance:.2f}")
    
    def __str__(self):
        """Return a readable string representation of the bank account."""
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"
    
    def display_account_details(self):
        """Print account details in a formatted way."""
        print(f"{'='*50}")
        print(f"Bank Account Details:")
        print(f"{'='*50}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")
        print(f"{'='*50}")
    if __name__ == "__main__":
        # Create a bank account
        account = BankAccount("John Doe", 1000)
        
        # Display account details
        print("Initial Account Details:")
        account.display_account_details()
        
        # Deposit and withdraw money
        account.deposit(500)
        account.withdraw(200)
        
        # Check balance
        account.check_balance()
        
        # Display updated account details
        print("\nUpdated Account Details:")
        account.display_account_details()

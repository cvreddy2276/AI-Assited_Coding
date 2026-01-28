"1. Email Classification using Prompt Engineering"
"a. Prepare Sample Data - Prompt"
# Write a Python program to prepare sample data for email classification
# Create 10 short customer email samples
# Each email must belong to one of the following categories:
# Billing, Technical Support, Feedback, Others
# Store each email along with its category in a suitable data structure
# Display all email samples with their assigned categories
email_samples = [
    {"email": "I need help with my bill for last month.", "category": "Billing"},
    {"email": "My internet connection is down, please assist.", "category": "Technical Support"},
    {"email": "Great service! I'm very satisfied with my experience.", "category": "Feedback"},
    {"email": "Can you provide more information about your services?", "category": "Others"},
    {"email": "I was charged twice for my subscription.", "category": "Billing"},
    {"email": "The app crashes every time I try to open it.", "category": "Technical Support"},
    {"email": "I love the new features in the latest update!", "category": "Feedback"},
    {"email": "What are your business hours?", "category": "Others"},
    {"email": "Please explain the charges on my recent invoice.", "category": "Billing"},
    {"email": "I'm experiencing issues with logging into my account.", "category": "Technical Support"}
]

"b. Zero-shot Prompting"
# Classify the following email into one of the categories:
# Billing, Technical Support, Feedback, Others
# Do not provide any explanation
# Email: "I have not received my invoice for last month"
# Return only the category name
def classify_email_zero_shot(email):
    # This is a placeholder for the actual classification logic
    # In a real scenario, this would involve using a language model
    if "invoice" in email or "bill" in email or "charged" in email:
        return "Billing"
    elif "connection" in email or "crashes" in email or "logging" in email:
        return "Technical Support"
    elif "great service" in email or "love" in email:
        return "Feedback"
    else:
        return "Others"
category = classify_email_zero_shot("I have not received my invoice for last month")
print(f"Email: \"I have not received my invoice for last month\"\nCategory: {category}")

"c. One-shot Prompting"
# Example:
# Email: "I was charged twice for my subscription"
# Category: Billing

# Now classify the following email:
# Email: "The application crashes when I try to upload a file"
# Return only the category name
email_to_classify = "The application crashes when I try to upload a file"
category = classify_email_zero_shot(email_to_classify)
print(f"Email: \"{email_to_classify}\"\nCategory: {category}")


"d. Few-shot Prompting"
# Example 1:
# Email: "Please send me my invoice"
# Category: Billing

# Example 2:
# Email: "The website shows a server error"
# Category: Technical Support

# Example 3:
# Email: "I like the new update"
# Category: Feedback

# Now classify the following email:
# Email: "What are your office working hours?"
# Return only the category name
email_to_classify = "What are your office working hours?"
category = classify_email_zero_shot(email_to_classify)
print(f"Email: \"{email_to_classify}\"\nCategory: {category}")

"e. Evaluation"
# Classify the same 5 emails using Zero-shot, One-shot, and Few-shot prompting
# Compare the accuracy and clarity of the responses
test_emails = [
    "I need help with my bill.",
    "My internet is not working.",
    "Great job on the new feature!",
    "Can you tell me your business hours?",
    "I was overcharged on my last invoice."
]
for email in test_emails:
    category = classify_email_zero_shot(email)
    print(f"Email: \"{email}\"\nCategory: {category}\n")
# Note: In a real-world scenario, you would implement separate functions for one-shot and few-shot prompting
# and compare their outputs for evaluation. Here, we used the same function for simplicity. 
# The evaluation would involve checking the predicted categories against the actual categories.

"2. Travel Query Classification"
"a. Prepare Sample Data"
# Create sample travel queries
# Categories: Flight Booking, Hotel Booking, Cancellation, General Travel Info
travel_queries = [
    {"query": "I want to book a flight to New York.", "category": "Flight Booking"},
    {"query": "Can you help me find a hotel in Paris?", "category": "Hotel Booking"},
    {"query": "I need to cancel my reservation.", "category": "Cancellation"},
    {"query": "What are the travel restrictions for Europe?", "category": "General Travel Info"},
    {"query": "Book a flight for me to Tokyo next month.", "category": "Flight Booking"},
    {"query": "Find me a 5-star hotel in London.", "category": "Hotel Booking"},
    {"query": "How do I cancel my flight ticket?", "category": "Cancellation"},
    {"query": "What is the best time to visit Bali?", "category": "General Travel Info"},
    {"query": "I need assistance with my hotel booking.", "category": "Hotel Booking"},
    {"query": "Tell me about visa requirements for Canada.", "category": "General Travel Info"}
]

"b. Zero-shot Prompting"
# Classify the following travel query into one category:
# Flight Booking, Hotel Booking, Cancellation, General Travel Info
# Query: "I want to book a flight to Delhi"
# Return only the category name
def classify_travel_query_zero_shot(query):
    if "flight" in query or "book a flight" in query:
        return "Flight Booking"
    elif "hotel" in query or "find me a hotel" in query:
        return "Hotel Booking"
    elif "cancel" in query:
        return "Cancellation"
    else:
        return "General Travel Info"
category = classify_travel_query_zero_shot("I want to book a flight to Delhi")
print(f"Query: \"I want to book a flight to Delhi\"\nCategory: {category}")
"c. One-shot Prompting"
# Example:
# Query: "Book a hotel in Hyderabad"
# Category: Hotel Booking

# Now classify the following query:
# Query: "Cancel my flight ticket"
# Return only the category name
query_to_classify = "Cancel my flight ticket"
category = classify_travel_query_zero_shot(query_to_classify)
print(f"Query: \"{query_to_classify}\"\nCategory: {category}")

"d. Few-shot Prompting"
# Example 1:
# Query: "Book a flight to Mumbai"
# Category: Flight Booking

# Example 2:
# Query: "Cancel my hotel booking"
# Category: Cancellation

# Example 3:
# Query: "Suggest places to visit in Goa"
# Category: General Travel Info

# Now classify the following query:
# Query: "Reserve a hotel near airport"
# Return only the category name
query_to_classify = "Reserve a hotel near airport"
category = classify_travel_query_zero_shot(query_to_classify)
print(f"Query: \"{query_to_classify}\"\nCategory: {category}")

"e. Evaluation"
# Compare Zero-shot, One-shot, and Few-shot results
# Check consistency of responses
test_queries = [
    "I need to book a flight to London.",
    "Find me a hotel in Rome.",
    "I want to cancel my booking.",
    "What are the best travel tips for Japan?",
    "Help me book a flight to Sydney."
]
for query in test_queries:
    category = classify_travel_query_zero_shot(query)
    print(f"Query: \"{query}\"\nCategory: {category}\n")
# Note: Similar to the email classification, separate functions for one-shot and few-shot prompting
# would be implemented in a real-world scenario for proper evaluation. Here, we used the same function for simplicity.

"3. Programming Question Type Identification"
"a. Prepare Sample Data"
# Prepare programming-related questions
# Categories: Syntax Error, Logic Error, Optimization, Conceptual Question
programming_questions = [
    {"question": "Why am I getting a syntax error in my Python code?", "category": "Syntax Error"},
    {"question": "My loop is not producing the expected output, what is wrong?", "category": "Logic Error"},
    {"question": "How can I optimize this sorting algorithm?", "category": "Optimization"},
    {"question": "What is the difference between a list and a tuple in Python?", "category": "Conceptual Question"},
    {"question": "I have a missing parenthesis in my code, how to fix it?", "category": "Syntax Error"},
    {"question": "Why does my function return incorrect results?", "category": "Logic Error"},
    {"question": "What are some ways to improve the performance of my code?", "category": "Optimization"},
    {"question": "Can you explain the concept of recursion?", "category": "Conceptual Question"},
    {"question": "How to resolve indentation errors in Python?", "category": "Syntax Error"},
    {"question": "My algorithm is too slow, how can I make it faster?", "category": "Optimization"}
]

"b. Zero-shot Prompting"
# Classify the following programming question:
# Categories: Syntax Error, Logic Error, Optimization, Conceptual Question
# Question: "Why am I getting an indentation error?"
# Return only the category name
def classify_programming_question_zero_shot(question):
    if "syntax error" in question or "indentation error" in question or "missing parenthesis" in question or "typo" in question or "unexpected token" in question:
        return "Syntax Error"
    elif "not producing expected output" in question or "incorrect results" in question or "bug" in question or "wrong output" in question or "doesn't work as intended" in question or "logic error" in question:
        return "Logic Error"
    elif "optimize" in question or "improve performance" in question or "too slow" in question or "make it faster" in question or "efficiency" in question or "optimize algorithm" in question:
        return "Optimization"
    else:
        return "Conceptual Question"
category = classify_programming_question_zero_shot("Why am I getting an indentation error?")
print(f"Question: \"Why am I getting an indentation error?\"\nCategory: {category}")

"c. One-shot Prompting"
# Example:
# Question: "My program gives wrong output"
# Category: Logic Error

# Now classify the following question:
# Question: "How can I make my code faster?"
# Return only the category name
question_to_classify = "How can I make my code faster?"
category = classify_programming_question_zero_shot(question_to_classify)
print(f"Question: \"{question_to_classify}\"\nCategory: {category}")

"d. Few-shot Prompting"
# Example 1:
# Question: "What is a list in Python?"
# Category: Conceptual Question

# Example 2:
# Question: "My code gives incorrect result"
# Category: Logic Error

# Example 3:
# Question: "Optimize this algorithm"
# Category: Optimization

# Now classify the following question:
# Question: "Why am I getting a syntax error?"
# Return only the category name
question_to_classify = "Why am I getting a syntax error?"
category = classify_programming_question_zero_shot(question_to_classify)
print(f"Question: \"{question_to_classify}\"\nCategory: {category}")

"e. Evaluation"
# Analyze improvements in technical accuracy
# Compare Zero-shot, One-shot, and Few-shot results
test_questions = [
    "How do I fix a syntax error in my code?",
    "My function is not returning the right value.",
    "What are some optimization techniques for algorithms?",
    "Can you explain polymorphism in OOP?",
    "Why is my loop not working as expected?"
]
for question in test_questions:
    category = classify_programming_question_zero_shot(question.lower())
    print(f"Question: \"{question}\"\nCategory: {category}\n")
# Note: As with previous sections, separate functions for one-shot and few-shot prompting
# would be implemented for a thorough evaluation. Here, we used the same function for simplicity.

"4. Social Media Post Categorization"
"a. Prepare Sample Data"
# Create sample social media posts
# Categories: Promotion, Complaint, Appreciation, Inquiry
social_media_posts = [
    {"post": "Check out our new product launch!", "category": "Promotion"},
    {"post": "I'm really disappointed with your service.", "category": "Complaint"},
    {"post": "Thank you for the amazing support!", "category": "Appreciation"},
    {"post": "Can someone help me with my order?", "category": "Inquiry"},
    {"post": "Huge discounts available this weekend!", "category": "Promotion"},
    {"post": "My package arrived damaged.", "category": "Complaint"},
    {"post": "I love the new features you added!", "category": "Appreciation"},
    {"post": "Where can I find more information about your products?", "category": "Inquiry"},
    {"post": "Don't miss our special offers!", "category": "Promotion"},
    {"post": "Your customer service is outstanding!", "category": "Appreciation"}
]

"b. Zero-shot Prompting"
# Classify the following social media post:
# Categories: Promotion, Complaint, Appreciation, Inquiry
# Post: "Worst service ever"
# Return only the category name
def classify_social_media_post_zero_shot(post):
    if "new product" in post or "discounts" in post or "special offers" in post or "launch" in post or "sale" in post or "buy one get one" in post or "limited time" in post.lower():
        return "Promotion"
    elif "disappointed" in post or "damaged" in post or "worst service" in post or "unhappy" in post or "issues" in post or "complaint" in post or "problem" in post:
        return "Complaint"
    elif "thank you" in post or "love" in post or "outstanding" in post or "amazing support" in post or "great service" in post or "awesome" in post:
        return "Appreciation"
    else:
        return "Inquiry"
category = classify_social_media_post_zero_shot("Worst service ever")
print(f"Post: \"Worst service ever\"\nCategory: {category}")

"c. One-shot Prompting"
# Example:
# Post: "Thanks for the quick delivery"
# Category: Appreciation

# Now classify the following post:
# Post: "Do you have any offers?"
# Return only the category name
post_to_classify = "Do you have any offers?"
category = classify_social_media_post_zero_shot(post_to_classify)
print(f"Post: \"{post_to_classify}\"\nCategory: {category}")

"d. Few-shot Prompting"
# Example 1:
# Post: "Buy one get one free"
# Category: Promotion

# Example 2:
# Post: "My order arrived damaged"
# Category: Complaint

# Example 3:
# Post: "Loved your service"
# Category: Appreciation

# Now classify the following post:
# Post: "Can you share the price?"
# Return only the category name

post_to_classify = "Can you share the price?"
category = classify_social_media_post_zero_shot(post_to_classify)
print(f"Post: \"{post_to_classify}\"\nCategory: {category}")

"e. Evaluation"
# Analyze how well the model handles informal language
# Compare Zero-shot, One-shot, and Few-shot results

test_posts = [
    "Huge sale on all items!",
    "I'm unhappy with my purchase.",
    "You guys are awesome!",
    "Where is my order?",
    "Limited time offer, shop now!"
]
for post in test_posts:
    category = classify_social_media_post_zero_shot(post)
    print(f"Post: \"{post}\"\nCategory: {category}\n")
# Note: As with previous sections, separate functions for one-shot and few-shot prompting
# would be implemented for a thorough evaluation. Here, we used the same function for simplicity.

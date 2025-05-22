import re

# Email Validation
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_regex, email):
        return True
    return False

# Phone Number Validation
def validate_phone(phone):
    phone_regex = r'^(\(\d{3}\)\s?|\d{3}[-.\s])\d{3}[-.\s]?\d{4}$'
    if re.match(phone_regex, phone):
        return True
    return False

# URL Validation
def validate_url(url):
    url_regex = r'^https?:\/\/([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}(\/[a-zA-Z0-9\-._~:?#\[\]@!$&\'()*+,;=]*)?$'
    if re.match(url_regex, url):
        return True
    return False

# Credit Card Validation
def validate_credit_card(card_number):
    card_regex = r'^(?:\d{4}[-\s]?){3}\d{4}$'
    if re.match(card_regex, card_number):
        return True
    return False

# Example Usage
sample_email = "user@example.com"
sample_phone = "(123) 456-7890"
sample_url = "https://www.example.com"
sample_card = "1234 5678 9012 3456"

print(f"Email valid: {validate_email(sample_email)}")
print(f"Phone valid: {validate_phone(sample_phone)}")
print(f"URL valid: {validate_url(sample_url)}")
print(f"Credit Card valid: {validate_credit_card(sample_card)}")


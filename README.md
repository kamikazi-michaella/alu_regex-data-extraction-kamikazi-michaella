 Input Validation Library
A simple Python utility for validating common input formats using regular expressions.
Overview
This library provides functions to validate:

## Email addresses
Phone numbers (US format)
URLs
Credit card numbers

## Requirements

Python 3.x
No external dependencies required (uses only built-in re module)

## Installation
Simply copy the validation functions into your project or import the file.
python# To import all validation functions
from input_validator import validate_email, validate_phone, validate_url, validate_credit_card
Usage
python# Email validation
email = "user@example.com"
is_valid = validate_email(email)  # Returns True

# Phone number validation (US format)
phone = "(123) 456-7890"
is_valid = validate_phone(phone)  # Returns True
# Also accepts formats like: 123-456-7890, 123.456.7890

# URL validation
url = "https://www.example.com"
is_valid = validate_url(url)  # Returns True

# Credit card number validation
card = "1234 5678 9012 3456"
is_valid = validate_credit_card(card)  # Returns True
# Also accepts format: 1234-5678-9012-3456
Validation Patterns
Email
Validates standard email formats with:

Username: Letters, numbers, and common special characters
Domain: Letters, numbers, periods, and hyphens
TLD: At least 2 characters

## Phone Number (US format)
Validates formats:

(123) 456-7890
123-456-7890
123.456.7890

## URL
Validates HTTP and HTTPS URLs with:

Protocol (http:// or https://)
Domain with valid TLD
Optional path and query parameters

## Credit Card
Validates format:

16 digits in groups of 4
Separated by spaces or hyphens

## Limitations

Phone validation is primarily for US formats
Credit card validation only checks format, not the Luhn algorithm
URL validation may not catch all edge cases

## License
MIT License license4d this project 
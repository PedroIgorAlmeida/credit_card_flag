import re

def validate_card_number(card_number):
    """Validate if card number is valid using Luhn's algorithm."""
    card_number = card_number.replace(' ', '')
    if not card_number.isdigit():
        return False
    
    digits = [int(d) for d in card_number]
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(divmod(d*2, 10))
    
    return checksum % 10 == 0

def identify_card_flag(card_number):
    """Identify the credit card flag based on the card number."""
    # Clean the input
    card_number = card_number.replace(' ', '')
    card_number = ''.join(filter(str.isdigit, card_number))
    
    # If card number is invalid, return immediately
    if not validate_card_number(card_number):
        return "Invalid card number"
    
    # Card patterns
    card_patterns = {
        "Visa": r'^4\d{12}(\d{3})?$',
        "MasterCard": r'^(5[1-5]\d{14}|222[1-9]\d{12}|22[3-9]\d{13}|2[3-6]\d{14}|27[0-1]\d{13}|2720\d{12})$',
        "American Express": r'^3[47]\d{13}$',
        "Diners Club": r'^3(?:0[0-5]|[68]\d)\d{11}$',
        "Discover": r'^6011\d{12}$',
        "JCB": r'^(2131|1800|35\d{13,14})$',
        "HiperCard": r'^606282\d{10}$',
        "EnRoute": r'^(2014|2149)\d{11}$',
        "Voyager": r'^8699\d{11}$',
        "Aura": r'^50\d{14}$'
    }
    
    # Check each pattern
    for flag, pattern in card_patterns.items():
        if re.match(pattern, card_number):
            return flag
    
    return "Unknown card type"

def main():
    """Main function to run the credit card flag identifier."""
    card_number = input("Enter the credit card number: ").strip()
    result = identify_card_flag(card_number)
    print(f"\nCredit Card Type: {result}")

if __name__ == '__main__':
    main()

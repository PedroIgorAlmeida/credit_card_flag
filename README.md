# Credit Card Flag Identifier

A Python script that identifies credit card flags (brands) based on the card number input. The script validates card numbers using Luhn's algorithm and matches them against known patterns for various credit card brands.

## Supported Card Brands

The script can identify the following credit card brands:
- Visa (prefix 4, length 13 or 16 digits)
- MasterCard (prefixes 51-55 or 2221-2720, length 16 digits)
- American Express (prefixes 34 or 37, length 15 digits)
- Diners Club (prefixes 300-305, 36, or 38-39, length 14 digits)
- Discover (prefixes 6011, 622126-622925, 644-649, or 65, length 16 digits)
- JCB (prefixes 2131, 1800, or 35, length 15 or 16 digits)
- HiperCard (prefix 606282, length 16 digits)
- EnRoute (prefixes 2014 or 2149, length 15 digits)
- Voyager (prefix 8699, length 15 digits)
- Aura (prefix 50, length 16 digits)

## How it Works

The script implements two main functions:

1. **Luhn Algorithm Validation**
   - Validates the card number using the Luhn algorithm (also known as "modulus 10" or "mod 10" algorithm)
   - This is a checksum formula used to validate a variety of identification numbers
   - The algorithm doubles every second digit from right to left and sums all digits
   - If the total modulo 10 is equal to 0, the number is valid

2. **Card Pattern Matching**
   - Uses regular expressions to match card numbers against known patterns for each brand
   - The patterns are ordered to ensure correct identification (most specific patterns are checked first)
   - Each pattern verifies both the prefix and total length of the card number

## Testing

The script has been tested using test card numbers from 4devs.com.br, a reliable source for test data. The tests confirmed that:
- The Luhn algorithm validation works correctly for all card types
- Each card brand is properly identified based on its specific prefix and length requirements
- The script handles both valid and invalid card numbers appropriately

## Usage

1. Run the script:
```bash
python src/credit_card_flag.py
```

2. Enter the credit card number when prompted
3. The program will:
   - Validate the card number using Luhn's algorithm
   - Identify the card brand if valid
   - Return "Invalid card number" if the validation fails
   - Return "Unknown card type" if the card doesn't match any known patterns

## Requirements

- Python 3.x
- Built-in Python libraries (`re` for regex matching)

## Project Structure

```
credit_card_flag/
├── README.md
├── requirements.txt
└── src/
    └── credit_card_flag.py
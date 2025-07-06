# Retail Payment System

## Overview
This Python program allows users to make retail payments by either scanning a QR code or entering a merchant ID. The function validates input data and returns a payment object containing details such as the amount, currency, merchant ID, date, and status. Error handling is included for invalid inputs.

## Features
- Supports payment via QR code scanning or manual entry of merchant details.
- Validates merchant ID, currency, amount, and date format.
- Returns a structured payment object with status tracking.
- Logs messages based on user actions and input validation.

## Payment Object Structure
The function returns a payment object with the following fields:
- `amount`: The amount of the payment.
- `currency`: The currency of the payment.
- `merchant`: The merchant ID.
- `date`: The date of the payment.
- `status`: Payment status ("pending", "approved", "declined").

## Installation & Usage
### Prerequisites
Ensure you have Python installed on your system.

### Running the Program
1. Clone this repository:
   ```sh
   git clone [https://github.com/wtavi00/payment/retail-payment-system.git](https://github.com/wtavi00/Retail-payment-system)
   ```
2. Navigate to the project directory:
   ```sh
   cd Retail-payment-system
   ```
3. Run the script:
   ```sh
   python payment.py
   ```

### Example Usage
#### Payment via QR Code
```python
qr_code_payment = make_payment(None, None, None, None, qr_code_data={
    "amount": 100.5,
    "currency": "USD",
    "merchant": "MERCHANT123",
    "date": "2025-01-20"
})
print(qr_code_payment)
```

#### Payment via Merchant ID
```python
user_payment = make_payment(50, "EUR", "MERCHANT456", "2025-01-21")
print(user_payment)
```

### Error Handling
- If an unrecognized merchant ID is entered, the function logs "Merchant not found" and raises an error.
- If the entered amount is not a number, it logs "Invalid amount" and raises an error.
- If an invalid currency is entered, it logs "Invalid currency" and raises an error.
- If an incorrect date format is entered, it logs "Invalid date" and raises an error.


## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author
Avijit Tarafder

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Issues
If you encounter any issues, feel free to open an issue in the GitHub repository.

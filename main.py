import datetime
from typing import Dict, Union

def make_payment(amount: Union[float, str], currency: str, merchant: str, date: str, qr_code_data: Dict = None):

    # Predefined set of recognized currencies and merchants
    recognized_currencies = {"USD", "EUR", "INR", "GBP", "JPY"}
    recognized_merchants = {"MARCHANT123", "MARCHANT456", "MARCHANT7"}

    def log(message):
        print(message)

    try:
        if qr_code_data:
            # -- QR Code Flow --
            
            # Extract data from QR code
            amount = qr_code_data.get("amount")
            currency = qr_code_data.get("currency")
            merchant = qr_code_data.get("merchant")
            date = qr_code_data.get("date")
            
        else:
            # -- Manual Input Flow --
            
            # Validate user-entered data
            if merchant not in recognized_merchants:
                log("Merchant not found")
                raise ValueError("Merchant not recognized")
                
            # Validate amount
            try:
                amount = float(amount)
            except ValueError:
                log("Invalid amount")
                raise ValueError("Amount must be a number")

            # Validate currency
            if currency not in recognized_currencies:
                log("Invalid currency")
                raise ValueError("Currency not recognized")

            # Validate date format (YYYY-MM-DD)
            try:
                datetime.datetime.strptime(date, "%Y-%m-%d")
            except ValueError:
                log("Invalid date")
                raise ValueError("Invalid date format. Use YYYY-MM-DD")

        # -- Construct the Payment Object --
        payment = {
            "amount": amount,
            "currency": currency,
            "merchant": merchant,
            "date": date,
            "status": "pending"
        }

        # Log payment details
        log(f"Payment of {amount} {currency} to {merchant} on {date} pending")

        # Simulate a resolved promise (returning the payment object)
        return payment

    except ValueError as e:
        # Simulate a rejected promise (raising an error)
        return {"error": str(e)}

# ----------------------------
# Example Usages
# ----------------------------
if __name__ == "__main__":
    # Example 1: Payment via QR code
    qr_code_payment = make_payment(None, None, None, None, qr_code_data={
        "amount": 100.5,
        "currency": "USD",
        "merchant": "MARCHANT123",
        "date": "2025-01-20"
    })
    print(qr_code_payment)

    # Example 2: Payment via merchant ID
    user_payment = make_payment(50, "EUR", "MARCHaNT123", "2025-01-21")
    print(user_payment)

    # Example 3: Invalid merchant
    invalid_merchant = make_payment(50, "EUR", "UNKNOWN_MERCHANT", "2025-01-21")
    print(invalid_merchant)

    # Example 4: Invalid amount
    invalid_amount = make_payment("fifty", "USD", "MERCHANT123", "2025-01-20")
    print(invalid_amount)

    # Example 5: Invalid currency
    invalid_currency = make_payment(50, "XYZ", "MERCHANT123", "2025-01-20")
    print(invalid_currency)

    # Example 6: Invalid date
    invalid_date = make_payment(50, "USD", "MERCHANT123", "2025-20-01")
    print(invalid_date)

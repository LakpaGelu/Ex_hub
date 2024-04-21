import requests


def book_appointment(request):
    # Logic to book appointment

    # Make request to eSewa API
    url = 'https://uat.esewa.com.np/epay/main'
    data = {
        'amt': 100,  # Amount to be paid
        'pdc': 0,  # Payment Duration Code (e.g., for one-time payment)
        'psc': 0,  # Payment Service Charge
        'txAmt': 0,  # Tax Amount
        'tAmt': 100,  # Total Amount
        'pid': '123',  # Unique Payment ID
        'scd': 'epay_payment'  # eSewa Merchant Code
        # Add more required parameters as per eSewa API documentation
    }
    response = requests.post(url, data=data)
    # Process response from eSewa API and redirect user to payment gateway

    return render(request, 'booking_confirmation.html')

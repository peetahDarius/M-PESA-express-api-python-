# +++++++++++++++ IF USING DJANGO ++++++++++++++++++++++++++++
from django.shortcuts import render
# make sure you've registered the url


def incoming(request):
    data = request.get_json()
    print(data)
    if data["Body"]["stkCallback"]["ResultCode"] != 0:

        error_desc = data["Body"]["stkCallback"]["ResultDesc"]
        print(error_desc)
        return error_desc

    elif data["Body"]["stkCallback"]["ResultCode"] == 0:
        amount = data["Body"]["stkCallback"]['CallbackMetadata']['Item'][0]["Value"]
        mpesa_receipt_number = data["Body"]["stkCallback"]['CallbackMetadata']['Item'][1]["Value"]
        transaction_date = str(data["Body"]["stkCallback"]['CallbackMetadata']['Item'][3]["Value"]) if len(
            data["Body"]["stkCallback"]['CallbackMetadata']['Item']) == 5 else \
        data["Body"]["stkCallback"]['CallbackMetadata']['Item'][2]["Value"]
        phone_number = data["Body"]["stkCallback"]['CallbackMetadata']['Item'][4]["Value"] if len(
            data["Body"]["stkCallback"]['CallbackMetadata']['Item']) == 5 else \
        data["Body"]["stkCallback"]['CallbackMetadata']['Item'][3]["Value"]
        print(
            {"amount": amount, "receipt_no": mpesa_receipt_number, "date": transaction_date, "phone_no": phone_number})

    context = {}
    return render(request, "your_html_page.html", context)
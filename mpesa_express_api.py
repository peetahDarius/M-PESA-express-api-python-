from models import MpesaExpress

""" FOR ANY QUESTIONS/HELP, PLEASE FEEL FREE TO CONTACT ME VIA MY EMAIL 'peterdariusk@gmail.com'. """

json_data = {
    "amount": 10,  # The amount of money to be transacted
    "phone_number": '254708374149',  # The phone number of the client/customer
    "party_b": 174379,  # Business short code [will be provided to you by mpesa('174379 is used in the daraja 2.0
    # sandbox').]
    "callback_url": "https://mydomain.com/path",
    # The url that will recieve the mpesa expresss transaction, confirmation.
    "account_reference": "CompanyXLTD",  # The Accounts reference. usually the business's name[paybill/tillNo name].
    "transaction_desc": "Payment of X",  # Transaction description.
    "transaction_type": "CustomerPayBillOnline",
    # CustomerPayBillOnline means using a Paybill and CustomerBuyGoodsOnline means using a Till number
    "short_code": "174379",  # This is the business short code that will be provided to you by mpesa
    "pass_key": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"  # will also be provided to you.
}

""" NB: Please use your own consumer key and consumer secret. The key and secret are provided for free in the safaricom
        daraja.2.0 page.
        In the case of production, Mpesa will provide you with your own consumer key and consumer secret.
        The below consumer key and consumer secret will not work since by the time you are using this code, they will have expired.
"""


def stk_iniitiate():
    consumer_key = 'GVdkmTSajtHRd3665YdQrvbbBisNAGz0ubC'
    consumer_secret = 'VlK6efsGw1Hg745V'
    mpesaobj = MpesaExpress(consumer_key=consumer_key, consumer_secret=consumer_secret)
    response = mpesaobj.initiate_transaction(json_data=json_data)
    return response


# ======================== IF USING FLASK ======================
# make sure you've imported flask.request
# consume Mpesa Express callback
@app.route('/mpesa_callback', methods=['POST'])
def incoming():
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

    return "ok"


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# +++++++++++++++ IF USING DJANGO ++++++++++++++++++++++++++++
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

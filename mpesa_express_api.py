from models import MpesaExpress

json_data = {
    "amount": 10,
    "phone_number": '254708374149',
    "party_b": 174379,
    "callback_url": "https://mydomain.com/path",
    "account_reference": "CompanyXLTD",
    "transaction_desc": "Payment of X",
    "transaction_type": "CustomerPayBillOnline",
    "short_code": "174379",
    "pass_key": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
}

consumer_key = 'MV4kmTSajtHC3665YPQrv9isNAGz0ubC'
consumer_secret = 'VIKVeflGw1HD7a5V'
mpesaobj = MpesaExpress(consumer_key=consumer_key, consumer_secret=consumer_secret)
print(mpesaobj.initiate_transaction(json_data=json_data))
# M-PESA-express-api-python-
Integrating Daraja 2.0 mpesa express api with your system, using python.

if you are using a different python framework than flask or django you can still download the models.py file and import it in your code,
and then initialize the stk push as described in the mpesa_express_api.py file. 

You only have to fill out the json file with the correct details and use your provided consumer key and consumer key and everything else will be taken care of
by the MPesaExpress Model.

Also if you are using the code for production, you will use the second stk_initiate function in the mpesa_express_api.py file. The function sets the Mpesa 
endpoints to the production urls.

If You are using flask oR Django web frameworks, then, feel free to use the code as it is. You just have to import the necessary imports, and everything else
will be taken care of by the functions in their respective files. 

The two files contain webhooks that will receive confirmation responses when a transaction has been successfully.


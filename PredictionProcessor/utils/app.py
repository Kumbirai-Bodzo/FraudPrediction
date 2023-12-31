# from flask import Flask, render_template, request
# import pandas as pd
# from pandas.core.reshape.merge import merge
# from predict import *

# app = Flask(__name__, static_url_path='/static')

# # flask --app sample --debug run
# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     predictions = None
#     testdata = None
#     try:
#         transaction_file = request.files['transaction-file']
#         transaction_data = pd.read_csv(transaction_file)
#         identity_file = request.files['identity-file']
#         identity_data = pd.read_csv(identity_file)
#         testdata = transaction_data.merge(identity_data, how='left', on='TransactionID')
#         del transaction_data, identity_data
#     except:  
#         merged_file = request.files['merged-file']
#         testdata = pd.read_csv(merged_file)
#         del merged_file
#     finally:
#         error = None
#         if(testdata is None):
#             error = 'Files not yet uploaded'
#         else:
#             predictions = predict(testdata)
#         # if predictions is None:
#         #     error = 'Maximum rows error!'
        
#         return render_template('index.html', predictions=predictions,error=error)


# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
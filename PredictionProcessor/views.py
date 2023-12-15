import pandas as pd
from pandas.core.reshape.merge import merge
# from PredictionProcessor.utils import predict
from django.shortcuts import render
import os
from PredictionProcessor.models import Reports
from PredictionProcessor.utils.predict import predict
from pathlib import Path
from django.contrib.auth.decorators import login_required

@login_required(login_url="/auth/login/")
def Index(request):
    print('predict')
    
    predictions = None
    testdata = None
    try:
  
        print(request.FILES['transaction-file'])
        #print(request.FILES['transaction-file'])
        print('hhhhhh')
        transaction_file = request.FILES['transaction-file']
        transaction_data = pd.read_csv(transaction_file)
        print(transaction_data)
        identity_file = request.FILES['identity-file']
        identity_data = pd.read_csv(identity_file)
        testdata = transaction_data.merge(identity_data, how='left', on='TransactionID')
        print(testdata)
        del transaction_data, identity_data
    except Exception as e:
        print(e)
        merged_file = request.FILES['merged-file']
        testdata = pd.read_csv(merged_file)
        del merged_file
    finally:
        error = None
        if(testdata is None):
            error = 'Files not yet uploaded'
        else:
            #* run the prediction
            predictions = predict(testdata)
            batch = Reports.objects.order_by('-batch_no')
            if batch.exists():
                batch_no = batch.first().batch_no+1
                
            else:
                batch_no = 0
            print(predictions)
                

            # saving data to the database for the generation of reports
            for ind in predictions.index:
                print(ind)
                tid = predictions['TransactionID'][ind]
                pred =  predictions['Predictions'][ind]
                print(predictions['TransactionID'][ind], predictions['Predictions'][ind])
                # Predictions
                report = Reports.objects.get_or_create(batch_no=batch_no,transaction_id=tid,probability_fradulent=pred)

        # if predictions is None:
        #     error = 'Maximum rows error!'
        
        # return render_template('index.html', predictions=predictions,error=error)
        return render(request, 'home.html', {'predictions': predictions,'error':error })




@login_required(login_url="/auth/login/")
def get_reports(request):
    reports = []

    try:
        reports = Reports.objects.all()
  
        
      
        return render(request, 'reports.html', {'reports': reports })

    except Exception as e:
        print(e)

    return render(request, 'reports.html', {'reports': reports ,'error':'Ooops error ocurred' })


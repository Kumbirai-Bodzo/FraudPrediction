import pandas as pd
from .make_prediction import *

BASE_DIR = Path(__file__).resolve().parent


def predict(testdata):

    if(testdata is None):
        return None 
    predictions = predict_proba(testdata)
    predictions = pd.DataFrame({
            'TransactionID':testdata['TransactionID'].astype(int),
            'Predictions':np.round(predictions, 5)
    })

    # predictions.to_csv(path+'output.csv')
    
    del testdata
    
    return predictions


# 1. Library imports
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere

# 3. Expose the prediction functionality, make a prediction from the passed
# JSON data and return the predicted Bank Note with the confidence
@app.get('/predict')
def predict_banknote(variance: float, skewness: float, curtosis: float, entropy: float):
   #print(classifier.predict([[variance,skewness,curtosis,entropy]]))
   prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
   print(prediction)
   if(prediction[0] > 0.5):
       prediction="Fake note"
   else:
        prediction="Its a Bank note"
   return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000/docs
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload
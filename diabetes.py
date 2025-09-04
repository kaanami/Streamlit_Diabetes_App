import joblib

def predict_diabetes(input):
    model = joblib.load('saved/DTree_Diabetes.pkl')

    result = model.predict(input)
    return result

    
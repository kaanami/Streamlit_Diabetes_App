import joblib

def predict_diabetes(input):
    model = joblib.load('saved/dGmodel.pkl')

    result = model.predict(input)
    return result

    
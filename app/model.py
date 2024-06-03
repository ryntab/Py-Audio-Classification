import joblib

def load_model():
    return joblib.load('models/classifier.pkl')

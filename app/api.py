from flask import request, jsonify
from app import app
from app.utils import extract_features
from app.model import load_model

model = load_model()

@app.route('/classify', methods=['POST'])
def classify_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        features = extract_features(file_path)
        prediction = model.predict([features])
        
        return jsonify({'prediction': prediction[0]})
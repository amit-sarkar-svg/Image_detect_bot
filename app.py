from flask import Flask, request, jsonify
import os
import cv2
import torch

app = Flask(__name__)

# Ensure the uploads directory exists
os.makedirs('uploads', exist_ok=True)

# Load YOLO model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def generate_description(detected_objects):
    if not detected_objects:
        return "No objects detected."
    return f"Detected objects: {', '.join(detected_objects)}."

@app.route('/')
def home():
    return jsonify({
        'message': 'YOLOv5 Object Detection API',
        'endpoints': {
            '/upload': {
                'method': 'POST',
                'description': 'Upload an image file',
                'parameters': {
                    'image': 'Image file (form-data)'
                }
            },
            '/chat': {
                'method': 'POST', 
                'description': 'Upload an image and get object detection results',
                'parameters': {
                    'image': 'Image file (form-data)'
                }
            }
        },
        'usage': 'Use POST requests with form-data containing an image file'
    })

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        return jsonify({'message': 'Image uploaded successfully', 'filename': file.filename}), 200

@app.route('/chat', methods=['POST'])
def chat():
    if 'image' not in request.files:
        return jsonify({'error': 'No image part'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = os.path.join('uploads', file.filename)
        file.save(filename)
        
        # Process image with YOLO
        img = cv2.imread(filename)
        if img is None:
            return jsonify({'error': 'Could not read image file'}), 400
            
        # Set confidence threshold and run detection
        model.conf = 0.25  # Lower confidence threshold
        results = model(img)
        
        # Get detailed results
        if len(results.pandas().xyxy) > 0:
            df = results.pandas().xyxy[0]
            detected_objects = df['name'].tolist()
            confidences = df['confidence'].tolist()
            
            # Create detailed detection info
            detections = []
            for i, (obj, conf) in enumerate(zip(detected_objects, confidences)):
                detections.append({
                    'object': obj,
                    'confidence': round(conf, 3)
                })
            
            description = generate_description(detected_objects)
            
            return jsonify({
                'message': 'Image processed',
                'detected_objects': detected_objects,
                'description': description,
                'detailed_detections': detections,
                'total_detections': len(detected_objects)
            }), 200
        else:
            return jsonify({
                'message': 'Image processed',
                'detected_objects': [],
                'description': 'No objects detected.',
                'detailed_detections': [],
                'total_detections': 0,
                'note': 'Try with a clearer image or different objects'
            }), 200

if __name__ == '__main__':
    app.run(debug=True) 
# 🤖 Image_detect_bot using YOLOv5 Object Detection API

A Flask-based REST API that uses YOLOv5 for real-time object detection in images. Upload images and get instant detection results with confidence scores.

## ✨ Features

- **Real-time Object Detection** using YOLOv5 model
- **RESTful API** with Flask backend
- **80+ Object Classes** supported (COCO dataset)
- **Confidence Scoring** for each detection
- **Image Upload & Processing** via HTTP requests
- **Detailed JSON Responses** with detection metadata
- **Easy Integration** with any frontend application

## 🎯 What It Can Detect

### Animals
- Cats, dogs, birds, horses, sheep, cows, elephants, bears, zebras, giraffes

### Vehicles
- Cars, trucks, buses, motorcycles, bicycles, airplanes, boats

### Humans & Objects
- People, chairs, tables, beds, couches, laptops, phones, TVs

### Food & Kitchen Items
- Pizza, hot dogs, fruits, cups, plates, forks, knives

### Sports & Recreation
- Baseball bats, tennis rackets, skateboards, surfboards

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Visual Studio C++ Build Tools (Windows)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/amit-sarkar-svg/image_detect_bot.git
cd C:\Users\User\image_detect_bot
```

2. **Create virtual environment**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

## 📡 API Endpoints

### GET `/`
Get API information and available endpoints.

### POST `/upload`
Upload an image file (saves to server).

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `image` (file)

**Response:**
```json
{
  "message": "Image uploaded successfully",
  "filename": "image.jpg"
}
```

### POST `/chat`
Upload an image and get object detection results.

**Request:**
- Method: `POST`
- Content-Type: `multipart/form-data`
- Body: `image` (file)

**Response:**
```json
{
  "message": "Image processed",
  "detected_objects": ["person", "chair", "laptop"],
  "description": "Detected objects: person, chair, laptop.",
  "detailed_detections": [
    {
      "object": "person",
      "confidence": 0.95
    },
    {
      "object": "chair",
      "confidence": 0.87
    },
    {
      "object": "laptop",
      "confidence": 0.92
    }
  ],
  "total_detections": 3
}
```

## 🧪 Testing with Postman

1. **Open Postman**
2. **Create new request:**
   - Method: `POST`
   - URL: `http://127.0.0.1:5000/chat`
3. **Set up body:**
   - Select `form-data`
   - Key: `image`
   - Value: Select `File` and choose an image
4. **Send request**

## 🛠️ Technologies Used

- **Backend:** Flask 2.0.1
- **AI Model:** YOLOv5 (Ultralytics)
- **Computer Vision:** OpenCV 4.11.0
- **Deep Learning:** PyTorch 2.7.1
- **Data Processing:** Pandas, NumPy
- **Image Processing:** Pillow

## 📁 Project Structure

```
yolov5-object-detection-api/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── uploads/              # Directory for uploaded images
└── README.md             # This file
```

## 🔧 Configuration

- **Model:** YOLOv5s (small, fast, accurate)
- **Confidence Threshold:** 0.25 (configurable)
- **Supported Formats:** JPG, PNG, JPEG
- **Max File Size:** Limited by Flask configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5) for the detection model
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [COCO Dataset](https://cocodataset.org/) for object classes

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section below

## 🔍 Troubleshooting

### Common Issues

1. **"No image part" error**
   - Ensure you're using `form-data` in Postman
   - Check that the key is exactly `image`

2. **Model loading errors**
   - Ensure all dependencies are installed
   - Check internet connection for model download

3. **Permission errors**
   - Run as administrator (Windows)
   - Check file permissions

---

**Made with ❤️ using YOLOv5 and Flask** 

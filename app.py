# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model

# # Load the trained model
# model = load_model('models/model2.h5')

# # Define emotion labels corresponding to the dataset mapping
# emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

# # Load Haar cascade for face detection provided by OpenCV
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Start video capture (default camera index 0)
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Convert frame to grayscale for both face detection and model prediction
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

#     for (x, y, w, h) in faces:
#         roi_gray = gray_frame[y:y+h, x:x+w]
#         try:
#             roi_gray = cv2.resize(roi_gray, (48, 48))
#         except Exception as e:
#             continue

#         # Normalize and reshape the region of interest to feed into the model
#         roi = roi_gray.astype('float32') / 255.0
#         roi = np.expand_dims(roi, axis=0)
#         roi = np.expand_dims(roi, axis=-1)

#         # Predict emotion
#         prediction = model.predict(roi)
#         max_index = int(np.argmax(prediction))
#         label = emotion_labels[max_index]

#         # Draw bounding box and emotion label on the frame
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
#                     0.9, (255, 0, 0), 2)

#     # Display the live feed
#     cv2.imshow('Real-Time Emotion Detection', frame)

#     # Exit loop when 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# from flask import Flask, Response
# import cv2
# import numpy as np
# from tensorflow.keras.models import load_model

# app = Flask(__name__)

# # Load the trained model
# model = load_model('models/model2.h5')
# emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# def generate_frames():
#     while True:
#         success, frame = cap.read()
#         if not success:
#             break
        
#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

#         for (x, y, w, h) in faces:
#             roi_gray = gray_frame[y:y+h, x:x+w]
#             roi_gray = cv2.resize(roi_gray, (48, 48))
#             roi = roi_gray.astype('float32') / 255.0
#             roi = np.expand_dims(roi, axis=0)
#             roi = np.expand_dims(roi, axis=-1)

#             prediction = model.predict(roi)
#             label = emotion_labels[np.argmax(prediction)]

#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
#             cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)




from flask import Flask, Response, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Specify allowed origin

model = load_model('models/model2.h5')
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

current_emotion_stats = {}

def generate_frames():
    global current_emotion_stats
    while True:
        success, frame = cap.read()
        if not success:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray_frame[y:y+h, x:x+w]
            roi_gray = cv2.resize(roi_gray, (48, 48))
            roi = roi_gray.astype('float32') / 255.0
            roi = np.expand_dims(roi, axis=0)
            roi = np.expand_dims(roi, axis=-1)

            prediction = model.predict(roi)
            emotion_probs = prediction[0]
            current_emotion_stats = {emotion_labels[i]: emotion_probs[i] * 100 for i in range(len(emotion_labels))}

            label = emotion_labels[np.argmax(prediction)]

            # Displaying only the emotion label in the video feed, without productivity
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(frame, f'{label}', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/emotion_stats')
def emotion_stats():
    # Convert all the values to float to avoid JSON serialization errors
    serializable_stats = {emotion: float(prob) for emotion, prob in current_emotion_stats.items()}
    return jsonify(serializable_stats)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

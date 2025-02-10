import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('models/emotion_model.h5')

# Define emotion labels corresponding to the dataset mapping
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Load Haar cascade for face detection provided by OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture (default camera index 0)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale for both face detection and model prediction
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray_frame[y:y+h, x:x+w]
        try:
            roi_gray = cv2.resize(roi_gray, (48, 48))
        except Exception as e:
            continue

        # Normalize and reshape the region of interest to feed into the model
        roi = roi_gray.astype('float32') / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)

        # Predict emotion
        prediction = model.predict(roi)
        max_index = int(np.argmax(prediction))
        label = emotion_labels[max_index]

        # Draw bounding box and emotion label on the frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (255, 0, 0), 2)

    # Display the live feed
    cv2.imshow('Real-Time Emotion Detection', frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

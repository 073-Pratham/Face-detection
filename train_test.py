import os
import numpy as np
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
from model import create_model
from data_preprocessing import get_data_generators
from sklearn.utils.class_weight import compute_class_weight

# Training parameters
batch_size = 64
epochs = 100

# Use the balanced dataset for training
train_generator, validation_generator = get_data_generators(data_dir='data/balanced', target_size=(48,48), batch_size=batch_size, validation_split=0.2)

# Compute class weights based on the training data
labels = train_generator.classes
unique_classes = np.unique(labels)
class_weights = compute_class_weight('balanced', classes=unique_classes, y=labels)
class_weights = dict(enumerate(class_weights))
print("Computed class weights:", class_weights)

# Build the improved CNN model (variable name "model")
model = create_model(input_shape=(48,48,1), num_classes=7)

# Ensure models folder exists
os.makedirs('models', exist_ok=True)

# Callbacks: save best model, early stopping, and reduce learning rate on plateau
checkpoint = ModelCheckpoint(os.path.join('models', 'model.h5'),
                             monitor='val_accuracy',
                             verbose=1,
                             save_best_only=True,
                             mode='max')
early_stop = EarlyStopping(monitor='val_accuracy', patience=15, verbose=1)
reduce_lr = ReduceLROnPlateau(monitor='val_accuracy', factor=0.5, patience=5, min_lr=1e-6, verbose=1)

# Train the model with class weights
history = model.fit(
    train_generator,
    epochs=epochs,
    validation_data=validation_generator,
    callbacks=[checkpoint, early_stop, reduce_lr],
    class_weight=class_weights
)

# Evaluate the model on validation data
scores = model.evaluate(validation_generator)
print("Validation Loss: {:.4f}, Validation Accuracy: {:.4f}".format(scores[0], scores[1]))

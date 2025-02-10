import os
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from model import create_model
from data_preprocessing import get_data_generators

# Load data generators (20% of data reserved for validation)
train_generator, validation_generator = get_data_generators(data_dir='data/all', target_size=(48,48), batch_size=64, validation_split=0.2)

# Build the CNN model
model = create_model(input_shape=(48,48,1), num_classes=7)

# Callbacks for checkpointing and early stopping
checkpoint = ModelCheckpoint(os.path.join('models', 'emotion_model.h5'),
                             monitor='val_accuracy',
                             verbose=1,
                             save_best_only=True,
                             mode='max')
early_stop = EarlyStopping(monitor='val_accuracy', patience=10, verbose=1)

# Train the model
history = model.fit(
    train_generator,
    epochs=50,
    validation_data=validation_generator,
    callbacks=[checkpoint, early_stop]
)

# Evaluate the model
scores = model.evaluate(validation_generator)
print("Validation Loss: {:.4f}, Validation Accuracy: {:.4f}".format(scores[0], scores[1]))

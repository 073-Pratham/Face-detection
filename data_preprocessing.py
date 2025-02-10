from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_data_generators(data_dir='data/all', target_size=(48, 48), batch_size=64, validation_split=0.2):
    # --- Augmentation and Normalization for Training ---
    train_datagen = ImageDataGenerator(
        rescale=1./255,             # Normalizes pixel values from 0-255 to 0-1
        rotation_range=30,          # Random rotations up to 30 degrees
        width_shift_range=0.1,      # Horizontal shifts up to 10%
        height_shift_range=0.1,     # Vertical shifts up to 10%
        shear_range=0.2,            # Shear transformation
        zoom_range=0.2,             # Random zoom
        horizontal_flip=True,       # Randomly flip images horizontally
        fill_mode='nearest',        # Fill mode for newly created pixels
        validation_split=validation_split
    )

    # --- Only Normalization for Validation ---
    valid_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=validation_split
    )

    # --- Creating Generators from Directory Structure ---
    train_generator = train_datagen.flow_from_directory(
        directory=data_dir,
        target_size=target_size,
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
        shuffle=True
    )

    validation_generator = valid_datagen.flow_from_directory(
        directory=data_dir,
        target_size=target_size,
        color_mode='grayscale',
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

    return train_generator, validation_generator

if __name__ == '__main__':
    train_gen, valid_gen = get_data_generators()
    print("Training classes:", train_gen.class_indices)

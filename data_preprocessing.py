import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

def balance_dataset(source_dir='data/all', target_dir='data/balanced', target_size=(48,48)):
    """
    Balances the dataset by oversampling minority classes using offline augmentation.
    Saves the balanced images in target_dir.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # List emotion folders in source_dir
    emotion_folders = [d for d in os.listdir(source_dir) if os.path.isdir(os.path.join(source_dir, d))]
    
    # Count images per emotion
    counts = {}
    for emotion in emotion_folders:
        emotion_path = os.path.join(source_dir, emotion)
        counts[emotion] = len(os.listdir(emotion_path))
    
    max_count = max(counts.values())
    print("Image counts per emotion (before balancing):", counts)
    print("Target count per emotion:", max_count)
    
    # Copy original images to target_dir
    for emotion in emotion_folders:
        src_emotion_dir = os.path.join(source_dir, emotion)
        tgt_emotion_dir = os.path.join(target_dir, emotion)
        os.makedirs(tgt_emotion_dir, exist_ok=True)
        for fname in os.listdir(src_emotion_dir):
            full_src = os.path.join(src_emotion_dir, fname)
            full_tgt = os.path.join(tgt_emotion_dir, fname)
            if os.path.isfile(full_src):
                img = cv2.imread(full_src, cv2.IMREAD_GRAYSCALE)
                cv2.imwrite(full_tgt, img)
    
    # Set up an augmentation generator (without rescaling)
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.25,
        height_shift_range=0.25,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    # For each emotion folder, generate augmented images until count ~ max_count
    for emotion in emotion_folders:
        tgt_emotion_dir = os.path.join(target_dir, emotion)
        current_count = len(os.listdir(tgt_emotion_dir))
        needed = max_count - current_count
        print(f"For emotion '{emotion}': current count = {current_count}, need to generate {needed} images.")
        if needed <= 0:
            continue
        
        images = os.listdir(tgt_emotion_dir)
        i = 0
        while needed > 0:
            fname = images[i % len(images)]
            img_path = os.path.join(tgt_emotion_dir, fname)
            try:
                image = load_img(img_path, color_mode="grayscale", target_size=target_size)
            except Exception as e:
                print(f"Error loading image {img_path}: {e}")
                i += 1
                continue
            x = img_to_array(image)
            x = x.reshape((1,) + x.shape)  # shape: (1, 48, 48, 1)
            # Generate one augmented image
            aug_iter = datagen.flow(x, batch_size=1)
            aug_image = next(aug_iter)[0].astype('uint8')
            new_fname = f"aug_{i}_{fname}"
            new_img_path = os.path.join(tgt_emotion_dir, new_fname)
            cv2.imwrite(new_img_path, aug_image)
            needed -= 1
            i += 1

def get_data_generators(data_dir='data/balanced', target_size=(48, 48), batch_size=64, validation_split=0.2):
    """
    Creates training and validation generators using the balanced dataset.
    Applies on-the-fly augmentation (for training) and normalization for both.
    """
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.25,
        height_shift_range=0.25,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=validation_split
    )
    
    valid_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=validation_split
    )
    
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
    # First, balance the dataset (this may take several minutes depending on your data)
    balance_dataset()
    # Then, test the generators
    train_gen, valid_gen = get_data_generators()
    print("Balanced training classes:", train_gen.class_indices)

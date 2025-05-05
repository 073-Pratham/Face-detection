from tensorflow.keras.models import load_model
from model import create_model  # Assuming this is your function

# Step 1: Recreate the architecture
model = create_model(input_shape=(48, 48, 1), num_classes=7)

# Step 2: Load the trained weights into the architecture
model.load_weights("models/model2.h5")

# Step 3: Save the full model (architecture + weights)
model.save("models/full_model.h5")

print("Full model saved successfully.")

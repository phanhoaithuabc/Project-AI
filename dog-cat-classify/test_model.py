import os
import pandas as pd
import numpy as np
from keras import models
from keras.preprocessing.image import ImageDataGenerator, load_img
import architecture_model
import matplotlib.pyplot as plt

IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
batch_size=15

test_filenames = os.listdir("data/test")
test_df = pd.DataFrame({
    'filename': test_filenames
})
nb_samples = test_df.shape[0]

# Create Testing Generator
test_gen = ImageDataGenerator(rescale=1./255)
test_generator = test_gen.flow_from_dataframe(
    test_df, 
    "data/test", 
    x_col='filename',
    y_col=None,
    class_mode=None,
    target_size=IMAGE_SIZE,
    batch_size=batch_size,
    shuffle=False
)

model = models.load_model("model.h5")
result = model.predict_generator(test_generator, 
                steps=np.ceil(nb_samples/batch_size))

test_df['category'] = np.argmax(result, axis=-1)

test_df['category'] = test_df['category'].replace({ 1: 'dog', 0: 'cat' })

print(test_df)
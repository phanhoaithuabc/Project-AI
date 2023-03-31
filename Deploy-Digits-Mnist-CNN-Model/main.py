import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

# Hyperparameters
num_classes = 10
batch_size = 128
epochs = 12

# Image Resolution
img_rows, img_cols = 28, 28
# Loading the data.
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preparing the data
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

# Training the model
model.fix(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,verbose=1,
          validation_data=(x_test, y_test))

# Evaluateing the Predictions on the Model
score = model.evaluate(x_test, y_test,verbose=0)
print('test loss: ',score[0])
print('test accuracy: ', score[1])

# Save the model for Future Inference
model_json = model.to_json()
with open("model.json","w")as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")

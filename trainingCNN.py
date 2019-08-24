import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.layers.convolutional import Conv2D
from keras.layers import MaxPooling2D
import numpy as np
import cv2
#from parser import load_data
from keras_preprocessing.image import ImageDataGenerator

#traingen=train_datagen.flow_from_directory(directory=r"C:/train",target_size=(250,250),color_mode="rgb",batch_size=5,class_mode="binary",shuffle=True,seed=3)
#validgen=valid_datagen.flow_from_directory(directory=r"C:/test",target_size=(250,250),color_mode="rgb",batch_size=1,class_mode=None,shuffle=False,seed=3)

#training_data = load_data('C:/hand_train')
#validation_data = load_data('C:/hand_test')

model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),activation='relu',input_shape=(150, 150,3)))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'C:/Train2',  # this is the target directory
        target_size=(150, 150),  # all images will be resized to 150x150
        batch_size=5,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        'C:/Test',
        target_size=(150, 150),
        batch_size=5,
        class_mode='binary')

model.fit_generator(
        train_generator,
        steps_per_epoch=50 ,
        epochs=20,
        validation_data=validation_generator,
        validation_steps=60)
model.save('D:/retrain.h5')

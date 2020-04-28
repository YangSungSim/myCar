from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import *
#import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Activation, Dropout,Flattern,Dense
from keras.callbacks import ModelCheckpoint
from keras.layers.normalization import BatchNormalization

# Create your views here.
def index(request):
    photo = request.FILES.get('fileInput')

    model = Photo(photo=photo)

    model.save()

    #신경망으로 모델 분석하기
    def keras_model():
        model = Sequential()
        model.add(Conv2D(16,(3,3),padding='same',use_bias=False,input_shape=(128,128,3)))
        model.add(BatchNormalization(axis=3,scale=False))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(4,4),strides=(4,4),padding='same'))
        model.add(Dropout(0.2))

        model.add(Conv2D(32,(3,3),padding='same',use_bias=False))
        model.add(BatchNormalization(axis=3,scale=False))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(4, 4), strides=(4, 4), padding='same'))
        model.add(Dropout(0.2))

        model.add(Conv2D(64,(3,3),padding='same',use_bias=False))
        model.add(BatchNormalization(axis=3,scale=False))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(4, 4), strides=(4, 4), padding='same'))
        model.add(Dropout(0.2))

        model.add(Dense(512,activation='relu'))
        model.add(166,activation='softmax')
        model.summary()
        return model
    keras_model1 = keras_model()
    keras_model1.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    keras_model1.fit(train_data,train_label,batch_size=10,validation_data=[])
    pred = keras_model1.predict(test_data) #고객이 집어넣은 사진
    answer = np.argmax(pred,axis=1) #고객의 최종 차종 모델



    return render(request,'photo/car_design.html')
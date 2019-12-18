from keras.datasets import mnist

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

print(X_train[0])
print(Y_test[0])
print(X_train.shape)
print(X_test.shape)
print(Y_train.shape)
print(Y_test.shape)

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint, EarlyStopping
import numpy as np
import os
import tensorflow as tf

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255 #float32로 바꿔줌 (60000,28,28,1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype('float32') / 255 #float32로 바꿔줌 (60000,28,28,1)
print(X_train.shape)
print(X_test.shape)
# 원-핫 인코딩은 단어 집합의 크기를 벡터의 차원으로 하고, 표현하고 싶은 단어의 인덱스에 1의 값을 부여하고,
#  다른 인덱스에는 0을 부여하는 단어의 벡터 표현 방식입니다. 
# 이렇게 표현된 벡터를 원-핫 벡터(One-hot vector)라고 합니다.

# (1) 각 단어에 고유한 인덱스를 부여합니다. (정수 인코딩)
# (2) 표현하고 싶은 단어의 인덱스의 위치에 1을 부여하고, 다른 단어의 인덱스의 위치에는 0을 부여합니다.
Y_train = np_utils.to_categorical(Y_train)
Y_test = np_utils.to_categorical(Y_test)
print(Y_train[0])
print(Y_train.shape)
print(Y_test.shape)

#컨볼루션 신경망의 설정
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), input_shape=(28, 28, 1), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=2))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax')) # 분류모델은 무조건 softmax 

model.summary()

model.compile(loss='categorical_crossentropy', 
              optimizer='adam',
              metrics=['accuracy'])

early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10)

# 모델의 실행
history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test),
                    epochs=2, batch_size=200, verbose=1,
                    callbacks=[early_stopping_callback]) #,checkpointer

# 테스트 정확도 출력
print("\n Test Accuracy: %.4f" % (model.evaluate(X_test, Y_test)[1]))
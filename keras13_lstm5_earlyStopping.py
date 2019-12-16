from numpy import array
from keras.models import Sequential, Model
from keras.layers import Dense, LSTM, Input

#1 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7],
           [6,7,8], [7,8,9], [8,9,10], [9,10,11], [10,11,12],
           [20,30,40], [30,40,50], [40,50,60]])
y = array([4,5,6,7,8,9,10,11,12,13,50,60,70])
print(x)
x1 = x[:10]
x2 = x[10:]
y1 = y[:10]
y2 = y[10:]

print('x1 : ', x1)
print('x2 : ', x2)
print('y1 : ', y1)
print('y2 : ', y2)

print("x1.shape : ", x1.shape)
print("x2.shape : ", x2.shape)
print("y1.shape : ", y1.shape)
print("y2.shape : ", y2.shape)
x1 = x1.reshape((x1.shape[0], x1.shape[1], 1))
x2 = x2.reshape((x2.shape[0], x2.shape[1], 1))
y1 = y1.reshape((y1.shape[0], 1))
y2 = y2.reshape((y2.shape[0], 1))
print("x1.shape : ", x1.shape)
print("x2.shape : ", x2.shape)
print("y1.shape : ", y1.shape)
print("y2.shape : ", y2.shape)   

#2. 모델 구성
input1 = Input(shape=(3,1))
lstm = LSTM(10)(input1)
dense1 = Dense(5, activation='relu')(lstm)
dense2 = Dense(3)(dense1)
dense3 = Dense(4)(dense2)
middle1 = Dense(3)(dense3)

input2 = Input(shape=(1,))
lstm = LSTM(10)(input2)
xx = Dense(5, activation='relu')(lstm)
xx = Dense(3)(xx)
middle2 = Dense(3)(xx)

from keras.layers.merge import concatenate
merge1 = concatenate([middle1, middle2])

output1 = Dense(30)(merge1)
output1 = Dense(13)(output1)
output1 = Dense(3)(output1)

output2 = Dense(15)(merge1)
output2 = Dense(32)(output2)
output2 = Dense(3)(output2)



model = Model(inputs = [input1, input2], outputs = [output1, output2])

#model.summary()

#3. 실행
model.compile(optimizer='adam', loss='mse')

from keras.callbacks import EarlyStopping

early_stopping = EarlyStopping(monitor='loss', patience=100, mode='auto')
#model.fit(x, y, epochs=250, verbose=2)
model.fit([x1, x2], [y1, y2], epochs=1000, callbacks=[early_stopping])


x_input = array([25,35,45]) # 1, 3, ???
x_input = x_input.reshape((1,3,1))

yhat = model.predict(x_input)
print(yhat)

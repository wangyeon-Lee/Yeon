from numpy import array 
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7],
           [6,7,8], [7,8,9], [8,9,10], [9,10,11], [10,11,12],
           [20000,30000,40000], [30000,40000,50000], [40000,50000,60000], [100,200,300]])
y = array([4,5,6,7,8,9,10,11,12,13,50000,60000,70000,400])

from sklearn.preprocessing import MinMaxScaler, StandardScaler
#scaler = MinMaxScaler()
scaler = StandardScaler()
scaler.fit(x)
x = scaler.transform(x)  #evaluate, predict

# train과 predict로 나눌것
# train = 1번째부터 13번째까지
# predict = 14번째.
x_train = x[:13]
x_predict = x[13:]
y_train = y[:13]
y_predict = y[13:]
print(x_train)
print()
print(x_predict)

print("x.shape : ", x.shape)  # (13,3)
print("y.shape : ", y.shape)  # (13, )
print(x)
#x = x.reshape((x.shape[0], x.shape[1], 1))
#print(x)
#print("x.shape : ", x.shape)       #(4, 3, 1)

#2. 모델 구성
model = Sequential()
model.add(Dense(20, activation='relu', input_shape=(3,)))  # 3, 1  3= 컬럼 1=1개씩 잘라서작업
model.add(Dense(18, activation='relu',))
model.add(Dense(16))
model.add(Dense(13))
model.add(Dense(10))
model.add(Dense(7))
model.add(Dense(5))
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(1))

model.summary()

#3. 실행

model.compile(loss='mse', optimizer='adam', metrics=['mse'])
model.fit(x, y, epochs=100, batch_size=1, verbose=2)

import numpy as np
# 평가 예측
# x_input = array([25,35,45]) # 1, 3, ???
# x_input = np.transpose(x_input)
# # x_input = scaler.transform(x_input)

#print(x_input.shape)
#x_input = x_input.reshape((1,3,1))

yhat = model.predict(x_predict, verbose=2)
print(yhat)

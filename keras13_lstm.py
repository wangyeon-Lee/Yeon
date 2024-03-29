from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
x = array([[1,2,3], [2,3,4], [3,4,5], [4,5,6]])
y = array([4,5,6,7])
print(x)
print("x.shape : ", x.shape)    #(4, 3)
print("y.shape : ", y.shape)    #(4, )
'''
 x  y
123 4
234 5
345 6
456 7
'''
x = x.reshape((x.shape[0], x.shape[1], 1)) # x 배열1, 2번째 뒤에 1추가
print(x)
print("x.shape : ", x.shape)       #(4, 3, 1)

#2. 모델 구성
model = Sequential()
model.add(LSTM(10, activation='relu', input_shape=(3,1)))  # 3, 1  3= 컬럼 1=1개씩 잘라서작업
model.add(Dense(15))
model.add(Dense(13))
model.add(Dense(11))
model.add(Dense(10))
model.add(Dense(8))
model.add(Dense(7))
model.add(Dense(7))
model.add(Dense(5))
model.add(Dense(3))
model.add(Dense(1))
# model.summary()

#3. 실행
model.compile(optimizer='adam', loss='mse')
model.fit(x, y, epochs=500, batch_size=1)

x_input = array([6,7,8]) # 1, 3, ???
x_input = x_input.reshape((1,3,1)) # 1,3,1로 재배열

yhat = model.predict(x_input)
print(yhat)

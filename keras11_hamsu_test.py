# 1. 데이터
import numpy as np	#numpy를 np로 줄인다

x = np.array(range(1,101))
y = np.array(range(1,101))
print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=50, train_size=0.6, test_size=0.4, shuffle=False
)
x_val, x_test, y_val, y_test = train_test_split(
    x_test, y_test, random_state=50, test_size=0.5, shuffle=False
) # 6:2:2

# 2. 모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
# model = Sequential()

input1 = Input(shape=(1,))
dense1 = Dense(11, activation='relu')(input1)
dense2 = Dense(10)(dense1)
dense3 = Dense(12)(dense2)
dense4 = Dense(13)(dense3)
dense5 = Dense(14)(dense4)
dense6 = Dense(15)(dense5)
dense7 = Dense(16)(dense6)
dense8 = Dense(17)(dense7)
dense9 = Dense(18)(dense8)
dense10 = Dense(19)(dense9)
dense11 = Dense(18)(dense10)
output1 = Dense(1)(dense11)

model = Model(inputs = input1, outputs = output1)
model.summary()

# 3. 훈련
model.compile(loss='mse', optimizer='adam', 
            #  metrics=['accuracy'])
             metrics=['mse'])
model.fit(x_train, y_train, epochs=150, batch_size=1, validation_data=(x_val, y_val))	#fit = 기계를 트레이닝 시킴, 

# 4. 평가 예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1) # a[0], a[1] 
print('mse: ', mse) #1.0
print('loss: ', loss)

y_predict = model.predict(x_test)
print(y_predict)

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(y_test, y_predict ):
    return np.sqrt(mean_squared_error(y_test, y_predict))
print("RMSE : ", RMSE(y_test, y_predict))


# R2 구하기
from sklearn.metrics import r2_score
r2_y_predict = r2_score(y_test, y_predict)
print("R2 : ", r2_y_predict)

#레이어를 10개 이상 늘리시오.
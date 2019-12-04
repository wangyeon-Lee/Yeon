from keras.models import Sequential
from keras.layers import Dense

import numpy as np	#numpy를 np로 줄인다
x_train = np.array([1,2,3,4,5,6,7,8,9,10])
y_train = np.array([1,2,3,4,5,6,7,8,9,10])
x_test = np.array([11,12,13,14,15,16,17,18,19,20])
y_test = np.array([11,12,13,14,15,16,17,18,19,20])
# x_predict = np.array([21,22,23,24,25])
model = Sequential()
# model.add(Dense(30, input_dim=1, activation='relu'))
model.add(Dense(511, input_shape=(1, ), activation='relu'))
model.add(Dense(132))
model.add(Dense(568))
model.add(Dense(211))
model.add(Dense(511))
model.add(Dense(111))
model.add(Dense(521))
model.add(Dense(211))
model.add(Dense(611))
model.add(Dense(411))
model.add(Dense(211))
model.add(Dense(511))
model.add(Dense(1111))
model.add(Dense(311))
model.add(Dense(510))
model.add(Dense(1))



model.summary()

model.compile(loss='mse', optimizer='adam', 
            #  metrics=['accuracy'])
             metrics=['mse'])
model.fit(x_train, y_train, epochs=150, batch_size=1)	#fit = 기계를 트레이닝 시킴, 

loss, mse = model.evaluate(x_test, y_test, batch_size=1) # a[0], a[1] 
print('mse: ', mse) #1.0
print('loss: ', loss) #1.997137815124006e-05

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

# 문제 1. R2를 0.5이하로 줄이시오.
# 레이어는 인풋과 아웃풋 포함 5개 이상, 노드는 각 레이어당 5개이상
# batch_size = 1
# epochs = 100이상
'''
mse:  49806420.0
loss:  49806418.8
[[4010.9724]
 [4651.1963]
 [5276.6187]
 [5901.118 ]
 [6526.435 ]
 [7153.204 ]
 [7780.076 ]
 [8406.942 ]
 [9033.805 ]
 [9660.193 ]]
RMSE :  7057.364731421059
R2 :  -6037138.024521921

mse:  1160.7525634765625
loss:  1160.7524631500244
[[17.133482]
 [19.862036]
 [24.356543]
 [30.702276]
 [38.321606]
 [47.89237 ]
 [55.853573]
 [63.59287 ]
 [70.5544  ]
 [77.38452 ]]
RMSE :  34.06983676428384
R2 :  -139.69742753272084
'''

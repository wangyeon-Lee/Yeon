# 1. 데이터
import numpy as np	#numpy를 np로 줄인다

x = np.array([range(100), range(311,411), range(100)])


y1 = np.array([range(100,200), range(311,411), range(100,200)])
y2 = np.array([range(501,601), range(711,811), range(100)])



x = np.transpose(x)
y1 = np.transpose(y1)
y2 = np.transpose(y2)

print(x.shape) # (100, 3)
print(y1.shape) # (100, 3)
print(y2.shape) # (100, 3)



from sklearn.model_selection import train_test_split
x_train, x_test, y1_train, y1_test = train_test_split(
    x, y1, random_state=50, train_size=0.6, test_size=0.4, shuffle=False
)
x_val, x_test, y1_val, y1_test = train_test_split(
    x_test, y1_test, random_state=50, test_size=0.5, shuffle=False
)

y2_train, y2_test = train_test_split(
    y2, random_state=50, train_size=0.6, test_size=0.4, shuffle=False
)
y2_val, y2_test = train_test_split(
    y2_test, random_state=50, test_size=0.5, shuffle=False
)




# 2. 모델구성
from keras.models import Sequential, Model
from keras.layers import Dense, Input
# model = Sequential()

input1 = Input(shape=(3,))
dense1 = Dense(5, activation='relu')(input1)
dense2 = Dense(3)(dense1)
dense3 = Dense(4)(dense2)
middle1 = Dense(3)(dense3)


from keras.layers.merge import concatenate


output1 = Dense(7)(middle1)
output1 = Dense(5)(output1)
output1 = Dense(3)(output1)

output2 = Dense(7)(middle1)
output2 = Dense(5)(output2)
output2 = Dense(3)(output2)



model = Model(inputs = input1, outputs = [output1, output2])
model.summary()

# 3. 훈련
model.compile(loss='mse', optimizer='adam', 
            #  metrics=['accuracy'])
             metrics=['mse'])
model.fit(x_train, [y1_train, y2_train], epochs=150, batch_size=1, validation_data=(x_val, [y1_val, y2_val]))	#fit = 기계를 트레이닝 시킴, 

# 4. 평가 예측
mse = model.evaluate(x_test, [y1_test, y2_test], batch_size=1) # a[0], a[1] 
print('mse: ', mse[0]) #1.0
print('mse: ', mse[1]) #1.0
print('mse: ', mse[2]) #1.0
print('mse: ', mse[3]) #1.0
print('mse: ', mse[4]) #1.0



y1_predict, y2_predict = model.predict(x_test)
print(y1_predict)
print()
print(y2_predict)
print()

# RMSE 구하기
from sklearn.metrics import mean_squared_error
def RMSE(xxx, yyy):
    return np.sqrt(mean_squared_error(xxx, yyy))
RMSE1 = RMSE(y1_test, y1_predict)
RMSE2 = RMSE(y2_test, y2_predict)

print("RMSE1 : ", RMSE1)
print("RMSE2 : ", RMSE2)

print("RMSE : ", (RMSE1 + RMSE2)/2)

# R2 구하기
from sklearn.metrics import r2_score
r2_y1_predict = r2_score(y1_test, y1_predict)
r2_y2_predict = r2_score(y2_test, y2_predict)


print("R2_1 : ", r2_y1_predict)
print("R2_2 : ", r2_y2_predict)

print("R2 : ", (r2_y1_predict + r2_y2_predict)/2)

#레이어를 10개 이상 늘리시오.

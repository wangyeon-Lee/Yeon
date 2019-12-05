# 1. 데이터
import numpy as np	#numpy를 np로 줄인다

x = np.array([range(1,101), range(101,201)])
y = np.array([range(201,301)])
# print(x)

print(x.shape)

x = np.transpose(x) # 행 열 위치 바꿈
y = np.transpose(y) # 행 열 위치 바꿈
print(x.shape)



from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, random_state=50, train_size=0.6, test_size=0.4, shuffle=False
)
x_val, x_test, y_val, y_test = train_test_split(
    x_test, y_test, random_state=50, test_size=0.5, shuffle=False
) # 6:2:2

# 2. 모델구성
from keras.models import Sequential
from keras.layers import Dense
model = Sequential()

# model.add(Dense(5, input_dim=1, activation='relu'))
model.add(Dense(5, input_shape=(2, ), activation='relu'))
model.add(Dense(4))
model.add(Dense(3))
model.add(Dense(2))
model.add(Dense(1))

model.summary()

# 3. 훈련
model.compile(loss='mse', optimizer='adam', 
            #  metrics=['accuracy'])
             metrics=['mse'])
model.fit(x_train, y_train, epochs=100, batch_size=1, validation_data=(x_val, y_val))	#fit = 기계를 트레이닝 시킴, 

# 4. 평가 예측
loss, mse = model.evaluate(x_test, y_test, batch_size=1) # a[0], a[1] 
print('mse: ', mse) #1.0
print('loss: ', loss)

#aaa = np.array([[101,102,103],[201,202,203]])
#aaa = np.transpose(aaa) # 행 열 위치 바꿈
#y_predict = model.predict(aaa)
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



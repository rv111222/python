from sklearn.linear_model import LinearRegression
import random
model = LinearRegression()
hours = [[1],[2],[3],[4],[5]]
marks = [35,40,50,60,75]
model.fit(hours,marks)
print(model.predict([[2]]))
print(model.predict([[15]]))

days = ['Monday','Tuesday','Wednesday']
probability = [0.6,0.3,0.1]
print("i am taking tea at",random.choices(days,probability))


import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Загрузить данные из файла
x1 = []
y1 = []
x = []
y = []
with open("lab1-09.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
#Проходим покаждой строке в объекте reader
    for line in csv_reader:
        x0, y0 = line
        x1.append (x0)
        y1.append (y0)

        x= [float(x) for x in list(x1)]
        y= [float(y) for y in list(y1)]

        #print (x, y)


#Визуальное представление данных
fix, ax = plt.subplots() #Возвращает 2 объекта. fix - Canva рисования. ax - Система координат.
ax.scatter (x, y, 1) #Отрисовка графика.(x и y - вектора). scatter - диаграмма рассеивания.
ax.axes.get_xaxis().set_visible (False)
ax.axes.get_yaxis().set_visible (False)
#ax.grid()
plt.title ('Visual representation of data')
plt.show ()

#Разбиение данных на обучающую и тестовую выборки
x_train, x_test, y_train, y_test = train_test_split (x, y, test_size=0.3)
print ('Разбиение успешно!')
#print (x_train)
#print ( y_train)
#Модель регрессии - линейная

x_train= np.reshape(x_train, (-1, 1))
x_test= np.reshape(x_test, (-1, 1))

#Learning. Next, we need to create an instance of the Linear Regression Python object. We will assign this to a variable called model. Here is the code for this:

model = LinearRegression ()
model.fit (x_train, y_train)

#Our model has now been trained. You can examine each of the model’s coefficients using the following statement:

print(model.coef_)

#Similarly, here is how you can see the intercept of the regression equation:

print (model.intercept_)

#Greate future's data
predictions = model.predict (x_test)

#Проверrf качества полученной модели на тестовых данных.

fix, ax = plt.subplots() #Возвращает 2 объекта. fix - Canva рисования. ax - Система координат.
ax.scatter (x_test, y_test, 5)
ax.scatter (x_test, predictions, 1)
plt.title("New scatterplot - TEST OF Predictions")
plt.show()

plt.hist(y_test - predictions)
plt.title("Histogram of the residuals from our machine learning model")
plt.show()

#Можно заметить, что остатки от нашей модели машинного обучения распределены с отклонениями.
#Это указывает на то, что был выбран не подходящий тип модели (в данном случае линейная регрессия) для составления прогнозов на основе исходного набора данных.

#model.score () #Считает среднеквадратичное отклонение.


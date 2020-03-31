import numpy as np
#Girdi dizisiniz oluşturulması.
input_arr = np.array([[1,0], [0,1]], np.double)
#Ağırlık dizisinin oluşturulması.
weight_arr = np.array([[1],[2]], np.double)
#net dizisinin oluşturulması.
net=np.array([1,0], np.double)
#Sınıfları içeren hedef dizisinin oluşturulması.
target = np.array([1,0], np.double)
learning_rate=0.5
threshold = -1
weight0_n = 0
weight1_n = 0

while True:
    net[0] = input_arr[0].dot(weight_arr)
    net[1] = input_arr[1].dot(weight_arr)
    for j in range(len(input_arr)):
        if net[j] > threshold:
            if target[j] != 1:
                weight0_n = weight_arr[0] - learning_rate*input_arr[j][0]
                weight1_n = weight_arr[1] - learning_rate*input_arr[j][1]
        elif net[j] <= threshold:
            if target[j] != 0:
                weight0_n = weight_arr[0] + learning_rate*input_arr[j][0]
                weight1_n = weight_arr[1] + learning_rate*input_arr[j][1]
    #eğer eski ağırlıklar yenilerine eşitse eğitim sonlanıyor.
    if weight0_n == weight_arr[0] and weight1_n == weight_arr[1]:
        net[0] = input_arr[0].dot(weight_arr)
        net[1] = input_arr[1].dot(weight_arr)
        for j in range(len(input_arr)):
            if net[j] > threshold and target[j] == 1:
                print("Test")
                print("Örnek 1 için Net " + str(net[j]))
                print("1. örnek başarılı")
            elif net[j] <= threshold and target[j] == 0:
                print("Örnek 1 için Net " + str(net[j]))
                print("2. örnek başarılı")
        print("Ağırlıklar")
        print(weight_arr)
        break
    else:
         weight_arr[0] = weight0_n 
         weight_arr[1] = weight1_n 

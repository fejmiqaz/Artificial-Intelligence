import os

from sklearn.preprocessing import MinMaxScaler

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.naive_bayes import GaussianNB

dataset = [
    [14.23, 1.71, 2.43, 15.6, 127, 2.8, 3.06, .28, 2.29, 5.64, 1.04, 3.92, 1065, 0],
    [13.2, 1.78, 2.14, 11.2, 100, 2.65, 2.76, .26, 1.28, 4.38, 1.05, 3.4, 1050, 0],
    [13.16, 2.36, 2.67, 18.6, 101, 2.8, 3.24, .3, 2.81, 5.68, 1.03, 3.17, 1185, 0],
    [14.37, 1.95, 2.5, 16.8, 113, 3.85, 3.49, .24, 2.18, 7.8, .86, 3.45, 1480, 0],
    [13.24, 2.59, 2.87, 21, 118, 2.8, 2.69, .39, 1.82, 4.32, 1.04, 2.93, 735, 0],
    [14.2, 1.76, 2.45, 15.2, 112, 3.27, 3.39, .34, 1.97, 6.75, 1.05, 2.85, 1450, 0],
    [14.39, 1.87, 2.45, 14.6, 96, 2.5, 2.52, .3, 1.98, 5.25, 1.02, 3.58, 1290, 0],
    [14.06, 2.15, 2.61, 17.6, 121, 2.6, 2.51, .31, 1.25, 5.05, 1.06, 3.58, 1295, 0],
    [14.83, 1.64, 2.17, 14, 97, 2.8, 2.98, .29, 1.98, 5.2, 1.08, 2.85, 1045, 0],
    [13.86, 1.35, 2.27, 16, 98, 2.98, 3.15, .22, 1.85, 7.22, 1.01, 3.55, 1045, 0],
    [14.1, 2.16, 2.3, 18, 105, 2.95, 3.32, .22, 2.38, 5.75, 1.25, 3.17, 1510, 0],
    [14.12, 1.48, 2.32, 16.8, 95, 2.2, 2.43, .26, 1.57, 5, 1.17, 2.82, 1280, 0],
    [13.75, 1.73, 2.41, 16, 89, 2.6, 2.76, .29, 1.81, 5.6, 1.15, 2.9, 1320, 0],
    [14.75, 1.73, 2.39, 11.4, 91, 3.1, 3.69, .43, 2.81, 5.4, 1.25, 2.73, 1150, 0],
    [14.38, 1.87, 2.38, 12, 102, 3.3, 3.64, .29, 2.96, 7.5, 1.2, 3, 1547, 0],
    [13.63, 1.81, 2.7, 17.2, 112, 2.85, 2.91, .3, 1.46, 7.3, 1.28, 2.88, 1310, 0],
    [14.3, 1.92, 2.72, 20, 120, 2.8, 3.14, .33, 1.97, 6.2, 1.07, 2.65, 1280, 0],
    [13.83, 1.57, 2.62, 20, 115, 2.95, 3.4, .4, 1.72, 6.6, 1.13, 2.57, 1130, 0],
    [14.19, 1.59, 2.48, 16.5, 108, 3.3, 3.93, .32, 1.86, 8.7, 1.23, 2.82, 1680, 0],
    [13.64, 3.1, 2.56, 15.2, 116, 2.7, 3.03, .17, 1.66, 5.1, .96, 3.36, 845, 0],
    [12.37, .94, 1.36, 10.6, 88, 1.98, .57, .28, .42, 1.95, 1.05, 1.82, 520, 1],
    [12.33, 1.1, 2.28, 16, 101, 2.05, 1.09, .63, .41, 3.27, 1.25, 1.67, 680, 1],
    [12.64, 1.36, 2.02, 16.8, 100, 2.02, 1.41, .53, .62, 5.75, .98, 1.59, 450, 1],
    [13.67, 1.25, 1.92, 18, 94, 2.1, 1.79, .32, .73, 3.8, 1.23, 2.46, 630, 1],
    [12.37, 1.13, 2.16, 19, 87, 3.5, 3.1, .19, 1.87, 4.45, 1.22, 2.87, 420, 1],
    [12.17, 1.45, 2.53, 19, 104, 1.89, 1.75, .45, 1.03, 2.95, 1.45, 2.23, 355, 1],
    [12.37, 1.21, 2.56, 18.1, 98, 2.42, 2.65, .37, 2.08, 4.6, 1.19, 2.3, 678, 1],
    [13.11, 1.01, 1.7, 15, 78, 2.98, 3.18, .26, 2.28, 5.3, 1.12, 3.18, 502, 1],
    [12.37, 1.17, 1.92, 19.6, 78, 2.11, 2, .27, 1.04, 4.68, 1.12, 3.48, 510, 1],
    [13.34, .94, 2.36, 17, 110, 2.53, 1.3, .55, .42, 3.17, 1.02, 1.93, 750, 1],
    [12.21, 1.19, 1.75, 16.8, 151, 1.85, 1.28, .14, 2.5, 2.85, 1.28, 3.07, 718, 1],
    [12.29, 1.61, 2.21, 20.4, 103, 1.1, 1.02, .37, 1.46, 3.05, .906, 1.82, 870, 1],
    [13.86, 1.51, 2.67, 25, 86, 2.95, 2.86, .21, 1.87, 3.38, 1.36, 3.16, 410, 1],
    [13.49, 1.66, 2.24, 24, 87, 1.88, 1.84, .27, 1.03, 3.74, .98, 2.78, 472, 1],
    [12.99, 1.67, 2.6, 30, 139, 3.3, 2.89, .21, 1.96, 3.35, 1.31, 3.5, 985, 1],
    [11.96, 1.09, 2.3, 21, 101, 3.38, 2.14, .13, 1.65, 3.21, .99, 3.13, 886, 1],
    [11.66, 1.88, 1.92, 16, 97, 1.61, 1.57, .34, 1.15, 3.8, 1.23, 2.14, 428, 1],
    [13.03, .9, 1.71, 16, 86, 1.95, 2.03, .24, 1.46, 4.6, 1.19, 2.48, 392, 1],
    [11.84, 2.89, 2.23, 18, 112, 1.72, 1.32, .43, .95, 2.65, .96, 2.52, 500, 1],
    [12.33, .99, 1.95, 14.8, 136, 1.9, 1.85, .35, 2.76, 3.4, 1.06, 2.31, 750, 1],
    [12.7, 3.87, 2.4, 23, 101, 2.83, 2.55, .43, 1.95, 2.57, 1.19, 3.13, 463, 1],
    [12, .92, 2, 19, 86, 2.42, 2.26, .3, 1.43, 2.5, 1.38, 3.12, 278, 1],
    [12.72, 1.81, 2.2, 18.8, 86, 2.2, 2.53, .26, 1.77, 3.9, 1.16, 3.14, 714, 1]
]

if __name__ == '__main__':
    n = int(input())

    train_set = dataset[:n]
    train_x = [[row[1]] for row in train_set]
    train_y = [row[-1]for row in train_set]

    test_set = dataset[n:]
    test_x = [[row[1]] for row in dataset]
    test_y = [row[-1] for row in dataset]

    scaling = MinMaxScaler()
    train_x_scaled = scaling.fit_transform(train_x)
    test_x_scaled = scaling.transform(test_x)

    nb_classifier = GaussianNB()
    nb_classifier.fit(train_x, train_y)

    nb_accuracy = 0
    for x_sample, y_sample in zip(test_x, test_y):
        predict = nb_classifier.predict([x_sample])
        if y_sample == predict[0]:
            nb_accuracy += 1
    naivebayes_accuracy = nb_accuracy / len(test_y)
    print(round(naivebayes_accuracy,5))

    dt_accuracy = 0
    dt_classifier = DecisionTreeClassifier(criterion='entropy')
    dt_classifier.fit(train_x, train_y)

    for x_sample, y_sample in zip(test_x, test_y):
        predict = dt_classifier.predict([x_sample])
        if y_sample == predict[0]:
            dt_accuracy += 1
    decisiontree_accuracy = dt_accuracy/len(test_y)
    print(round(decisiontree_accuracy, 5))

    e_accuracy = 0
    ensemble = RandomForestClassifier( n_estimators=4, random_state=0, criterion='entropy')
    ensemble.fit(train_x, train_y)

    for x_sample, y_sample in zip(test_x, test_y):
        predict = ensemble.predict([x_sample])
        if y_sample == predict[0]:
            e_accuracy += 1
    ensemble_accuracy = e_accuracy/len(test_y)
    print(round(ensemble_accuracy, 5))

    mlp_accuracy = 0
    mlp_classifier = MLPClassifier(learning_rate_init=0.0001, n_iter_no_change=10, hidden_layer_sizes=(10,), activation='relu', max_iter=200,random_state=1)
    mlp_classifier.fit(train_x, train_y)

    for x_sample, y_sample in zip(test_x, test_y):
        predict = mlp_classifier.predict([x_sample])
        if y_sample == predict[0]:
            mlp_accuracy += 1
    mlp_classifier_accuracy = mlp_accuracy/len(test_y)
    print(round(mlp_classifier_accuracy,5))

    highest_accuracy = max(naivebayes_accuracy, decisiontree_accuracy, mlp_accuracy, ensemble_accuracy)

    if naivebayes_accuracy == highest_accuracy:
        print("The highest accuracy was achieved by the classifier: Naive Bayes")
    elif ensemble_accuracy == highest_accuracy:
        print("The highest accuracy was achieved by the classifier: Random Forest")
    elif decisiontree_accuracy == highest_accuracy:
        print("The highest accuracy was achieved by the classifier: DecisionTree")
    else:
        print("The highest accuracy was achieved by the classifier: MLP")

    nb_classifier_scaled = GaussianNB()
    nb_classifier.fit(train_x_scaled, train_y)
    nb_accuracy_scaled = 0
    for x_sample, y_sample in zip(test_x, test_y):
        predict = nb_classifier.predict([x_sample])
        if y_sample == predict[0]:
            nb_accuracy_scaled += 1
    naivebayes_accuracy_scaled = nb_accuracy_scaled / len(test_y)
    print("Naive bayes classifier scaled: ",round(naivebayes_accuracy_scaled, 5))
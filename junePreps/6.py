import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'

dataset = [
    [2.55, 1.42, 5.15, 'Perch'],
    [3.9, 2.2, 6.6, 'Bream'],
    [1.3, 0.75, 3.6, 'Roach'],
    [3.85, 2.15, 6.55, 'Bream'],
    [2.6, 1.5, 5.2, 'Perch'],
    [1.0, 0.6, 3.1, 'Roach'],
    [2.7, 1.45, 5.3, 'Perch'],
    [3.8, 2.1, 6.5, 'Bream'],
    [1.25, 0.78, 3.4, 'Roach'],
    [1.2, 0.7, 3.3, 'Roach'],
    [2.4, 1.3, 5.0, 'Perch'],
    [4.0, 2.3, 6.7, 'Bream'],
    [1.1, 0.8, 3.5, 'Roach'],
    [2.5, 1.4, 5.1, 'Perch'],
    [3.7, 2.0, 6.4, 'Bream']
]

if __name__ == '__main__':
    p = int(input())
    c = input()
    l = int(input())

    train_set = dataset[:p]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[len(dataset)-p:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    dt_classifier = DecisionTreeClassifier(criterion=c, max_depth=l,random_state=0)
    dt_classifier.fit(train_x, train_y)

    accuracy = 0
    for x_sample, y_sample in zip(test_x, test_y):
        predict = dt_classifier.predict([x_sample])[0]
        if y_sample == predict:
            accuracy += 1
    dt_accuracy = accuracy / len(test_y)

    dt_ensemble_classifier = RandomForestClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    dt_ensemble_classifier.fit(train_x, train_y)

    labels = ["Roach", "Perch", "Bream"]

    classifiers = {}
    for label in labels:
        binary_y = [1 if y == label else 0 for y in train_y]
        clf = DecisionTreeClassifier(criterion=c, max_depth=l, random_state=0)
        clf.fit(train_x, binary_y)
        classifiers[label] = clf

    correct = 0
    for x_sample, y_sample in zip(test_x, test_y):
        votes = {}
        for label in labels:
            prediction = classifiers[label].predict([x_sample])[0]
            votes[label] = prediction

        is_correct = (votes[y_sample] == 1) and all( votes[label] == 0 for label in labels if label != y_sample)

        if is_correct:
            correct += 1

    dt_ensemble_accuracy = correct / len(test_y)

    print("Accuracy with the original classifier:",dt_accuracy)
    print("Accuracy with the ensemble classifier:",dt_ensemble_accuracy)
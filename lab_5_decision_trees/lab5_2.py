import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.ensemble import RandomForestClassifier
from submission_script import *
from dataset_script import dataset

# This is a sample from the dataset, for training/evaluation use the imported variable dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    column_index = int(input())
    number_of_trees = int(input())
    crit = input()
    input_to_predict = [el for i,el in enumerate(list(map(float, input().split(" ")))) if i !=column_index]

    dataset_deleted_col = list()
    for row in dataset:
        dataset_deleted_col.append([row[i] for i in range(0, len(row)) if i != column_index])
    dataset = dataset_deleted_col

    test_set = dataset[int(len(dataset) * 0.85):]
    x_test = [row[:-1] for row in test_set]
    y_test = [row[-1] for row in test_set]

    train_set = dataset[:int(len(dataset) * 0.85)]
    x_train = [row[:-1] for row in train_set]
    y_train = [row[-1] for row in train_set]


    classifier = RandomForestClassifier(
        criterion=crit,
        random_state=0,
        n_estimators=number_of_trees
    )
    classifier.fit(x_train, y_train)

    accuracy = 0
    for to_predict, actual_class in zip(x_test, y_test):
        prediction = classifier.predict([to_predict])[0]
        if prediction == actual_class:
            accuracy += 1
    accuracy /= len(y_test)
    print(f"Accuracy: {accuracy}")

    prediction_from_input = classifier.predict([input_to_predict])[0]
    print(prediction_from_input)
    print(classifier.predict_proba([input_to_predict])[0])

    # At the end you need to submit the dataset, classifier and encoder by calling the following functions

    # submit the training set
    # submit_train_data(train_X, train_Y)
    submit_train_data(x_train, y_train)

    # submit the test set
    # submit_test_data(test_X, test_Y)
    submit_test_data(x_test, y_test)
    # submit the classifier
    # submit_classifier(classifier)
    submit_classifier(classifier)
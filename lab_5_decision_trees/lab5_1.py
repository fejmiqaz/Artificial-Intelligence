import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from AI.lab5_datasets.zad1_dataset import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

# This is a sample from the dataset, for training/evaluation use the imported variable dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    X = float(input())
    X /= 100
    crit = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[int(len(dataset) * (1.0 - X)):]
    x_train = [row[:-1] for row in train_set]
    y_train = [row[-1] for row in train_set]
    x_train = encoder.transform(x_train)

    test_set = dataset[:int(len(dataset) * (1.0 - X))]
    x_test = [row[:-1] for row in test_set]
    y_test = [row[-1] for row in test_set]
    x_test = encoder.transform(x_test)

    decision_tree_classifier = DecisionTreeClassifier(criterion=crit, random_state=0)
    decision_tree_classifier.fit(x_train, y_train)

    print(f"Depth: {decision_tree_classifier.get_depth()}")
    print(f"Num of leaves: {decision_tree_classifier.get_n_leaves()}")

    accuracy = 0
    for to_predict, actual_class in zip(x_test, y_test):
        prediction = decision_tree_classifier.predict([to_predict])[0]
        if prediction == actual_class:
            accuracy += 1
    accuracy /= len(y_test)
    print(f"Accuracy: {accuracy}")

    feature_importances = decision_tree_classifier.feature_importances_
    max_idx = max(list(feature_importances))
    min_idx = min(list(feature_importances))

    for i, importance in enumerate(feature_importances):
        if importance == max_idx:
            print("Most important feature: " + str(i))
        if importance == min_idx:
            print("Least important feature: " + str(i))

    # At the end you need to submit the dataset, classifier and encoder by calling the following functions

    # submit the training set
    # submit_train_data(train_X, train_Y)
    submit_train_data(x_train, y_train)

    # submit the test set
    # submit_test_data(test_X, test_Y)
    submit_test_data(x_test, y_test)
    # submit the classifier
    # submit_classifier(classifier)
    submit_classifier(decision_tree_classifier)

    # submit the encoder
    # submit_encoder(encoder)
    submit_encoder(encoder)
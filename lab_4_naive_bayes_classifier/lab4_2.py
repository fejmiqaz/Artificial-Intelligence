import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.naive_bayes import CategoricalNB
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import accuracy_score

# from submission_script import *
from AI.lab4_datasets.zad2_dataset import dataset

if __name__ == '__main__':
    # Your code here
    data_set = [[float(i) for i in row] for row in dataset]

    train_set = data_set[:int(0.85 * len(dataset))]
    x_train = [row[:-1] for row in train_set]
    y_train = [row[-1] for row in train_set]

    test_set = data_set[int(0.85 * len(data_set)):]
    x_test = [row[:-1] for row in test_set]
    y_test = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(x_train, y_train)

    accuracy = 0

    for x_sample, y_sample in zip(x_test, y_test):
        predicted = classifier.predict([x_sample])[0]
        if predicted == y_sample:
            accuracy += 1

    print(accuracy / len(test_set))

    input_test = [float(i) for i in input().split(" ")]

    prediction_from_input = classifier.predict([input_test])[0]
    print(int(prediction_from_input))
    print(classifier.predict_proba([input_test]))

# At the end you are required to submit the dataset,
# the classifier and the encoder via calling the folllowing functions

# submit the train dataset
# submit_train_data(train_X, train_Y)

# submit the test dataset
# submit_test_data(test_X, test_Y)

# submit the classifier
# submit_classifier(classifier)

# re-import at the end / do not remove the following line

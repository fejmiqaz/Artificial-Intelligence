import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from AI.lab4_datasets.zad1_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB, GaussianNB

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.75 * len(dataset))]
    x_train = [row[:-1] for row in train_set]
    y_train = [row[-1] for row in train_set]
    x_train_encoded = encoder.transform(x_train) # encoded

    test_set = dataset[int(0.75 * len(dataset)):]
    x_test = [row[:-1] for row in test_set]
    y_test = [row[-1] for row in test_set]
    x_test_encoded = encoder.transform(x_test)

    acc = 0
    classifier = CategoricalNB()
    classifier.fit(x_train_encoded, y_train)

    for x_sample, y_sample in zip (x_test_encoded, y_test):
        prediction = classifier.predict([x_sample])[0]
        if prediction == y_sample:
            acc += 1

    print(acc/len(x_test))

    input_test = [i for i in input().split(" ")]
    input_test_encoded = encoder.transform([input_test])

    prediction_input = classifier.predict(input_test_encoded)[0]
    predictions_input_probabilites = classifier.predict_proba(input_test_encoded)

    print(prediction_input)
    print(predictions_input_probabilites)

    # At the end you are required to submit the dataset,
    # the classifier and the encoder via calling the following function

    # submit the train dataset
    # submit_train_data(train_X, train_Y)
    # submit the test dataset
    # submit_test_data(test_X, test_Y)
    # submit the classifier
    # submit_classifier(classifier)
    # submit the encoderot
    # submit_encoder(encoder)

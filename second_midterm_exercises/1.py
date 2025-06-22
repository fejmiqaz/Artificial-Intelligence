import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    C = int(input())
    P = int(input())

    modified_dataset = []

    for row in dataset:
        features = row[:-1]
        class_label = row[-1]

        sum_feature = features[0] + features[-1]

        middle_features = features[1:-1]
        new_features = [sum_feature] + middle_features

        modified_row = new_features + [class_label]
        modified_dataset.append(modified_row)

    good = []
    bad = []

    for row in modified_dataset:
        if row[-1] == 'good':
            good.append(row)
        else:
            bad.append(row)

    good_train_size = int((P / 100) * len(good))

    if C == 0:
        good_train = good[:good_train_size]
        good_test = good[good_train_size:]
    else:
        good_train = good[:-good_train_size]
        good_test = good[-good_train_size:]

    bad_train_size = int((P / 100) * len(bad))

    if C == 0:
        bad_train = bad[:bad_train_size]
        bad_test = bad[bad_train_size:]
    else:
        bad_train = bad[:-bad_train_size]
        bad_test = bad[-bad_train_size:]

    train_set = good_train + bad_train
    test_set = good_test + bad_test

    x_train = [row[:-1] for row in train_set]
    y_train = [row[-1] for row in train_set]
    x_test = [row[:-1] for row in test_set]
    y_test = [row[-1] for row in test_set]

    classifier1 = GaussianNB()
    classifier1.fit(x_train, y_train)

    acc1 = 0

    for x_sample, y_sample in zip(x_test, y_test):
        prediction = classifier1.predict([x_sample])[0]
        if prediction == y_sample:
            acc1 += 1
    accuracy1 = acc1 / len(x_test)

    scaler = MinMaxScaler(feature_range=(-1,1))
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    classifier2 = GaussianNB()
    classifier2.fit(x_train_scaled, y_train)

    acc2 = 0

    for x_sample, y_sample in zip(x_test_scaled, y_test):
        prediction = classifier2.predict([x_sample])[0]
        if prediction == y_sample:
            acc2 += 1

    accuracy2 = acc2 / len(y_test)

    print("Accuracy with a sum of columns: ", float(accuracy1))
    print("Accuracy with a sum of columns and feature scaling: ", float(accuracy2))
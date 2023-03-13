import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

PATH = "bayes/iris.data"

def read_data(path):
    df = pd.read_csv(path, header=None)
    df = df.to_numpy()
    return df

def compute_apriori(X_train, Y_train):
    apriori = {}
    list_of_classes = []
    Y_set = set(Y_train)
    size = len(X_train)
    for y in Y_set:
        apriori[y] = Y_train.count(y)/size
        list_of_classes.append(y)
    return apriori, list_of_classes

def set_names(Y_train):
    prob_in_bin = {}
    Y_set = set(Y_train)
    for y in Y_set:
        prob_in_bin[y] = 0.01
    return prob_in_bin

def compute_other_prob(counts, X_train, Y_train, i):
    XY_train = np.column_stack((X_train, Y_train))
    XY_train = XY_train[XY_train[:, i].argsort()]
    prob_of_atribute = []
    idx = 0
    for i in range(len(counts)):
        prob_in_bin = set_names(Y_train)
        values, count = np.unique([XY_train[idx : idx + counts[i],-1]], return_counts=True)
        for j in range(len(values)):
            prob_in_bin[values[j]] += count[j] / counts[i]
        prob_of_atribute.append(prob_in_bin)
        idx = idx + counts[i]
    return prob_of_atribute

def bayes_classifier(path, percent_of_train_set):
    data = read_data(path)
    data_size = np.shape(data)[0]
    X = [data[i][:-1] for i in range(data_size)]
    Y = [data[i][-1] for i in range(data_size)]
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y ,train_size=percent_of_train_set, shuffle=True)
    n_of_atributes = len(X_train[0])
    ##### TRAIN #####
    apriori, list_of_classes = compute_apriori(X_train, Y_train)
    prob_other = []
    bins = []
    for atribute_idx in range(n_of_atributes):
        counts, bin = np.histogram([X_train[i][atribute_idx] for i in range(len(X_train))])
        bins.append(bin)
        prob_other.append(compute_other_prob(counts, X_train, Y_train, atribute_idx))
    # print(prob_other)
    ##### TEST #####
    Y_pred = []
    for idx in range(len(X_test)):
        prob_x = np.array([apriori[y] for y in apriori])
        for i in range(n_of_atributes):   
            for j in range(len(bins[i])):
                if bins[i][j] > X_test[idx][i]:
                    prob_of_classes_for_atribute = []
                    for pred_class in apriori:
                        prob_others = prob_other[i][j - 1][pred_class]
                        prob_of_classes_for_atribute.append(prob_others)
                    prob_of_classes_for_atribute = np.array(prob_of_classes_for_atribute)
                    prob_x = prob_x * prob_of_classes_for_atribute
                    break
        Y_pred.append(list_of_classes[np.argmax(prob_x)])
    return Y_pred, Y_test

                    


print()
vvalues = []
par = 0.0
for i in range(9):
    values = []
    for i in range(5):
        Y_pred, Y_test = bayes_classifier(PATH, par + 0.1)
        result = np.column_stack((Y_pred, Y_test))
        count = 0
        # print(result)
        for i in range(len(Y_test)):
            if Y_test[i] != Y_pred[i]:
                count += 1
        values.append(count/len(Y_test)*100)
        # print(count)
        # print(len(Y_test))
        # print("Percentage of failures: ", count/len(Y_test)*100)
    vvalues.append(sum(values)/5)
    par += 0.1
# print(vvalues)
keys = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
plt.plot(keys, vvalues, 'o')
plt.show()


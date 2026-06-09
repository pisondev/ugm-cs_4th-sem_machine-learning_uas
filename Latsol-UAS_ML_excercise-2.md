# Excercise Machine Learning -2

Lecturer : Afiahayati, S.Kom., M.Cs., Ph.D.

---

1. Look at table 1. Determine the class (Y) for the test data using the 3-nearest neighbor method. Please use the euclidian distance for the distance calculation process!

Table 1. Training and Testing data

| | Training Data | | | | | | Testing Data | |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| X1 | 2 | 1 | 2 | 3 | 1 | 3 | 2 | 1 |
| X2 | 2 | 2 | 3 | 3 | 0 | 2 | 1 | 1 |
| Y | -1 | 1 | -1 | 1 | 1 | -1 | ??? | ??? |

2. Please explain for which data the Support Vector Machine is suitable!

3. Please pay attention to Figure 1. Please explain how the machine learning method works in Figure 1.

```
from sklearn import naive_bayes

nb = naive_bayes.CategoricalNB()

nb.fit(X_train, y_train)
y_pred = nb.predict(X_test)
```

Figure 1. Code snippets for number 3

4. a. Please explain the algorithms of bagging, boosting and stacking! Please also explain the diffencess! (score : 3%)

   b. Look at Figure 2. Please explain what is the meaning of base classifier, n_estimators and learning rate! (score:2%)

```
adaboost_classifier = AdaBoostClassifier(
    base_classifier, n_estimators=50, learning_rate=1.0, random_state=42
)
adaboost_classifier.fit(X_train, y_train)
```

Figure 2. Code Snippets of Adaboost

   c. Please pay attention to the following data. Please implement the Bagging algorithm for the data. Please use only 3 bootstrapings/single models! Please write the final prediction and calculate the accuracy! (score : 5%)

Table 2. Data for Bagging Algorithm

| Source Dataset | x | 2,4 | 3,1 | 3,7 | 4,4 | 5,2 | 5,8 |
|---|---|---:|---:|---:|---:|---:|---:|
| | y | 1 | 1 | 1 | -1 | -1 | -1 |

# FINAL EXAMINATION

UNIVERSITY ELEPHANT MADA  
FACULTY OF MATHEMATICS AND NATURAL SCIENCES  
DEPARTMENT OF COMPUTER SCIENCE AND ELECTRONICS  
IUP COMPUTER SCIENCE

Semester II Academic Year 2024/2025

Course name : Machine Learning - CSA  
Day, date : Wednesday , 11 June 2025  
Time : 07.30 – 09.20 (110 minutes )  
Lecturer : Afiahayati, M.Cs. , Ph.D.  
Exam Type : Open 1 sheet of A4 hand written notes, Open Calculator , Closed  
Book , Gadget OFF, Laptop OFF, Internet OFF

Instructions:

1. This final exam contributes 35% of your final grade
2. Please submit your A4 handwritten notes together with the answer sheet

---

PLO2; CO-2: Students are able to understand data preparation and performance evaluation in machine learning (score: 10%).

1. Please answer the questions below !

   a. Look at Figure 1. Please write the output of the python code below , if the total number of data from the dataset is 500! (score : 2%)

```
[ ] from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7)

[ ] print("Banyak data latih setelah dilakukan Train-Test Split: ", len(X_train))
    print("Banyak data uji setelah dilakukan Train-Test Split: ", len(X_test))
```

Figure 1. Code Snippets of Data preparation

   b. Please explain about k- fold cross validation ! When should we use k- fold cross validation ? (score : 3%)

   c. Look at Table 1. Table 1 represents the target and prediction results of a classification model. There are 2 classes , namely the YES class and the NO class . Create a Confusion Matrix from the classification results , then calculate the accuracy, sensitivity / recall , precision and F1-measure! (score : 5%)

Table 1. Classification results table

| No. | Target | Classification Results |
|---:|---|---|
| 1 | NO | NO |
| 2 | NO | YES |
| 3 | YES | YES |
| 4 | YES | NO |
| 5 | YES | YES |
| 6 | NO | NO |
| 7 | NO | NO |
| 8 | YES | NO |
| 9 | YES | YES |
| 10 | YES | NO |
| 11 | YES | NO |
| 12 | YES | YES |

---

PLO3; CO-5: Students are able to understand k-NN and apply it to solve a case (score : 4%).

2. Determine whether the following statements are correct or wrong and give the reason

   a. K-NN is more suitable used on large datasets because its high speed for prediction. (score :2%)

   b. K-NN must use the Euclidian Distance formula (score 2%)

PLO3; CO-6: Students are able to understand Naive Bayes Model and apply it to solve a case (score : 5%).

3. Given data as following (Table 2)

Table 2. Play Tennis Data

PlayTennis: training examples

| Day | Outlook | Temperature | Humidity | Wind | PlayTennis |
|---|---|---|---|---|---|
| D1 | Sunny | Hot | High | Weak | No |
| D2 | Sunny | Hot | High | Strong | No |
| D3 | Overcast | Hot | High | Weak | Yes |
| D4 | Rain | Mild | High | Weak | Yes |
| D5 | Rain | Cool | Normal | Weak | Yes |
| D6 | Rain | Cool | Normal | Strong | No |
| D7 | Overcast | Cool | Normal | Strong | Yes |
| D8 | Sunny | Mild | High | Weak | No |
| D9 | Sunny | Cool | Normal | Weak | Yes |
| D10 | Rain | Mild | Normal | Weak | Yes |
| D11 | Sunny | Mild | Normal | Strong | Yes |
| D12 | Overcast | Mild | High | Strong | Yes |
| D13 | Overcast | Hot | Normal | Weak | Yes |
| D14 | Rain | Mild | High | Strong | No |

   a. Create a probability table from the playtennis data above. Then use the Naive Bayes Model to determine whether on days D15 and D16 it is advisable to play tennis or not with the following weather. (Score : 3,5%)

D15: Outlook = Rain, Temperature = Mild, Humidity = Normal, Wind = Weak

   b. In the beginning, Naïve bayes is designed for the categorical data. But Naïve bayes model also can be implemented for numerical data. Please explain, how is Naïve bayes implemented for numerical data? (Score : 1,5%)

PLO3; CO-7: Student a r e a b l e t o understand ensemble learning and apply it to solve a case (score 10%)

4. a. Please explain the algorithms of bagging, boosting and stacking! Please also explain the diffencess! (score : 3%)

   b. Look at Figure 2. Please explain what is the meaning of base classifier, n_estimators and learning rate! (score:2%)

```
adaboost_classifier = AdaBoostClassifier(

    base_classifier, n_estimators=50, learning_rate=1.0, random_state=42

)

adaboost_classifier.fit(X_train, y_train)
```

Figure 2. Code Snippets of Adaboost

   c. Please pay attention to the following data. Please implement the Bagging algorithm for the data. Please use only 3 bootstrappings/single models! Please write the final prediction and calculate the accuracy! (score : 5%)

Table 3. Data for Bagging Algorithm

| Source Dataset | x | 2,4 | 3,1 | 3,7 | 4,4 | 5,2 | 5,8 | 6,4 |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| | y | 1 | 1 | 1 | -1 | -1 | -1 | -1 |

PLO3; CO-7: Student a r e a b l e t o understand clustering and apply it to solve a case (score 6%)

5. a. Please explain what is the difference between clustering and classification? (score: 3%)

   b. Please explain how to determine the optimal value of k in k-means clustering. Please loot at Figure 3. Based on the figure 3, please determine the optimal value of k! (score : 3%)

Elbow Method For Optimal k

Sum_of_squared_distances

Number of Clusters (k)

Figure 3. Elbow method for optimal k

-- No effort will be vain –

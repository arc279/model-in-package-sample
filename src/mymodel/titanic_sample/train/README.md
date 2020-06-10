
## data source

https://www.kaggle.com/c/titanic/data

## データ配置

```
.
├── README.md
├── data
│   ├── input
│   │   ├── gender_submission.csv
│   │   ├── test.csv
│   │   ├── titanic.zip
│   │   └── train.csv
│   └── models -> ../../models/
├── lr.py
├── rf.py
└── svc.py
```

## 実行

[中身](rf.py)は本題じゃないので適当です。

```bash
$ python rf.py
$ python lr.py
$ python svc.py
```

## 生成後

```
data/models/
├── LogisticRegression
│   ├── __init__.py
│   └── model.pkl
├── RandomForestClassifier
│   ├── __init__.py
│   └── model.pkl
├── SVC
│   ├── __init__.py
│   └── model.pkl
└── __init__.py
```

# モデルデータをパッケージに含めるサンプル

## [バージョニング](./src/mymodel/version.py)に関する知見の資料

cf. https://mercari.github.io/ml-system-design-pattern/Operation-patterns/Data-model-versioning-pattern/design_ja.html


## generate models

[こちら](./src/mymodel/titanic_sample/train/README.md)を参照。


## package

```bash
$ python -V
Python 3.8.1

$ python -m venv .venv
$ . .venv/bin/activate

(.venv) $ pip install wheel
(.venv) $ python setup.py bdist_wheel

(..snip..)

(.venv) $ zipinfo -1 dist/mymodel-1.1.1_titanic.from_kaggle-py3-none-any.whl
mymodel/__init__.py
mymodel/version.py
mymodel/titanic_sample/__init__.py
mymodel/titanic_sample/models/__init__.py
mymodel/titanic_sample/models/LogisticRegression/__init__.py
mymodel/titanic_sample/models/LogisticRegression/model.pkl
mymodel/titanic_sample/models/RandomForestClassifier/__init__.py
mymodel/titanic_sample/models/RandomForestClassifier/model.pkl
mymodel/titanic_sample/models/SVC/__init__.py
mymodel/titanic_sample/models/SVC/model.pkl
mymodel/titanic_sample/models/SVC/__pycache__/__init__.cpython-38.pyc
mymodel/titanic_sample/models/__pycache__/__init__.cpython-38.pyc
mymodel-1.1.1_titanic.from_kaggle.dist-info/METADATA
mymodel-1.1.1_titanic.from_kaggle.dist-info/WHEEL
mymodel-1.1.1_titanic.from_kaggle.dist-info/top_level.txt
mymodel-1.1.1_titanic.from_kaggle.dist-info/RECORD
```

## usage

呼び出し方は[こちら](./this_is_usage.py)を参照。


```bash
$ python -m venv .venv
$ . .venv/bin/activate

(.venv) $ pip install dist/mymodel-1.1.1_titanic.from_kaggle-py3-none-any.whl

(..snip..)

(.venv) $ pip list
Package         Version
--------------- -------------------------
joblib          0.15.1
mymodel         1.1.1-titanic.from-kaggle
numpy           1.18.5
pandas          1.0.4
pip             19.2.3
python-dateutil 2.8.1
pytz            2020.1
scikit-learn    0.23.1
scipy           1.4.1
setuptools      41.2.0
six             1.15.0
threadpoolctl   2.1.0
wheel           0.34.2

(.venv) $ ./this_is_usage.py
1.1.1-titanic.from-kaggle
SVC()
[0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 0 1 1 0 1 0 0 0 0 0 0 0 1 0 0
 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0
 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0
 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0
 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 1 0
 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0
 0 0 0 0 0 0 0 1 0 0 0 1 0 1 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0
 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 1 1 0 0 0 0 0 0 1 0 0 0 1 1 0 0 1 0 0
 1 0 0 1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 1 0 0 1 0 1 0 0 0 0 1
 0 0 0 1 0 0 1 0 0 0]
```

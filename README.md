[![Build Status](https://travis-ci.org/serhii73/python_sum_in_ua_api.svg?branch=master)](https://travis-ci.org/serhii73/python_sum_in_ua_api)

# ukrdict
Python wrapper for [sum.in.ua/api](http://sum.in.ua/api)

##### Search for the word meaning
```bash
ukrdict тин 
```
```
ТИН, у, чол. Огорожа, сплетена з лози, тонкого гілля
пліт. Та вже ж наші слобожани Тини городили; Із-під
лугу, із-під гаю Лозу волочили (Яків Щоголів, Поезії, 1958, 130);
```

##### Installation
1. Clone the repository
2. Create Python virtual environment and install ukrdict package
```bash
cd sum_in_ua
python -m venv myenv && source myenv/bin/activate
python ukrdict/setup.py install
```

### package the project into a wheel
```python setup.py sdist bdist_wheel```


### test the project out
```bash
python -m virtualenv venv
source venv/bin/activate
pip install <location of wheel file>
```

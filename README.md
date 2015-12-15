# SimplePythonParser
```python
>>> from extracter import Extracter
>>> f = open('extracter.py')
>>> e = Extracter(f=f)
>>> e.extract(pattern_name='class')
['Extracter']
>>> e.extract_all(pattern_name='class')
['class Extracter:']
```

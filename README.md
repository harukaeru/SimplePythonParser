# SimplePythonParser
```python
>>> from parser import Extracter
>>> f = open('parser.py')
>>> e = Extracter(f=f)
>>> e.extract(pattern_name='class')
['Extracter']
>>> e.extract_all(pattern_name='class')
['class Extracter:']
```

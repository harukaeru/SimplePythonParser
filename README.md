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

## Todo
- Add tests
- Rename project
- Able to use 'python setup.py install'
- Upload to pypi
- Add patterns
- Be useful not only 'python'
- For purpose of multi-line

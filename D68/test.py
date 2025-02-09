from os import path

print(path.abspath(path.join(path.dirname(__file__), "..",  "static", 'files')))
class StreamDataFilter:
    def __init__(self, data):
        self.data = data

    def filter(self, condition):
        return [item for item in self.data if condition(item)]

# Misol ma'lumotlar
data = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 30},
    {"name": "Hasan", "age": 20},
    {"name": "Husan", "age": 35}
]

# Filter qilish
filtered_data = StreamDataFilter(data).filter(lambda x: x["age"] > 25)

# Natija
print(filtered_data)
```

Natija:
```python
[
    {'name': 'Vali', 'age': 30},
    {'name': 'Husan', 'age': 35}
]

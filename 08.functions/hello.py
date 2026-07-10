# Named parameters with type hints and a default value
def hello(name: str, last_name: str, age: int, default: str = 'default value') -> None:
    print('Hello')
    print(f'Welcome {name} {last_name} - {age} years old')
    print(default)

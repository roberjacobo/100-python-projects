import hello
import kwargs
import xargs


def main() -> None:
    # Positional arguments (order matters)
    hello.hello('Roberto', 'Jacobo', 33)

    # Keyword arguments (order does not matter)
    hello.hello(last_name='Jacobo', name='Roberto', age=33, default='No default')

    print('---------------')
    # *args: variable number of positional arguments
    print(xargs.sum_all(1, 2, 51, 19))

    print('---------------')
    # **kwargs PACKING: id and name are required, desc goes into **extra
    print(kwargs.get_product(id='1', name='iPhone', desc='This is an iPhone'))

    # **kwargs UNPACKING: ** turns the dict into keyword arguments
    data = {'id': '1', 'name': 'iPhone', 'desc': 'This is an iPhone'}
    print(kwargs.get_product(**data))  # same as the call above


if __name__ == '__main__':
    main()

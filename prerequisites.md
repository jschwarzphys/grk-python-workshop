# Prerequisites


- variables

  ```python
  # variable assignment
  favorite_number = 42
  hello = "World"
  ```

    - integer
      ```python
      num = 3
      other = (num * 2)**2 + 3  # arithmethics
      num += 1  # in-place arithmetics
      ```

    - float
      ```python
      circle = 3.14
      cake = (cirlcle * 2)**2 + 3  # arithmethics
      circle *= 2  # in-place arithmetics
      ```

    - complex
      ```python
      point = 1.2+3.4j
      other = point * 2  # arithmetics
      point += 3.2  # in-place arithmetics
      x = other.real  # real part
      y = other.imag  # imaginary part
      ```
    - string
      ```python
      greeting = "Hello, World!"
      upper = greeting.upper()  # HELLO, WORLD!
      lower = greeting.lower()  # hello, world!
      greeting.startswith("Hello")  # True
      greeting.endwrith("Earth!")  # False
      greeting[1:5]  # substring: ello

      name = "Uni" + "Freiburg"  # concatination
      scream =  "a" * 10  # aaaaaaaaaa
      ```

    - tuple
      ```python
      point = (3.42, 4)  # 2-tuple
      point[0]  # 3.42
      ```

    - list
      ```python
      numbers = [1, 2, 3, 5]
      numbers.append(7)  # append number
      numbers[0] = 3   # set item
      5 in numbers  # True

      listed = "--".join(["A", "B", "C", "D"])  # A--B--C--D
      ```

    - set
      ```python
      numbers = set([1, 2, 3, 5])
      numbers.add(7)  # add number
      9 in numbers  # False
      ```

    - dict
      ```python
      phonebook = {
          "Alice": 1234567,
          "Bob": 2345678,
      }

      phonebook["Bob"] = 3456789  # update item
      phonebook["David"] = 1357924  # add item
      "Eva" in phonebook  # False
      phonebook.keys()  # Alice, Bob, David
      phonebook.values()  # 1234567, 3456789, 1357924
      phonebook.items()  # (Alice, 1234567), ...
      ```

- import
  ```python
  # standard import
  import math

  # import parts
  from time import sleep

  # import as alias
  import numpy as np
  ```

- functions

  ```python
  # Function definition
  def greet(people):
    for person in people:
        print("Hello", person)

  # Call function
  greet(["Lea", "Mark"])
  ```

  - default arguments
    ```python
    def root(number, base=2):
      return math.pow(number, 1/base)

    root(4)  # use default
    root(27, 3)  # use different base
    root(3, base=1)  # named arguments
    ```

  - Lambda, usually passed to other functions
    ```python
    first = lambda x: x[0]

    # equal to
    def first(x):
      return x[0]
    ```

  - Positional arguments and keyword arguments
    ```python
    def func(pos_1, pos_2, *args, kwd_1="a", kwd_2="b", **kwds):
      pass

    funct(6, 7, 8, 9, 10, kwd_2="c", hello="world")
    # -> pos_1 = 6
    # -> pos_2 = 7
    # -> args = [8, 9, 10]
    # -> kwd_1 = "a"
    # -> kwd_2 = "c"
    # -> kwds = {"hello": "world"}
    ```

  - builtins
    ```python
    len(["a", "b", "c"])  # 3
    len("hello")  # 5
    len({"Hello": "world"}) # 1

    sorted([3, 5, 1])  # 1, 3, 5
    sorted("hello")  # e, h, l, l, o

    print("Hello", "World")  # Hello World
    print("Hello", "World", sep="")  # HelloWorld
    print("Hello", "World", file=some_file)  # prints to file
    print("Hello", "World", end="!")  # Hello World! (no new line)

    round(3.1415)  # 3
    round(3.1415, 2)  # 3.14

    reversed([1, 2, 5])  # 5, 2, 1

    sum([1, 2, 3, 5, 8])  # 19
    max([1, 2, 3, 5, 8])  # 8
    min([1, 2, 3, 5, 8])  # 1

    abs(7)  # 7
    abs(-4)  # 4

    any([True, False, False])  # True
    all([True, False, False])  # False

    help(int)  # print help about object
    dir(int)  # lists all attributes of object
    vars(int)  # lists all attributes and its values

    name = input("Please enter name: ")  # prompt user to enter name
    ```

- slicing
  ```python
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

  primes[3]  # access item: 7
  primes[5]  # access item: 13
  primes[3:5]  # range: 7, 11
  primes[3:]  # range: 7, 11, 13, 17, 19, 23, 29
  primes[:5]  # range: 2, 3, 5, 7, 11
  primes[:-3]  # range: 2, 3, 5, 7, 11, 13, 17

  primes[::2]  # steps: 2, 5, 11, 17, 23
  primes[1::2]  # steps: 3, 7, 13, 19, 29
  ```

- if
  ```python
  if 3 < 5:
      print("Three is less than five")
  ```

  - and, or, not
    ```python
    if "eva" in phonebook and phonebook["eva"] == 12345:
      print("Her number is 12345")

    if not number > 10:
      print("Number is too small")

    if "eva" not in phonebook:
      print("We don't have Eva's number.")
    ```

  - else, elif
    ```python
    if command == "help":
        print_help()
    elif command == "exit":
        sys.exit(0)
    else:
        print("Unknown command")
    ```
- loops
    - for
    - for-else
    - range
    - zip
    - enumerate
- with, open
- comprehension
    - list
    - set
    - dict
- numpy
    - array
    - arithmetics
    - linspace
    - functions, sin
    - max, sum, mean

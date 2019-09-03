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
      phonesbook.keys()  # Alice, Bob, David
      phonesbook.values()  # 1234567, 3456789, 1357924
      phonebook.items()  # (Alice, 1234567), ...
      ```

- import
    - standard
    - from
    - as
- functions
    - builtins: sorted, len, print, round
    - default arguments
    - `*args`, `**kwds`
- slicing
- if
    - and, or, not
    - else, elif
- loops
    - for
    - range
    - zip
    - enumerate
- with
- open
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

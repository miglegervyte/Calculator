# Calculator

Calculator is a tool performing basic mathematical operations.

## Installation 

*
*

## Functionality 

Calculator can perform these operations:
* Addition / Subtraction
* Multiplication / Division
* Take (n) root of a number
* Reset memory

Calculator has itself memory. At the beginning Calculator is set to 0 and after calculation are made it saves result to its memory. Memory is reset to 0 if two arguments are provided and operations are made between them or when `reset memory` function is used.

#### Addition

* If one number is provided calculator performs addition of memorised and provided numbers.
* If two numbers are provided calculator performs addition between them. 

```python
Calculator.add(8)
8
Calculator.add(8, 3)
11
```

#### Subtraction

* If one number is provided calculator subtracts provided number from memorised one.
* If two numbers are provided calculator subtracts second provided number from first provided number.

```python
Calculator.subtract(8)
-8
Calculator.subtract(8, 3)
5
```

#### Multiplication

* If one number is provided calculator performs multiplication of memorised and provided numbers.
* If two numbers are provided calculator performs multiplication of provided numbers.

```python
Calculator.multiply(8)
0
Calculator.add(8)
Calculator.multiply(8)
64
Calculator.multiply(8, 3)
24
```

#### Division

* If one number is provided calculator divides memorised number by provided one.
* If two numbers are provided calculator divides first number by second number.
* **Important**: division by 0 can not be performed and in these cases Calculator raises an error.

```python
Calculator.divide(8)
0
Calculator.add(8)
Calculator.divide(4)
2
Calculator.divide(8, 2)
4
```

#### Taking nth root of a number

* If one number is provided calculator takes nth root from memorised number.
* If two numbers are provided calculator takes nth root (first number) from provided number (second number).
* **Important**: the 0th root of any number is undefined and in these cases Calculator raises an error.

```python
Calculator.add(8)
Calculator.n_root(3)
2
Calculator.n_root(2, 16)
4
```

#### Checking and reseting memory 

Checks and resets memorised number.

```python
Calculator.add(8)
Calculator.subtract(5)
Calculator.check_memory()
3
Calculator.reset_memory()
0
```

## Docker file



## Licence 

[MIT](https://github.com/miglegervyte/Calculator/blob/main/LICENSE)

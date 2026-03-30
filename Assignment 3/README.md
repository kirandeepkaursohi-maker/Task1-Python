
## 📌 Description

This repository contains:
* Functions in Python
* Use of built-in modules (`math`)
* Performing calculations using loops and predefined functions

---

# 🧠 Concepts Covered

* Function definition and return values
* Loop-based calculations
* Python `math` module
* User input handling

---

# ✅ Task 1: Factorial Using a Function

## 🔹 Problem

Write a function to calculate the factorial of a number and display the result.

```

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")
```




## 📤 Output

```
Enter a number: 10
Factorial of 10 is: 3628800
```

## 💡 Explanation

* A function `factorial(n)` is created.
* A loop multiplies numbers from `1` to `n`.
* The result is returned and printed.

---

# ✅ Task 2: Using the Math Module

## 🔹 Problem

Take a number from the user and calculate:

* Square root
* Natural logarithm (log base e)
* Sine (in radians)

## 💻 Implementation

```python
from math import sin, log, sqrt
num = int(input("Enter a number: "))
square_root = sqrt(num)
Logarithm = log(num)
Sine = sin(num)
print(f"Square root:{square_root}")
print(f"Logarithm: {Logarithm}")
print(f"Sine: {Sine}")

```

## 📤 Example Output

```
Enter a number: 30
Square root:5.477225575051661
Logarithm: 3.4011973816621555
Sine: -0.9880316240928618
```

## 💡 Explanation

* The `math` module is used for calculations.
* `math.sqrt()` → square root
* `math.log()` → natural logarithm
* `math.sin()` → sine value (in radians)

---

# 🚀 How to Run

1. Clone the repository:

```
git clone <https://github.com/kirandeepkaursohi-maker/Python-Basics>
```

2. Navigate to the folder:

```
cd <Python-Basis>
```

3. Run the Python file:

```
python Assignment 3.py
```

---

# 📌 Notes

* Factorial uses a loop-based approach.
* `math.sin()` takes input in radians, not degrees.
* Input for logarithm must be greater than 0.

---


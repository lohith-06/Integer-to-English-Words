# Integer to English Words

A simple Python program that converts an integer into its English words representation.

## Problem Statement

Given an integer, convert it into its English words representation.

The program also handles:

* Positive numbers
* Negative numbers
* Zero
* Large numbers up to billions
* Proper spacing between words

## Examples

### Example 1

**Input:**

```text
123
```

**Output:**

```text
One Hundred Twenty Three
```

### Example 2

**Input:**

```text
12345
```

**Output:**

```text
Twelve Thousand Three Hundred Forty Five
```

### Example 3

**Input:**

```text
-12345
```

**Output:**

```text
Negative Twelve Thousand Three Hundred Forty Five
```

### Example 4

**Input:**

```text
0
```

**Output:**

```text
Zero
```

## Approach

1. Create a list containing words for numbers from `0` to `19`.
2. Create another list for multiples of ten such as `Twenty`, `Thirty`, and `Forty`.
3. Use a helper function to convert smaller parts of the number.
4. Handle numbers below `100` using tens and ones.
5. Handle numbers below `1000` using the `Hundred` format.
6. Divide larger numbers into groups such as `Thousand`, `Million`, and `Billion`.
7. Use the helper function again for each smaller group.
8. Add `Negative` when the input number is less than zero.
9. Handle `0` separately.
10. Combine the converted parts without adding unnecessary spaces.

## How It Works

For example, consider:

```text
12345
```

The number is divided into:

```text
12 Thousand
345
```

Then each part is converted:

```text
12     → Twelve
345    → Three Hundred Forty Five
```

Finally:

```text
Twelve Thousand Three Hundred Forty Five
```

## Technologies Used

* Python 3

## Complexity

The conversion works by breaking the number into groups of thousands, millions, and billions.

* **Time Complexity:** O(log n)
* **Space Complexity:** O(log n) because of the recursive function calls.

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Open the project folder

```bash
cd integer-to-english-words
```

### 3. Run the Python program

```bash
python main.py
```

### 4. Enter a number

```text
Enter a number: 12345
```

Output:

```text
Twelve Thousand Three Hundred Forty Five
```

## Project Structure

```text
integer-to-english-words/
│
├── main.py
└── README.md
```



## Author

**Lohith**

This project was created as a Python problem-solving practice project.

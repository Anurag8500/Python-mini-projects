# Text Analyzer

A command-line Python application that analyzes text and generates useful statistics about its structure, words, characters, sentences, paragraphs, and word frequency.

The project focuses on practical string processing, data cleaning, frequency analysis, and working with Python's core collection types.

## Features

* Analyze a block of text from the command line
* Count total characters
* Count characters excluding spaces
* Count words
* Count sentences
* Count paragraphs
* Count unique words
* Find the longest word
* Calculate average word length
* Calculate word frequencies
* Display the five most frequent words
* Normalize text for consistent word analysis
* Remove punctuation before processing words

## Concepts Practiced

* Variables and data types
* Strings
* String methods:

  * `.strip()`
  * `.lower()`
  * `.replace()`
  * `.split()`
* Lists
* Sets
* Dictionaries
* Dictionary methods:

  * `.items()`
* `for` loops
* Conditional statements
* List comprehensions
* Membership and filtering
* `len()`
* `sum()`
* `max()`
* `sorted()`
* `key=`
* `lambda`
* List slicing
* String formatting with f-strings
* Number formatting with `:.2f`
* Importing standard-library modules
* Basic text normalization
* Frequency counting
* Basic data aggregation

## How It Works

```text
Input text
    ↓
Normalize text
    ↓
Remove punctuation
    ↓
Split text into words
    ↓
Analyze characters, words and sentences
    ↓
Find unique words
    ↓
Build word-frequency dictionary
    ↓
Sort frequencies
    ↓
Calculate additional statistics
    ↓
Display analysis report
```

## Example

```text
=== Text Analyzer ===

Enter your text:
Python is powerful. Python is flexible and Python is easy to learn!

=== Text Analysis ===

Characters: 66
Characters (excluding spaces): 55
Words: 11
Sentences: 2
Paragraphs: 1
Unique words: 8
Longest word: powerful
Average word length: 4.91

Most frequent words:
- python: 3
- is: 3
- powerful: 1
- flexible: 1
- and: 1
```

The exact results depend on the text provided by the user.

## Data Processing Approach

The program normalizes the input before analyzing words.

For example:

```text
Python
python
PYTHON
```

are converted to the same lowercase representation.

Punctuation is also removed so that words such as:

```text
python
python,
python!
python.
```

are treated consistently during frequency analysis.

## What I Learned

* How to manipulate and clean strings
* The difference between `.strip()` and `.split()`
* How `.lower()` can normalize text
* How `replace()` can remove specific characters
* How sets can be used to identify unique values
* How dictionaries can be used to count frequencies
* How to use `sorted()` with `key=` and `lambda`
* How list slicing can limit displayed results
* How list comprehensions can filter and transform data
* How to combine multiple data-processing operations into a single workflow
* How to calculate statistics from processed text

## Limitations

This project is intentionally a basic text-analysis tool.

The sentence counter uses `.`, `!`, and `?` and therefore does not understand natural-language sentence boundaries.

The punctuation handling is also designed for basic text processing rather than advanced natural-language processing.

## Possible Improvements

* Analyze text from `.txt` files
* Add stop-word filtering
* Calculate character frequencies
* Search for a specific word
* Show the top 10 or top 20 words
* Compare two texts
* Calculate reading time
* Calculate sentence and word-length statistics
* Support multiple text files
* Export analysis results to JSON or CSV
* Refactor the program using reusable functions
* Add automated tests

## Project Structure

```text
06-text-analyzer/
│
├── main.py
└── README.md
```

## Status

**Completed — Phase 01: Python Core**

Project 06 of the Python Mini Projects curriculum.

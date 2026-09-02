# Project #12: Document Analyzer

A Python-based terminal application that analyzes a user-provided document and generates useful text and language statistics.

The project processes multi-line text and demonstrates how Python can be used to **clean, search, count, group, rank, and analyze textual data**.

This project builds on the text-processing concepts introduced in Project #06 and combines them with the filtering, sorting, aggregation, and reporting patterns developed throughout the previous projects.

## Features

* Enter a multi-line document through the terminal
* View the complete document
* Calculate basic document statistics
* Analyze word characteristics
* Analyze individual sentences
* Count word frequencies
* Display the most common words
* Search for words or phrases
* Show matching document lines
* Calculate unique-word statistics
* Identify repeated words
* Generate a detailed document report

## Concepts Practiced

### Text Processing

* String normalization
* `.lower()`
* `.strip()`
* `.replace()`
* `.split()`
* `.count()`
* Multi-line string processing
* Character-by-character processing

### Data Structures

* Lists
* Dictionaries
* Sets
* Lists of tuples
* Dictionary-based frequency tables

### Control Flow

* `while` loops
* `for` loops
* Nested loops
* `if / elif / else`
* `break`
* `continue`

### Data Analysis

* `len()`
* `sum()`
* `max()`
* `min()`
* `sorted()`
* `enumerate()`
* List comprehensions
* Dictionary comprehensions
* Generator expressions
* List slicing

### Functional Patterns

* `lambda`
* Sorting with custom keys
* Finding maximum/minimum values using `key=`

## How the Document Is Stored

The program collects the document one line at a time:

```python
lines = []
```

Each entered line is added to the list:

```python
lines.append(line)
```

When the user finishes, the lines are combined into one document:

```python
document = "\n".join(lines)
```

This allows the program to work with both:

* The complete document
* Individual lines

## Text Preparation

Before analyzing words, the document is normalized:

```python
normalized_document = document.lower()
```

Selected punctuation marks are removed so that words such as:

```text
Python,
Python.
Python!
```

can be treated as the same word during frequency analysis.

The cleaned text is then split into individual words:

```python
words = cleaned_document.split()
```

This produces a list of words that can be analyzed throughout the program.

## Basic Statistics

The application calculates several high-level document measurements:

* Total characters
* Characters excluding spaces and line breaks
* Total words
* Number of lines
* Number of sentences

Example:

```text
=== Basic Statistics ===

Characters: 425
Characters without spaces: 351
Words: 72
Lines: 8
Sentences: 6
```

## Word Statistics

The program analyzes the characteristics of individual words.

It calculates:

* Total number of words
* Longest word
* Shortest word
* Average word length

For example:

```python
longest_word = max(
    words,
    key=len
)
```

The `key=len` tells Python to compare words based on their length.

## Sentence Analysis

The program processes the document character by character and identifies sentences whenever it encounters:

```text
.
!
?
```

Each detected sentence is stored separately.

The program then calculates:

* Number of sentences
* Number of words in each sentence
* Average sentence length
* Longest sentence

Example:

```text
=== Sentence Analysis ===

Total sentences: 6

Sentence 1:
Text: Python is a programming language.
Words: 5

Sentence 2:
Text: It can be used for many different tasks.
Words: 8
```

This introduces a more detailed form of text parsing than the earlier projects.

## Word Frequency

The program builds a frequency dictionary to track how often each word occurs.

Example:

```python
word_frequency = {}

for word in words:
    word_frequency[word] = (
        word_frequency.get(word, 0) + 1
    )
```

For a document containing:

```text
python code python programming code
```

the frequency dictionary becomes conceptually:

```python
{
    "python": 2,
    "code": 2,
    "programming": 1
}
```

The program can then display the frequency of every word.

## Most Common Words

The frequency dictionary can also be sorted by occurrence count:

```python
ranked_words = sorted(
    word_frequency.items(),
    key=lambda item: item[1],
    reverse=True
)
```

The top ten words are then displayed.

Example:

```text
=== Most Common Words ===

1. python — 8 occurrences
2. code — 6 occurrences
3. project — 5 occurrences
4. data — 4 occurrences
5. program — 3 occurrences
```

This reinforces the ranking pattern used in previous projects.

## Search

The search feature allows the user to search for a word or phrase.

The search is case-insensitive because the document is normalized using:

```python
normalized_document = document.lower()
```

The program reports:

* Number of occurrences
* Lines containing the search term

Example:

```text
=== Search Results ===

'python' found 5 time(s).

Matching lines:

1: Python is a programming language.
4: I am currently learning Python.
7: This project analyzes Python text.
```

## Unique-Word Analysis

The program uses a `set` to identify unique words:

```python
unique_words = set(words)
```

Since sets automatically remove duplicate values, this makes it easy to determine how many different words are present.

The program calculates:

* Total words
* Unique words
* Unique-word percentage
* Number of repeated words
* Frequency of repeated words

Example:

```text
=== Unique-Word Analysis ===

Total words: 72
Unique words: 49
Unique-word percentage: 68.06%
Repeated words: 15
```

## Detailed Report

The detailed report combines the most useful metrics into a single summary.

It includes:

### Document Statistics

* Lines
* Sentences
* Words
* Characters
* Characters without spaces

### Word Analysis

* Unique words
* Unique-word percentage
* Longest word
* Shortest word
* Average word length
* Most common word

### Top Words

The report also displays the five most frequently used words.

Example:

```text
========================================
           DETAILED REPORT
========================================

Document statistics:
- Lines: 8
- Sentences: 6
- Words: 72
- Characters: 425
- Characters without spaces: 351

Word analysis:
- Unique words: 49
- Unique-word percentage: 68.06%
- Longest word: programming
- Shortest word: a
- Average word length: 5.21
- Most common word: python (8 occurrences)

Top 5 words:
1. python — 8
2. code — 6
3. project — 5
4. data — 4
5. program — 3
```

## Main Menu

```text
=== Menu ===
1. View document
2. Basic statistics
3. Word statistics
4. Sentence analysis
5. Word frequency
6. Most common words
7. Search document
8. Unique-word analysis
9. Detailed report
10. Exit
```

## Project Structure

```text
12-document-analyzer/
│
├── main.py
└── README.md
```

The project intentionally remains a single-file application at this point in the roadmap.

Custom functions and modular program design will be introduced in the next stage.

## How to Run

From the project directory:

```bash
python main.py
```

The program will ask you to enter the document line by line.

Press **Enter on an empty line** when you have finished entering the document.

## Example Workflow

A typical session can follow this sequence:

```text
Enter document
      ↓
View the document
      ↓
Check basic statistics
      ↓
Analyze words
      ↓
Analyze sentences
      ↓
Check word frequency
      ↓
Search for terms
      ↓
Analyze unique/repeated words
      ↓
Generate detailed report
```

## Learning Progression

Project #12 combines several patterns developed in previous projects:

```text
Project #06
Text processing
      ↓
Project #09
Searching + filtering
      ↓
Project #10
Sorting + aggregation
      ↓
Project #11
Grouping + statistical analysis
      ↓
Project #12
Document parsing + text analytics
```

The objective is to repeatedly reuse familiar Python concepts in increasingly realistic situations.

## What This Project Teaches

The main lesson is that raw text can be treated as structured data.

A document can be transformed into:

```text
Document
   ↓
Lines
   ↓
Sentences
   ↓
Words
   ↓
Unique words
   ↓
Word frequencies
   ↓
Rankings
   ↓
Statistics
   ↓
Report
```

This is an important foundation for later work involving log analysis, file processing, natural language processing, search systems, and backend data pipelines.

## Future Improvements

Possible extensions include:

* Read documents directly from text files
* Support more punctuation and special characters
* Improve sentence detection
* Ignore common stop words such as `the`, `is`, and `a`
* Add keyword density analysis
* Search by regular expressions
* Compare two documents
* Detect duplicate or similar text
* Export analysis reports
* Process multiple documents
* Add CSV/JSON report output

These improvements are intentionally reserved for later stages of the roadmap.

## Development Philosophy

This repository follows:

```text
Learn
  ↓
Build
  ↓
Break
  ↓
Debug
  ↓
Improve
  ↓
Understand
  ↓
Repeat
```

The goal is not simply to make the program work, but to understand why it works.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.

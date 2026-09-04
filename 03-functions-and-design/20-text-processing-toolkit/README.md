# Project #20: Text Processing Toolkit

A Python-based text-processing toolkit that provides reusable functions for cleaning, analyzing, searching, transforming, and summarizing text.

This project is part of **Phase 03 — Functions & Program Design** and builds directly on the document-analysis work from Project #12.

The primary focus is learning how to turn repeated text-processing logic into **small, reusable functions with clear inputs and outputs**.

## Features

* Enter and replace multi-line text
* View the current text
* Generate a cleaned-text preview
* Count words
* Count characters
* Count characters with or without spaces
* Calculate word frequencies
* Rank the most common words
* Find the longest word
* Find the shortest word
* Calculate average word length
* Count sentences
* Calculate unique-word statistics
* Search for words or phrases
* Search and replace text
* Extract frequently occurring keywords
* Generate a complete text-processing report

## Concepts Practiced

### Functions

* Function definitions
* Function calls
* Parameters
* Arguments
* Return values
* Default parameters
* Boolean values
* Helper functions
* Function composition
* Reusable utilities
* Separation of responsibilities

### Text Processing

* `.lower()`
* `.strip()`
* `.replace()`
* `.split()`
* `.join()`
* `.count()`
* Multi-line text processing
* Text normalization
* Search and replace

### Data Structures

* Lists
* Dictionaries
* Sets
* Tuples
* Lists of tuples
* Dictionary comprehensions

### Data Analysis

* `len()`
* `sum()`
* `max()`
* `min()`
* `sorted()`
* `enumerate()`
* List slicing
* Generator expressions
* Frequency counting
* Aggregation

### Validation and Control Flow

* `if / elif / else`
* `while` loops
* `for` loops
* `break`
* `continue`
* `try / except`
* Input validation

## Why This Project Exists

Project #12 implemented document analysis as part of a larger single-file application.

That approach worked, but many operations were tightly connected to the main program.

Project #20 reorganizes the same type of functionality into reusable functions.

Instead of:

```text
Text
 ↓
Large analysis block
 ↓
Output
```

the design becomes:

```text
Text
 ↓
Reusable processing functions
 ↓
Returned data
 ↓
Display / reporting functions
```

This makes the logic easier to reuse in other applications.

## Main Menu

```text
=== Menu ===
1. Enter / replace text
2. View current text
3. Clean text preview
4. Count words
5. Count characters
6. Word frequency
7. Most common words
8. Longest / shortest words
9. Text statistics
10. Search text
11. Search and replace
12. Extract keywords
13. Full report
14. Exit
```

## Text Input

The application supports multi-line text input.

The user enters lines individually and presses Enter on an empty line to finish.

The lines are then combined using:

```python
"\n".join(lines)
```

This allows the toolkit to retain the original line structure while still working with the entire document.

## Text Cleaning

The toolkit provides:

```python
clean_text(text)
```

which:

* Converts text to lowercase
* Removes common punctuation

For example:

```text
"Python, Python! Code."
```

becomes:

```text
"python python code"
```

This creates a normalized representation that can be used for analysis.

## Word Extraction

The function:

```python
get_words(text)
```

first cleans the text and then splits it into individual words.

For example:

```text
Python is useful.
```

becomes conceptually:

```python
[
    "python",
    "is",
    "useful"
]
```

This word list is reused by several other functions.

## Word Counting

The toolkit provides:

```python
count_words(text)
```

which returns the total number of words.

Example:

```python
count_words("Python is fun")
```

returns:

```text
3
```

The calculation itself is separate from displaying the result.

## Character Counting

The function:

```python
count_characters(text, include_spaces=True)
```

supports two modes.

With spaces:

```python
count_characters(text)
```

counts every character.

Without spaces:

```python
count_characters(text, False)
```

removes spaces and line breaks before counting.

This introduces the use of a **default parameter**.

## Word Frequency

The function:

```python
calculate_word_frequency(text)
```

creates a frequency dictionary.

For example:

```text
python code python data code python
```

produces conceptually:

```python
{
    "python": 3,
    "code": 2,
    "data": 1
}
```

The frequency-counting pattern is:

```python
word_frequency[word] = (
    word_frequency.get(word, 0) + 1
)
```

This is reused from previous projects but is now encapsulated inside a function.

## Sorted Word Frequency

The function:

```python
get_sorted_word_frequency(text)
```

takes the frequency dictionary and sorts it by occurrence count.

For example:

```python
[
    ("python", 3),
    ("code", 2),
    ("data", 1)
]
```

The function can also control sort direction using:

```python
descending=True
```

This demonstrates how parameters can control function behavior.

## Most Common Words

The toolkit can display the most frequently used words.

For example:

```text
=== Top 5 Words ===

1. python — 8 occurrences
2. code — 6 occurrences
3. project — 5 occurrences
4. data — 4 occurrences
5. program — 3 occurrences
```

The result is produced by sorting the frequency data and applying list slicing:

```python
sorted_frequency[:limit]
```

## Longest and Shortest Words

The toolkit provides:

```python
find_longest_word(text)
find_shortest_word(text)
```

Both functions use `max()` and `min()` with a custom key:

```python
max(words, key=len)
```

This returns the word with the greatest length rather than the lexicographically largest word.

## Average Word Length

The function:

```python
calculate_average_word_length(text)
```

calculates:

```text
Total characters in all words
──────────────────────────────
       Number of words
```

For example, if the words contain a total of 50 characters and there are 10 words:

```text
50 / 10 = 5
```

The average word length is therefore 5 characters.

## Sentence Counting

The toolkit estimates sentence count by looking for:

```text
.
!
?
```

For example:

```text
Hello! How are you? I am fine.
```

contains three sentence-ending marks and therefore produces:

```text
3 sentences
```

This remains a simple text-processing approximation rather than a full natural-language sentence parser.

## Unique-Word Analysis

The function:

```python
get_unique_words(text)
```

uses a set to remove duplicate words.

For example:

```text
python python code code data
```

becomes:

```python
{
    "python",
    "code",
    "data"
}
```

The toolkit also calculates the percentage of unique words:

```text
Unique words
──────────── × 100
Total words
```

This gives a simple measure of vocabulary variety within the text.

## Searching Text

The function:

```python
search_text(text, search_term)
```

counts occurrences of a word or phrase.

Searching is case-insensitive.

For example:

```python
search_text(
    "Python is useful. Python is popular.",
    "python"
)
```

returns:

```text
2
```

## Search and Replace

The function:

```python
replace_text(
    text,
    search_term,
    replacement
)
```

returns a new version of the text after replacement.

Example:

```text
Search: Python
Replacement: Java
```

can transform:

```text
Python is useful.
```

into:

```text
Java is useful.
```

The function returns the modified text rather than printing it directly.

## Keyword Extraction

The function:

```python
extract_keywords(
    text,
    minimum_frequency=2
)
```

returns words that occur at least the specified number of times.

For example, with:

```text
python code python data python code
```

and:

```python
minimum_frequency=2
```

the result becomes conceptually:

```python
[
    ("python", 3),
    ("code", 2)
]
```

This provides a simple way to identify repeated terms that may be useful as keywords.

## Text Statistics

The function:

```python
calculate_text_statistics(text)
```

returns a dictionary containing several measurements:

```python
{
    "characters": ...,
    "characters_without_spaces": ...,
    "words": ...,
    "sentences": ...,
    "unique_words": ...,
    "average_word_length": ...,
    "unique_word_percentage": ...
}
```

The important design idea is that the function **returns structured data** instead of directly printing it.

Another function can then decide how that data should be presented.

## Separation of Processing and Display

One of the main lessons of this project is separating computation from presentation.

For example:

```text
calculate_word_frequency()
        ↓
returns dictionary
        ↓
display_word_frequency()
        ↓
prints formatted output
```

Similarly:

```text
calculate_text_statistics()
        ↓
returns statistics
        ↓
display_text_statistics()
        ↓
prints statistics
```

This makes the processing functions reusable in programs that might not use terminal output.

## Function Composition

Functions in the toolkit can call other functions.

For example:

```text
display_full_report()
        ↓
calculate_text_statistics()
        ↓
count_characters()
get_words()
count_sentences()
calculate_average_word_length()
        ↓
return structured results
```

This demonstrates **function composition**: larger operations can be built from smaller reusable operations.

## Default Parameters

The project introduces default arguments.

For example:

```python
def count_characters(
    text,
    include_spaces=True
):
```

Normally:

```python
count_characters(text)
```

counts spaces.

But:

```python
count_characters(
    text,
    False
)
```

excludes spaces and line breaks.

Similarly:

```python
get_sorted_word_frequency(
    text,
    descending=True
)
```

allows the caller to change the sorting direction.

## Full Report

The full report combines the main text-processing functions into one output.

It includes:

### Text Statistics

* Characters
* Characters without spaces
* Words
* Sentences
* Unique words

### Word Analysis

* Longest word
* Shortest word
* Average word length
* Unique-word percentage
* Most common word

### Top Words

The five most frequent words are displayed.

Example:

```text
========================================
        TEXT PROCESSING REPORT
========================================

Text statistics:
- Characters: 425
- Characters without spaces: 351
- Words: 72
- Sentences: 6
- Unique words: 49

Word analysis:
- Longest word: programming
- Shortest word: a
- Average word length: 5.21
- Unique-word percentage: 68.06%
- Most common word: python (8 occurrences)

Top 5 words:
1. python — 8
2. code — 6
3. project — 5
4. data — 4
5. program — 3
```

## Project Structure

```text
20-text-processing-toolkit/
│
├── main.py
└── README.md
```

The project is still contained in a single file intentionally.

The important change is that the code is now internally organized around reusable functions.

Later projects will separate these functions into modules and eventually packages.

## How to Run

From the project directory:

```bash
python main.py
```

Make sure your Python virtual environment is activated before running the project.

## Example Workflow

```text
Enter text
    ↓
Clean / normalize
    ↓
Extract words
    ↓
Count and analyze
    ↓
Search / replace
    ↓
Extract repeated keywords
    ↓
Generate report
```

## Learning Progression

Project #20 builds directly on Projects #06 and #12:

```text
Project #06
Basic text analysis
        ↓
Project #12
Document parsing + text analytics
        ↓
Project #18
Functions + modular program structure
        ↓
Project #19
Reusable validation functions
        ↓
Project #20
Reusable text-processing functions
```

The focus is now shifting from simply writing working programs to designing **small pieces of reusable functionality**.

## Why This Project Matters

Text-processing operations are useful in many types of software:

```text
Search systems
Log analyzers
Document processors
CLI tools
Data pipelines
NLP applications
Backend services
Content analysis tools
```

The larger lesson is not just how to count words.

It is learning how to take a useful operation such as:

```text
clean text
count words
calculate frequency
search text
```

and turn it into a reusable function that another part of the program can call.

## Future Improvements

Possible extensions include:

* Remove stop words
* Support configurable punctuation rules
* Add regular-expression searching
* Analyze paragraphs
* Compare two texts
* Add text similarity analysis
* Calculate keyword density
* Export reports
* Process text files
* Process multiple documents
* Move utilities into a separate module
* Add type hints
* Add unit tests
* Package the toolkit for reuse

These improvements will be introduced progressively as the roadmap moves toward modular packages, file processing, testing, and production-quality Python applications.

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

The objective is to understand not only what each function does, but also why the program is divided into separate responsibilities.

> Never commit code you cannot explain.

AI can be used as a teacher, debugging assistant, or pair programmer, but the core logic of every project should remain understandable to the developer.

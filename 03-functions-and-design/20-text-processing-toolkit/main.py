print("=== Text Processing Toolkit ===")


# ============================================================
# Text Processing Functions
# ============================================================

def clean_text(text):
    """
    Normalize text by converting it to lowercase
    and removing common punctuation.
    """

    punctuation_marks = ".,!?;:\"'()[]{}-_/"

    cleaned_text = text.lower()

    for mark in punctuation_marks:
        cleaned_text = cleaned_text.replace(mark, "")

    return cleaned_text


def get_words(text):
    """
    Convert text into a list of words.
    """

    return clean_text(text).split()


def count_words(text):
    """
    Return the total number of words.
    """

    words = get_words(text)

    return len(words)


def count_characters(text, include_spaces=True):
    """
    Count characters in the text.

    include_spaces=True
    counts all characters.

    include_spaces=False
    excludes spaces and line breaks.
    """

    if include_spaces:
        return len(text)

    return len(
        text.replace(" ", "").replace("\n", "")
    )


def calculate_word_frequency(text):
    """
    Return a dictionary containing word frequencies.
    """

    words = get_words(text)

    word_frequency = {}

    for word in words:

        word_frequency[word] = (
            word_frequency.get(word, 0) + 1
        )

    return word_frequency


def get_sorted_word_frequency(
    text,
    descending=True
):
    """
    Return word frequencies sorted by occurrence count.
    """

    word_frequency = calculate_word_frequency(text)

    return sorted(
        word_frequency.items(),
        key=lambda item: item[1],
        reverse=descending
    )


def find_longest_word(text):
    """
    Return the longest word in the text.
    """

    words = get_words(text)

    if not words:
        return None

    return max(
        words,
        key=len
    )


def find_shortest_word(text):
    """
    Return the shortest word in the text.
    """

    words = get_words(text)

    if not words:
        return None

    return min(
        words,
        key=len
    )


def calculate_average_word_length(text):
    """
    Return the average number of characters per word.
    """

    words = get_words(text)

    if not words:
        return 0

    total_characters = sum(
        len(word)
        for word in words
    )

    return total_characters / len(words)


def count_sentences(text):
    """
    Estimate the number of sentences based on
    '.', '!' and '?'.
    """

    return sum(
        text.count(mark)
        for mark in [".", "!", "?"]
    )


def get_unique_words(text):
    """
    Return a set containing unique words.
    """

    return set(
        get_words(text)
    )


def calculate_unique_word_percentage(text):
    """
    Return the percentage of words that are unique.
    """

    words = get_words(text)

    if not words:
        return 0

    unique_words = set(words)

    return (
        len(unique_words)
        / len(words)
        * 100
    )


def search_text(text, search_term):
    """
    Find occurrences of a word or phrase.
    """

    if not search_term.strip():
        return 0

    return text.lower().count(
        search_term.lower()
    )


def replace_text(
    text,
    search_term,
    replacement
):
    """
    Replace occurrences of a word or phrase.
    """

    return text.replace(
        search_term,
        replacement
    )


def extract_keywords(
    text,
    minimum_frequency=2
):
    """
    Return words that occur at least
    minimum_frequency times.
    """

    word_frequency = calculate_word_frequency(text)

    keywords = {
        word: frequency
        for word, frequency
        in word_frequency.items()
        if frequency >= minimum_frequency
    }

    return sorted(
        keywords.items(),
        key=lambda item: item[1],
        reverse=True
    )


def calculate_text_statistics(text):
    """
    Return a dictionary containing
    major text statistics.
    """

    words = get_words(text)

    return {
        "characters": count_characters(text),
        "characters_without_spaces": count_characters(
            text,
            include_spaces=False
        ),
        "words": len(words),
        "sentences": count_sentences(text),
        "unique_words": len(set(words)),
        "average_word_length": (
            calculate_average_word_length(text)
        ),
        "unique_word_percentage": (
            calculate_unique_word_percentage(text)
        )
    }


# ============================================================
# Display Functions
# ============================================================

def display_word_frequency(text):
    """
    Display word frequencies.
    """

    print("\n=== Word Frequency ===")

    sorted_frequency = get_sorted_word_frequency(
        text
    )

    if not sorted_frequency:
        print("No words found.")
        return

    for word, frequency in sorted_frequency:

        print(
            f"- {word}: "
            f"{frequency}"
        )


def display_top_words(text, limit=10):
    """
    Display the most frequently occurring words.
    """

    print(
        f"\n=== Top {limit} Words ==="
    )

    sorted_frequency = get_sorted_word_frequency(
        text
    )


    for rank, (word, frequency) in enumerate(
        sorted_frequency[:limit],
        start=1
    ):

        print(
            f"{rank}. "
            f"{word} — "
            f"{frequency} occurrences"
        )


def display_text_statistics(text):
    """
    Display major text statistics.
    """

    statistics = calculate_text_statistics(
        text
    )


    print("\n=== Text Statistics ===")

    print(
        f"Characters: "
        f"{statistics['characters']}"
    )

    print(
        f"Characters without spaces: "
        f"{statistics['characters_without_spaces']}"
    )

    print(
        f"Words: "
        f"{statistics['words']}"
    )

    print(
        f"Sentences: "
        f"{statistics['sentences']}"
    )

    print(
        f"Unique words: "
        f"{statistics['unique_words']}"
    )

    print(
        f"Average word length: "
        f"{statistics['average_word_length']:.2f}"
    )

    print(
        f"Unique-word percentage: "
        f"{statistics['unique_word_percentage']:.2f}%"
    )


def display_full_report(text):
    """
    Display a complete text-processing report.
    """

    words = get_words(text)


    if not words:

        print("\nNo words found.")
        return


    statistics = calculate_text_statistics(
        text
    )


    longest_word = find_longest_word(
        text
    )

    shortest_word = find_shortest_word(
        text
    )


    sorted_frequency = get_sorted_word_frequency(
        text
    )


    most_common_word = sorted_frequency[0]


    print("\n========================================")
    print("        TEXT PROCESSING REPORT")
    print("========================================")


    print("\nText statistics:")

    print(
        f"- Characters: "
        f"{statistics['characters']}"
    )

    print(
        f"- Characters without spaces: "
        f"{statistics['characters_without_spaces']}"
    )

    print(
        f"- Words: "
        f"{statistics['words']}"
    )

    print(
        f"- Sentences: "
        f"{statistics['sentences']}"
    )

    print(
        f"- Unique words: "
        f"{statistics['unique_words']}"
    )


    print("\nWord analysis:")

    print(
        f"- Longest word: "
        f"{longest_word}"
    )

    print(
        f"- Shortest word: "
        f"{shortest_word}"
    )

    print(
        f"- Average word length: "
        f"{statistics['average_word_length']:.2f}"
    )

    print(
        f"- Unique-word percentage: "
        f"{statistics['unique_word_percentage']:.2f}%"
    )

    print(
        f"- Most common word: "
        f"{most_common_word[0]} "
        f"({most_common_word[1]} occurrences)"
    )


    print("\nTop 5 words:")


    for rank, (word, frequency) in enumerate(
        sorted_frequency[:5],
        start=1
    ):

        print(
            f"{rank}. "
            f"{word} — "
            f"{frequency}"
        )


# ============================================================
# Interactive Operations
# ============================================================

def enter_text():
    """
    Read multi-line text from the user.
    """

    print("\nEnter your text.")
    print(
        "Press Enter on an empty line "
        "when finished."
    )


    lines = []


    while True:

        line = input()

        if line == "":
            break

        lines.append(line)


    return "\n".join(lines)


def search_text_interactively(text):
    """
    Search the current text interactively.
    """

    print("\n=== Search Text ===")


    search_term = input(
        "Enter word or phrase: "
    ).strip()


    if not search_term:

        print(
            "Search term cannot be empty."
        )

        return


    occurrences = search_text(
        text,
        search_term
    )


    if occurrences == 0:

        print(
            f"'{search_term}' was not found."
        )

    else:

        print(
            f"'{search_term}' found "
            f"{occurrences} time(s)."
        )


def replace_text_interactively(text):
    """
    Search and replace text interactively.
    """

    print("\n=== Search and Replace ===")


    search_term = input(
        "Text to find: "
    )


    if not search_term:

        print(
            "Search term cannot be empty."
        )

        return text


    replacement = input(
        "Replacement text: "
    )


    updated_text = replace_text(
        text,
        search_term,
        replacement
    )


    if updated_text == text:

        print(
            "No matching text was found."
        )

    else:

        print(
            "Text replaced successfully."
        )


    return updated_text


def display_keywords(text):
    """
    Display repeated words as keywords.
    """

    print("\n=== Keywords ===")


    while True:

        try:

            minimum_frequency = int(
                input(
                    "Minimum frequency: "
                ).strip()
            )


            if minimum_frequency < 1:

                print(
                    "Frequency must be at least 1."
                )

                continue


            break


        except ValueError:

            print(
                "Please enter a valid number."
            )


    keywords = extract_keywords(
        text,
        minimum_frequency
    )


    if not keywords:

        print(
            "No words matched the frequency."
        )

        return


    for rank, (word, frequency) in enumerate(
        keywords,
        start=1
    ):

        print(
            f"{rank}. "
            f"{word} — "
            f"{frequency}"
        )


# ============================================================
# Main Program
# ============================================================

text = ""


while True:

    print("\n=== Menu ===")
    print("1. Enter / replace text")
    print("2. View current text")
    print("3. Clean text preview")
    print("4. Count words")
    print("5. Count characters")
    print("6. Word frequency")
    print("7. Most common words")
    print("8. Longest / shortest words")
    print("9. Text statistics")
    print("10. Search text")
    print("11. Search and replace")
    print("12. Extract keywords")
    print("13. Full report")
    print("14. Exit")


    choice = input(
        "Choose an option: "
    ).strip()


    if choice == "1":

        text = enter_text()

        if text:

            print(
                "\nText stored successfully."
            )

        else:

            print(
                "\nNo text was entered."
            )


    elif choice == "2":

        print("\n=== Current Text ===")

        if text:

            print(text)

        else:

            print("No text has been entered.")


    elif choice == "3":

        if not text:

            print("No text has been entered.")
            continue


        cleaned_text = clean_text(text)


        print("\n=== Cleaned Text ===")
        print(cleaned_text)


    elif choice == "4":

        if not text:

            print("No text has been entered.")
            continue


        print(
            f"\nWord count: "
            f"{count_words(text)}"
        )


    elif choice == "5":

        if not text:

            print("No text has been entered.")
            continue


        print("\n=== Character Count ===")

        print(
            f"With spaces: "
            f"{count_characters(text)}"
        )

        print(
            f"Without spaces: "
            f"{count_characters(text, False)}"
        )


    elif choice == "6":

        if not text:

            print("No text has been entered.")
            continue


        display_word_frequency(text)


    elif choice == "7":

        if not text:

            print("No text has been entered.")
            continue


        while True:

            try:

                limit = int(
                    input(
                        "How many words to display? "
                    ).strip()
                )


                if limit <= 0:

                    print(
                        "Enter a number greater than 0."
                    )

                    continue


                break


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        display_top_words(
            text,
            limit
        )


    elif choice == "8":

        if not text:

            print("No text has been entered.")
            continue


        longest_word = find_longest_word(text)
        shortest_word = find_shortest_word(text)


        if longest_word is None:

            print("No words found.")

        else:

            print(
                f"\nLongest word: "
                f"{longest_word}"
            )

            print(
                f"Shortest word: "
                f"{shortest_word}"
            )


    elif choice == "9":

        if not text:

            print("No text has been entered.")
            continue


        display_text_statistics(text)


    elif choice == "10":

        if not text:

            print("No text has been entered.")
            continue


        search_text_interactively(text)


    elif choice == "11":

        if not text:

            print("No text has been entered.")
            continue


        text = replace_text_interactively(
            text
        )


    elif choice == "12":

        if not text:

            print("No text has been entered.")
            continue


        display_keywords(text)


    elif choice == "13":

        if not text:

            print("No text has been entered.")
            continue


        display_full_report(text)


    elif choice == "14":

        print("\nGoodbye!")
        break


    else:

        print(
            "Invalid option. "
            "Please choose between 1 and 14."
        )
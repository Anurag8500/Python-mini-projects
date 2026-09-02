print("=== Document Analyzer ===")


# ============================================================
# Document Input
# ============================================================

print("\nEnter your document.")
print("Press Enter on an empty line when you are finished.")

lines = []

while True:
    line = input()

    if line == "":
        break

    lines.append(line)


# Join all lines into one document
document = "\n".join(lines)


if not document.strip():
    print("\nNo document was entered.")
else:

    # ========================================================
    # Text Preparation
    # ========================================================

    normalized_document = document.lower()

    punctuation_marks = ".,!?;:\"'()[]{}-_/"

    cleaned_document = normalized_document

    for mark in punctuation_marks:
        cleaned_document = cleaned_document.replace(mark, "")


    words = cleaned_document.split()


    # ========================================================
    # Main Menu
    # ========================================================

    while True:

        print("\n=== Menu ===")
        print("1. View document")
        print("2. Basic statistics")
        print("3. Word statistics")
        print("4. Sentence analysis")
        print("5. Word frequency")
        print("6. Most common words")
        print("7. Search document")
        print("8. Unique-word analysis")
        print("9. Detailed report")
        print("10. Exit")

        choice = input("Choose an option: ").strip()


        # ====================================================
        # VIEW DOCUMENT
        # ====================================================

        if choice == "1":

            print("\n=== Document ===")
            print(document)


        # ====================================================
        # BASIC STATISTICS
        # ====================================================

        elif choice == "2":

            character_count = len(document)

            character_count_without_spaces = len(
                document.replace(" ", "").replace("\n", "")
            )

            word_count = len(words)

            line_count = len(lines)

            sentence_count = sum(
                document.count(mark)
                for mark in [".", "!", "?"]
            )


            print("\n=== Basic Statistics ===")

            print(
                f"Characters: "
                f"{character_count}"
            )

            print(
                f"Characters without spaces: "
                f"{character_count_without_spaces}"
            )

            print(
                f"Words: "
                f"{word_count}"
            )

            print(
                f"Lines: "
                f"{line_count}"
            )

            print(
                f"Sentences: "
                f"{sentence_count}"
            )


        # ====================================================
        # WORD STATISTICS
        # ====================================================

        elif choice == "3":

            if not words:
                print("No words found.")
                continue


            longest_word = max(
                words,
                key=len
            )

            shortest_word = min(
                words,
                key=len
            )


            total_word_characters = sum(
                len(word)
                for word in words
            )


            average_word_length = (
                total_word_characters
                / len(words)
            )


            print("\n=== Word Statistics ===")

            print(
                f"Total words: "
                f"{len(words)}"
            )

            print(
                f"Longest word: "
                f"{longest_word} "
                f"({len(longest_word)} characters)"
            )

            print(
                f"Shortest word: "
                f"{shortest_word} "
                f"({len(shortest_word)} characters)"
            )

            print(
                f"Average word length: "
                f"{average_word_length:.2f}"
            )


        # ====================================================
        # SENTENCE ANALYSIS
        # ====================================================

        elif choice == "4":

            sentences = []

            current_sentence = ""

            for character in document:

                current_sentence += character

                if character in ".!?":

                    sentence = current_sentence.strip()

                    if sentence:
                        sentences.append(sentence)

                    current_sentence = ""


            if current_sentence.strip():
                sentences.append(
                    current_sentence.strip()
                )


            if not sentences:
                print("No sentences found.")
                continue


            print("\n=== Sentence Analysis ===")

            print(
                f"Total sentences: "
                f"{len(sentences)}"
            )


            sentence_lengths = []


            for number, sentence in enumerate(
                sentences,
                start=1
            ):

                sentence_words = sentence.split()

                word_count = len(sentence_words)

                sentence_lengths.append(word_count)


                print(
                    f"\nSentence {number}:"
                )

                print(
                    f"Text: {sentence}"
                )

                print(
                    f"Words: {word_count}"
                )


            average_sentence_length = (
                sum(sentence_lengths)
                / len(sentence_lengths)
            )


            longest_sentence = max(
                sentences,
                key=lambda sentence: len(sentence.split())
            )


            print(
                f"\nAverage sentence length: "
                f"{average_sentence_length:.2f} words"
            )

            print(
                f"Longest sentence: "
                f"{longest_sentence}"
            )


        # ====================================================
        # WORD FREQUENCY
        # ====================================================

        elif choice == "5":

            if not words:
                print("No words found.")
                continue


            word_frequency = {}


            for word in words:

                word_frequency[word] = (
                    word_frequency.get(word, 0) + 1
                )


            print("\n=== Word Frequency ===")


            for word, frequency in sorted(
                word_frequency.items(),
                key=lambda item: item[0]
            ):

                print(
                    f"{word}: "
                    f"{frequency}"
                )


        # ====================================================
        # MOST COMMON WORDS
        # ====================================================

        elif choice == "6":

            if not words:
                print("No words found.")
                continue


            word_frequency = {}


            for word in words:

                word_frequency[word] = (
                    word_frequency.get(word, 0) + 1
                )


            ranked_words = sorted(
                word_frequency.items(),
                key=lambda item: item[1],
                reverse=True
            )


            print("\n=== Most Common Words ===")


            for rank, (word, frequency) in enumerate(
                ranked_words[:10],
                start=1
            ):

                print(
                    f"{rank}. "
                    f"{word} — "
                    f"{frequency} occurrences"
                )


        # ====================================================
        # SEARCH DOCUMENT
        # ====================================================

        elif choice == "7":

            search_term = input(
                "Enter a word or phrase to search: "
            ).strip().lower()


            if not search_term:
                print("Search term cannot be empty.")
                continue


            occurrences = normalized_document.count(
                search_term
            )


            print("\n=== Search Results ===")


            if occurrences == 0:

                print(
                    f"'{search_term}' was not found."
                )

            else:

                print(
                    f"'{search_term}' found "
                    f"{occurrences} time(s)."
                )


                matching_lines = []

                for number, line in enumerate(
                    lines,
                    start=1
                ):

                    if search_term in line.lower():

                        matching_lines.append(
                            (number, line)
                        )


                print("\nMatching lines:")


                for number, line in matching_lines:

                    print(
                        f"{number}: {line}"
                    )


        # ====================================================
        # UNIQUE-WORD ANALYSIS
        # ====================================================

        elif choice == "8":

            if not words:
                print("No words found.")
                continue


            unique_words = set(words)


            unique_percentage = (
                len(unique_words)
                / len(words)
                * 100
            )


            repeated_words = {
                word: frequency
                for word, frequency in (
                    {
                        word: words.count(word)
                        for word in unique_words
                    }
                ).items()
                if frequency > 1
            }


            print("\n=== Unique-Word Analysis ===")

            print(
                f"Total words: "
                f"{len(words)}"
            )

            print(
                f"Unique words: "
                f"{len(unique_words)}"
            )

            print(
                f"Unique-word percentage: "
                f"{unique_percentage:.2f}%"
            )


            print(
                f"Repeated words: "
                f"{len(repeated_words)}"
            )


            if repeated_words:

                print("\nRepeated words:")

                repeated_words_sorted = sorted(
                    repeated_words.items(),
                    key=lambda item: item[1],
                    reverse=True
                )


                for word, frequency in repeated_words_sorted:

                    print(
                        f"- {word}: "
                        f"{frequency}"
                    )


        # ====================================================
        # DETAILED REPORT
        # ====================================================

        elif choice == "9":

            if not words:
                print("No words found.")
                continue


            # Basic counts

            character_count = len(document)

            character_count_without_spaces = len(
                document.replace(" ", "").replace("\n", "")
            )

            word_count = len(words)

            line_count = len(lines)

            sentence_count = sum(
                document.count(mark)
                for mark in [".", "!", "?"]
            )


            # Word statistics

            longest_word = max(
                words,
                key=len
            )

            shortest_word = min(
                words,
                key=len
            )


            total_word_characters = sum(
                len(word)
                for word in words
            )


            average_word_length = (
                total_word_characters
                / word_count
            )


            # Word frequency

            word_frequency = {}


            for word in words:

                word_frequency[word] = (
                    word_frequency.get(word, 0) + 1
                )


            most_common_word = max(
                word_frequency.items(),
                key=lambda item: item[1]
            )


            unique_word_count = len(
                set(words)
            )


            unique_percentage = (
                unique_word_count
                / word_count
                * 100
            )


            print("\n========================================")
            print("           DETAILED REPORT")
            print("========================================")


            print("\nDocument statistics:")

            print(
                f"- Lines: "
                f"{line_count}"
            )

            print(
                f"- Sentences: "
                f"{sentence_count}"
            )

            print(
                f"- Words: "
                f"{word_count}"
            )

            print(
                f"- Characters: "
                f"{character_count}"
            )

            print(
                f"- Characters without spaces: "
                f"{character_count_without_spaces}"
            )


            print("\nWord analysis:")

            print(
                f"- Unique words: "
                f"{unique_word_count}"
            )

            print(
                f"- Unique-word percentage: "
                f"{unique_percentage:.2f}%"
            )

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
                f"{average_word_length:.2f}"
            )

            print(
                f"- Most common word: "
                f"{most_common_word[0]} "
                f"({most_common_word[1]} occurrences)"
            )


            print("\nTop 5 words:")


            top_words = sorted(
                word_frequency.items(),
                key=lambda item: item[1],
                reverse=True
            )[:5]


            for rank, (word, frequency) in enumerate(
                top_words,
                start=1
            ):

                print(
                    f"{rank}. "
                    f"{word} — "
                    f"{frequency}"
                )


        # ====================================================
        # EXIT
        # ====================================================

        elif choice == "10":

            print("\nGoodbye!")
            break


        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print(
                "Invalid option. "
                "Please choose between 1 and 10."
            )
import string

print("=== Text Analyzer ===")

text = input("\nEnter your text:\n").strip()

if not text:
    print("No text was entered.")
else:
    # Normalize the text
    normalized_text = text.lower()

    # Remove punctuation for word analysis
    text_without_punctuation = normalized_text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Split text into words
    words = text_without_punctuation.split()

    # Basic character analysis
    character_count = len(text)
    character_count_without_spaces = len(
        text.replace(" ", "")
    )

    # Word and sentence analysis
    word_count = len(words)
    sentence_count = sum(
        text.count(mark)
        for mark in [".", "!", "?"]
    )

    # Paragraph analysis
    paragraphs = [
        paragraph
        for paragraph in text.split("\n")
        if paragraph.strip()
    ]

    paragraph_count = len(paragraphs)

    # Unique words
    unique_words = set(words)

    # Word frequency
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0

        word_frequency[word] += 1   

    # Most frequent words
    sorted_word_frequency = sorted(
        word_frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    # Longest word
    longest_word = max(words, key=len)

    # Average word length
    total_word_characters = sum(len(word) for word in words)
    average_word_length = total_word_characters / word_count

    # Display results
    print("\n=== Text Analysis ===")

    print(f"Characters: {character_count}")
    print(
        f"Characters (excluding spaces): "
        f"{character_count_without_spaces}"
    )
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Paragraphs: {paragraph_count}")
    print(f"Unique words: {len(unique_words)}")
    print(f"Longest word: {longest_word}")
    print(f"Average word length: {average_word_length:.2f}")

    print("\nMost frequent words:")

    for word, frequency in sorted_word_frequency[:5]:
        print(f"- {word}: {frequency}")


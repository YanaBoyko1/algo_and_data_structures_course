def longest_chain(words):
    """
    Finds the length of the longest chain of words by removing one letter from each word.
    Args:
        words (list): List of words.
    Returns:
        int: Length of the longest chain.
    """
    dict = {word: 1 for word in words}
    for current_word in sorted(words[::-1], key=len):
        for index in range(len(current_word)):
            next_word = current_word[:index] + current_word[index + 1:]
            if next_word in dict:
                dict[current_word] = max(dict[current_word], dict[next_word] + 1)

    return max(dict.values())


def read_input(file_path):
    """
    Reads words from the specified file.
    Args:
        file_path (str): Path to the file containing words.
    Returns:
        list: List of words.
    """
    with open(file_path, "r") as file:
        words = [line.strip() for line in file.readlines()]
    return words


def write_output(file_path, result):
    """
    Writes the result to the specified file.
    Args:
        file_path (str): Path to the file for writing the result.
        result (int): Result to write.
    Returns:
        None
    """
    with open(file_path, "w") as file:
        file.write(str(result))


def process_file(input_file, output_file):
    """
    Reads words from the input file, finds the length of the longest chain of words,
    and writes the result to the output file.
    Args:
        input_file (str): Path to the file containing words.
        output_file (str): Path to the file for writing the result.
    Returns:
        None
    """

    words = read_input(input_file)
    result = longest_chain(words)
    write_output(output_file, result)

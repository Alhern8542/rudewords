import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def bleeper(word):
    # Write code to replace rude words with asterisks
    new_word = []
    for character in word:
        if character not in string.punctuation:
            new_word.append("*")
        else:
            new_word.append(character)
    return "".join(new_word)


def check_line(line):
    rude_count = 0
    word_index = 0
    words = line.split(" ")
    for word in words:
        stripped_word = word.strip(string.punctuation).lower()
        if stripped_word in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")
            words[word_index] = bleeper(word)
        word_index += 1
    line = " ".join(words)
    return line, rude_count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        lines = []
        for line in myfile:
            line, rude_subtotal = check_line(line)
            rude_count += rude_subtotal
            lines.append(line)
    if rude_count == 0:
        print("Congratulations, your file has no rude words.")
        print("At least, no rude words I know.")
    else:
        with open("bleeped_copy.txt", "w") as bleep_copy:
            bleep_copy.write("\n".join(lines))
        print(f"Found {rude_count} rude words in file. See bleeped_copy.txt for censored copy")


if __name__ == "__main__":
    check_file("my_other_story.txt")
from num2words import num2words

from hw1_v2 import num_to_words


def test_check_word(num: int):
    word1 = num_to_words(num)
    word2 = num2words(num, lang='ru')
    try:
        assert word1.__eq__(word2)
    except AssertionError:
        print(f"{str(num)} -> {word1}")


def main():
    for n in range(10000, 100000):
        test_check_word(n)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_word_occurrences(text):
    num_words = {}
    text_list = text.split()

    for word in text_list:
        word = word.lower().strip()
        num_words[word] = num_words.get(word, 0) + 1

    return num_words

def main():
    # Văn bản cần đếm số lần xuất hiện từ
    message = "This is a sample text. This text contains some repeated words. Words are important."

    # Gọi hàm đếm từ và truyền message làm tham số
    word_occurrences = count_word_occurrences(message)

    # In ra kết quả
    print("Số lần xuất hiện của các từ trong văn bản:")
    for word, count in word_occurrences.items():
        print(f"'{word}': {count} lần")

if __name__ == "__main__":
    main()


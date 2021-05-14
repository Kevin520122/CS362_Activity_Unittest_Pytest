def count_word(sentence):
    if sentence == "" or sentence == " ":
        return 0
    word_list = sentence.split(" ")
    
    return len(word_list)
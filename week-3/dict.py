def counting_words():
    para = input("enter the paragraph")
    word_dict = {}
    para = para.split(" ")
    for i in para:
        if i in word_dict.keys():
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    return word_dict

print(counting_words())

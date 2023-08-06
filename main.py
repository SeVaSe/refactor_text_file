def del_words():
    with open('textWAR_I.txt', 'r', encoding='utf-8') as file_text_read:
        new_file = [wrd for wrd in file_text_read if 'смех' not in wrd]
        return new_word_file(new_file)

def new_word_file(new_file):
    with open('newWORD.txt', 'w', encoding='utf-8') as file_text_write:
        file_text_write.writelines(new_file)



def main():
    del_words()



if __name__ == '__main__':
    main()


































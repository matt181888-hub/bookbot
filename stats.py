
def word_count(text):
    words = text.split()
    lower_case_words = [item.lower() for item in words]
    return lower_case_words
    

def characters(lower_case_words):
    char_count = {}
    for word in lower_case_words:
            for chars in word:
                if chars not in char_count.keys():
                    char_count[chars] = 1
                else:
                    char_count[chars] += 1
    return char_count

def sort_on(letters):
     return letters['num']

def sorted_character_dict(ind_characters):
     ind_characters_list = [{'letters': k, 'num': v} for k, v in ind_characters.items()]
     ind_characters_list.sort(reverse=True, key=sort_on)
     for pair in ind_characters_list:
        letter = pair['letters']
        num = pair['num']
        if letter.isalpha():
            print(f'{letter}: {num}')
          
     

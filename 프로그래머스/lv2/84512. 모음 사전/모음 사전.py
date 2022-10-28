def solution(word):
    
    word_dict = {}
    def recursive(word, index = 0, s = ''):
        for c in ['A', 'E', 'I', 'O', 'U']:
            index += 1
            word_dict[s+c] = index
            if len(s+c) < 5:
                index = recursive(word, index, s+c)
        return index
    recursive(word, index = 0, s = '')
    return word_dict[word]
class Anagrams():
    def anagrams(self, word, words):
        _word_dictionary = {}
        for letter in word:
            try:
                _word_dictionary[letter] += 1
            except:
                _word_dictionary[letter] = 1

        _anagrams = []
        for ww in words:
            _ww_dictionary = {}
            for letter in ww:
                try:
                    _ww_dictionary[letter] += 1
                except:
                    _ww_dictionary[letter] = 1
            if _ww_dictionary == _word_dictionary:
                _anagrams.append(ww)
        
        print(_anagrams)
        return _anagrams

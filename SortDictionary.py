#   PURPOSE - This program is for sorting dictionaries

class SortDictionary:

# This function sorts a dict alphabetically and/or from least to greatest
    def sortDictByKey(self, dictionary):
    # Letter characters, numeric characters, and the remaining characters are
    # separated into 3 different dicts, each to be sorted individually
        letter_chars = {}
        number_chars = {}
        symbol_chars = {}
        for char in dictionary:
            if str(char).isnumeric():
                number_chars[char] = dictionary[char]
            elif str(char).isalnum():
                letter_chars[char] = dictionary[char]
            else:
                symbol_chars[char] = dictionary[char]
        sorted_dictionary = dict(sorted(letter_chars.items()))
        sorted_dictionary.update(dict(sorted(number_chars.items())))
        sorted_dictionary.update(symbol_chars)
        del dictionary, letter_chars, number_chars, symbol_chars
        return(sorted_dictionary)

# These two function calls serve as alternative ways to call the sortDictByKey function,
# in case a user forgets the original function name
    def sortDict(self, dictionary):
        self.sortDictByKey(dictionary)

    def sortDictionaryByKey(self, dictionary):
        self.sortDictByKey(dictionary)

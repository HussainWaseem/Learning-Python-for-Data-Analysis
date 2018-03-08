def lyrics_to_freq(lyrics):
    ''' lyrics is a list of words.
    It will return a dictioanry having words to frequency mapping'''
    
    my_d = {}
    for word in lyrics:  
        if word in my_d: # if the word(key) is in dictionary
            my_d[word] += 1 # Update its value (frequency) +1
        else:
            my_d[word] = 1 # else, add that word to the dictionary and put its value one.
    return my_d        


def most_common_words(d):
    ''' d is a dictioanry I get from lyrics_to_freq function.
    So d has words to frequency mapping.
    This function will returns the tuple, first element is a list of words
    and 2nd element is the Highest frequency(int). '''

    words = [] # I will store the words with highest frequency in this list.
    values = d.values() # Returns a dictionary view object of all values. values of d are frequencies.
    best = max(values) # Max frequency
    
    for key in d: # keys are words in d.
        if d[key] == best: # If a key has highest frequency
            words.append(key)
        
    return words,best
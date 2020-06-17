import database2
from stopwords import stop_words


def clean_words(words):
    """Takes a string, removes invalid or irrelevant words and returns a list of words"""
    
    cleaned_words = []
    words = str(words)
    for word in words.split():     
        if not word.isalpha():
            continue
        if word.lower() in stop_words:
            continue
        cleaned_words.append(word)
    return cleaned_words
    
    
def frequency(item):
    """counts the frequency of an item in a list"""
    
    freq = {}
    
    for i in item:
        freq[i] = freq.get(i, 0)+1
        
    return freq


def top_n_words(words, n):
    """return the top n words from a dictionary
    parameters:
        words(dictionary) containing word and word-count pairs
        n(int) number of words to return
        """
    
    return {k: v for k, v in sorted(words.items(), key=lambda item: item[1], 
                                    reverse = True)[:n]}


def word_match_count(word_frequencies1, word_frequencies2):
    """Returns the number of matching elements between two lists"""
    
    count = 0
    for word in word_frequencies1:
        if word in word_frequencies2:
            count += 1
    return count


def compare_members(members, n):
    """compare subjects to find those who use the most and least similar words 
    in the speaches when comparing the top n words
    parameters:
        members(str) 'party' or 'speaker'
        n (int) top number of words to compare
    """
    
    similarity = {}
    
    political_names = database2.get_political_names(members)
    
    for num, member1 in enumerate(political_names):
        mem1 = database2.get_speech(member1, members)
        top_n_mem1 = top_n_words(frequency(clean_words(mem1)),n) 
        
        for member2 in political_names[num:]:
            if member1 == member2:
                continue
            print (f'analysing {member1} against {member2}')
            mem2 = database2.get_speech(member2, members)
            top_n_mem2 = top_n_words((frequency((clean_words(mem2)))), n)
            
            name = member1 + ' / ' + member2
            
            similarity[name] = word_match_count(top_n_mem1, top_n_mem2)
            
    return similarity

            
def display_results(member, n):
    """display least and most simialr political members
    parameters:
        members(str) 'party' or 'speaker'
        n (int) top number of words to compare
    """
    
    comparison = compare_members(member, n)
    
    sort = [(k,v) for k,v in sorted(comparison.items(), key = lambda item: item[1])]
    
    if member == 'party':
        plural = 'parties'
    else:
        plural = 'speakers'
    
    most = sort[-1]
    least = sort[0]
    
    print (f'\nThe {plural} with the most top {n} words in common are {most[0]}'
           f' with {most[1]} out of {n} words in common\n\nThe {plural} with the '
           f'least top {n} words in common are {least[0]} with {least[1]} out of {n} words'
           ' in common\n')

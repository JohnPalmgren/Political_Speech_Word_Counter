import database_mod
from stopwords import stop_words


database_name = 'speech.sqlite'
    

class AnalysisTools():
    """Tools to generate top n clean words."""

    def clean_words(self, words):
        """Takes a string, removes invalid or irrelevant words and returns
        list of words.
        """
    
        cleaned_words = []
        words = str(words)
        for word in words.split():     
            if not word.isalpha():
                continue
            if word.lower() in stop_words:
                continue
            cleaned_words.append(word)
        return cleaned_words
    
    def frequency(self, item):
        """Counts the frequency of an item in a list."""
    
        freq = {}
        for i in item:
            freq[i] = freq.get(i, 0) + 1
        
        return freq

    def top_n_words(self, words, n):
        """Return the top n words from a dictionary.
        words(dictionary): containing word and word-count pairs
        n(int): number of words to return
        """
    
        return {k : v for k, v in sorted(words.items(), key=lambda item :
                item[1], reverse=True)[:n]}


class CompareMembers(AnalysisTools):
    """Perform comparison on political members and display the results."""
    
    def __init__(self, member_type, database_name):
        """Parameters: member_type(str): 'party' or 'speaker
        database_name(str): name of database 
        '"""
        
        self.member_type = member_type
        self.database_name = database_name

    def word_match_count(self, word_frequencies1, word_frequencies2):
        """Returns the number of matching elements between two lists.
        word_frequencies1 & word_frequencies2(lists): lists to be compared 
        to find matching elements.
        """
    
        count = 0
        for word in word_frequencies1:
            if word in word_frequencies2:
                count += 1
        return count

    def comparison(self, n):
        """Interacts with the database to compare subjects to find those who 
        use the most and least similar words in the speaches when comparing 
        the top n words.
        n (int) top number of words to compare
        """
    
        similarity = {}
        
        database = database_mod.Database(self.database_name)
    
        political_names = database.get_political_names(self.member_type)
    
        for num, member1 in enumerate(political_names):
            mem1 = database.get_speech(member1, self.member_type)
            top_n_mem1 = self.top_n_words(self.frequency(self.clean_words
                                         (mem1)),n) 
        
            for member2 in political_names[num:]:
                if member1 == member2:
                    continue
                print (f'analysing {member1} against {member2}')
                mem2 = database.get_speech(member2, self.member_type)
                top_n_mem2 = self.top_n_words((self.frequency(self.clean_words
                                             (mem2))), n)
            
                name = member1 + ' / ' + member2
                similarity[name] = self.word_match_count(top_n_mem1, 
                                                         top_n_mem2)
            
        return similarity

            
    def display_results(self, n):
        """Display least and most simialr political members.
        n (int) top number of words to compare
        """
    
        comparison = self.comparison(n)
    
        sort = [(k,v) for k,v in sorted(comparison.items(), key=lambda 
                                        item : item[1])]
    
        if self.member_type == 'party':
            plural = 'parties'
        else:
            plural = 'speakers'
    
        most = sort[-1]
        least = sort[0]
    
        print (f'\nThe {plural} with the most top {n} words in common are' 
               f' {most[0]} with {most[1]} out of {n} words in common\n\nThe'
               f' {plural} with the least top {n} words in common are' 
               f' {least[0]} with {least[1]} out of {n} words in common\n')


class IndividualMember(AnalysisTools):
    """"Lookup and disdplay top n results for any pary or speaker."""
    
    def __init__(self, member_type, database_name):
        self.member_type = member_type
        self.database_name = database_name
    
    def top_n_for_member(self, name, n):
        """"Retreive from database and return the top n results and wordcount 
        for an individual party or speaker.
        name(str) name of the party or speaker
        n(int) top number of words to be compared
            """

        database = database_mod.Database(self.database_name)

        return self.top_n_words(self.frequency(self.clean_words
                               (database.get_speech(name, self.member_type))),
                                n)
    
    def display_results(self, name, n):
        """Display top n results words and wordcount for individual speaker or
        party.
        """
    
        results = self.top_n_for_member(name, n)
    
        print (f'The top {n} resutls for {name} are: {results}')

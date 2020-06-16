import database2.py

class Political_Member():
    
    def __init__(self, name, member): #member is party or speaker   
        self.name = name
        self.member = member 
        
    def return_top_n_words(self, member, n):
        '''Returns the top n words for a party or speaker'''
            
        speeches = database2.get_speech(self.name, self.member)
        
        
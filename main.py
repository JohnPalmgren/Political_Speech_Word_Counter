import analyse

if __name__ == '__main__':
    
    
    database_name = 'speech.sqlite'
    
    # Display comparisons of top n words by speaker or party.
    party_or_speaker = 'party'
    
    num_comparison_words = 20
    
    results = analyse.CompareMembers(party_or_speaker, database_name)
    
    results.display_results(num_comparison_words)
    
    # Look up individual top n results with wordcounts by speaker or party.
    speaker_or_party = 'speaker'

    name = 'David Cameron'
    
    num_comparison_words = 10
    
    results = analyse.IndividualMember(speaker_or_party, database_name) 
    
    results.display_results(name, num_comparison_words)
    
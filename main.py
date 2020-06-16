import analyse2
import individual_member

if __name__ == '__main__':
    
    # Display comparisons of top n words by speaker or party
    party_or_speaker = 'party'
    
    num_comparision_words = 20
    
    analyse2.display_results(party_or_speaker, num_comparision_words)
    
    
    # Look up individual top n results with wordcounts by speaker or party
    
    speaker_or_party = 'speaker'

    name = 'David Cameron'
    
    num_comparision_words = 10
    
    individual_member.display_results(speaker_or_party, name, num_comparision_words)
    
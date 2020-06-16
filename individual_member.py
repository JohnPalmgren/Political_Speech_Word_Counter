import analyse2
import database2


def top_n_for_member(member, name, n):
    """"return the top n results and wordcount for an individual party or speaker"""

    return analyse2.top_n_words(analyse2.frequency(analyse2.clean_words(database2.get_speech(name, member))), n)
    

def display_results(member, name, n):
    """Display top n results words and wordcount for individual speaker or party"""
    
    results = top_n_for_member(member, name, n)
    
    print (f'The top {n} resutls for {name} are: {results}')


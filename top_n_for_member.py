import analyse2
import database2


def top_n_for_member(member, name, n):
    """"return the top n result for an individual party or speaker"""

    return analyse2.top_n_words(analyse2.frequency(analyse2.clean_words(database2.get_speech(name, member))), n)
    

speaker_or_party = 'speaker'

name = 'David Cameron'


print(top_n_for_member(speaker_or_party, name, 10))
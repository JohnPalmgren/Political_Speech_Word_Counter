import individual_member

def test_top_n_for_member():
    results = individual_member.top_n_for_member('party', 'Labour', 3)
    assert results == {'I': 5241, 'people': 2181, 'new': 1540}


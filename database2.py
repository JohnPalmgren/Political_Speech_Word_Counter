import sqlite3

database = 'speech.sqlite'


def context_manager(command):
    """Creates a context manager for opening and closing the database
    parameters:
        command(str): SQL database command
    """
    
    with sqlite3.connect(database) as conn:
        global cur
        cur = conn.cursor()
        return cur.execute(command)


def get_political_names(query):
    """get list of names of all parties or speakers
    parameters:
        query(str): 'party' or 'speaker'
    """
        
    output = []
    context_manager(f'SELECT {query} FROM  Speeches')
    for row in cur:
        if row[0] in output:
            continue
        else:
            output.append(row[0])
    return output


def get_speech(political_member, column):
    """Return a list of speeches which match speaker/party
    Parameters:
        political member (str): The name of the political party or speaker.
        column(str): Select the column in the database. Enter either 'party'
        or 'speaker'.
    """
       
    context_manager(f'SELECT speech FROM Speeches WHERE {column} = "{political_member}"')
    
    return [row for row in cur]
    

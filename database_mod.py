import sqlite3


class Database():
    """Class to interact with the database and retreive speeches"""
    
    def __init__(self, database_name):
        self.database_name = database_name
        
    def context_manager(self, command):
        """Creates a context manager for opening and closing the database
        command(str): SQL database command
        """
    
        with sqlite3.connect(self.database_name) as conn:
            self.cur = conn.cursor()
            return self.cur.execute(command)

    def get_political_names(self, column):
        """Get list of names of all parties or speakers
        column(str): Select the column in the database. Enter either 'party'
         or 'speaker
        """
        
        output = []
        self.context_manager(f'SELECT {column} FROM  Speeches')
        for row in self.cur:
            if row[0] in output:
                continue
            else:
                output.append(row[0])
        return output

    def get_speech(self, political_member, column):
        """Return a list of speeches which match speaker/party
        political member (str): The name of the political party or speaker.
        column(str): Select the column in the database. Enter either 'party'
        or 'speaker'.
        """
       
        self.context_manager(f'SELECT speech FROM Speeches WHERE {column} =' 
                             f'"{political_member}"')
    
        return [row for row in self.cur]        
    





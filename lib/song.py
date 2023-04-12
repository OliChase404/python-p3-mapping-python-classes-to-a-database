from config import CONN, CURSOR





class Song:
    
    
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
        
        
    def save(self):
        CURSOR.execute('''INSERT INTO songs (name, album) VALUES (?, ?)''', (self.name, self.album))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
    
    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            )
            '''
        CURSOR.execute(sql)
    
    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
    
    
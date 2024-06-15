from db import cursor, conn

class Upcoming:
    TABLE_NAME = "upcoming"  
    def __init__(self,image_url, title, release_date):
        self.id = None
        self.image_url = image_url
        self.title = title
        self.release_date = release_date
        
    def save(self):
            sql = f"""
            INSERT INTO {self.TABLE_NAME} (image_url, title, release_date)
            VALUES (?, ?, ?)
            """
            cursor.execute(sql, (self.image_url, self.title, self.release_date))
            conn.commit()
            self.id = cursor.lastrowid
            print(f"Inserted offer with ID: {self.id}")
            
    def to_dict(self):
        return{
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'release_date': self.release_date,
        }
    
    @classmethod
    def get_all(cls):
        sql = f"""
        SELECT * FROM {cls.TABLE_NAME}
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls.row_to_instance(row) for row in rows]
    
    @classmethod
    def row_to_instance(cls, row):
        if row is None:
            return None
        upcoming = cls(image_url=row[1], title=row[2], release_date=row[3])
        upcoming.id = row[0]
        return upcoming
    
    @classmethod
    def create_table(cls):
        sql_drop = f"""
        DROP TABLE IF EXISTS {cls.TABLE_NAME}
        """
        cursor.execute(sql_drop)
        conn.commit
        
        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_url TEXT NOT NULL,
            title TEXT NOT NULL,
            release_date TEXT NOT NULL
            )
            """
        cursor.execute(sql_create)
        conn.commit

Upcoming.create_table()

upcoming1 = Upcoming(
    image_url="https://example.com/upcoming1.jpg",
    title="Elden Ring",
    release_date="2023-02-25"
)
upcoming1.save()

upcoming2 = Upcoming(
    image_url="https://example.com/upcoming2.jpg",
    title="Starfield",
    release_date="2023-11-11"
)
upcoming2.save()

upcoming3 = Upcoming(
    image_url="https://example.com/upcoming3.jpg",
    title="Breath of the Wild 2",
    release_date="2023-12-31"
)
upcoming3.save()

upcoming4 = Upcoming(
    image_url="https://example.com/upcoming4.jpg",
    title="Hogwarts Legacy",
    release_date="2022-12-31"
)
upcoming4.save()

upcoming5 = Upcoming(
    image_url="https://example.com/upcoming5.jpg",
    title="God of War Ragnarok",
    release_date="2023-09-09"
)
upcoming5.save()
upcoming6 = Upcoming(
    image_url="https://example.com/upcoming6.jpg",
    title="Cyberpunk Chronicles",
    release_date="2023-08-15"
)
upcoming6.save()

upcoming7 = Upcoming(
    image_url="https://example.com/upcoming7.jpg",
    title="Beyond Good and Evil 2",
    release_date="2023-06-30"
)
upcoming7.save()

upcoming8 = Upcoming(
    image_url="https://example.com/upcoming8.jpg",
    title="Metroid Prime 4",
    release_date="2024-03-31"
)
upcoming8.save()

upcoming9 = Upcoming(
    image_url="https://example.com/upcoming9.jpg",
    title="Gothic Remake",
    release_date="2023-11-30"
)
upcoming9.save()

upcoming10 = Upcoming(
    image_url="https://example.com/upcoming10.jpg",
    title="Dragon Age 4",
    release_date="2024-02-29"
)
upcoming10.save()
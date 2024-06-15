from db import cursor, conn

class Games:
    TABLE_NAME = "games"
    
    def __init__(self, image_url, title, category, price, rating, release_date):
        self.id = None
        self.image_url = image_url
        self.title = title
        self.category = category
        self.price = price
        self.rating = rating
        self.release_date = release_date

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url, title, category, price, rating, release_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.image_url, self.title, self.category, self.price, self.rating, self.release_date))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted game with ID: {self.id}")
        print(f"{self.title}, {self.category}, {self.price}, {self.rating}, {self.release_date}, {self.image_url}")

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'category': self.category,
            'price': self.price,
            'rating': self.rating,
            'release_date': self.release_date
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
        game = cls(image_url=row[1], title=row[2], category=row[3], price=row[4], rating=row[5], release_date=row[6])
        game.id = row[0]
        return game

    @classmethod
    def create_table(cls):
        sql_drop = f"""
        DROP TABLE IF EXISTS {cls.TABLE_NAME}
        """
        cursor.execute(sql_drop)
        conn.commit()

        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_url TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price TEXT NOT NULL,
            rating TEXT NOT NULL,
            release_date TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()

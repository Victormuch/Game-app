from db import cursor, conn

class Offers:
    TABLE_NAME = "offers"
    
    def __init__(self, image_url, title, category, initial_price, current_price, rating, release_date):
        self.id = None
        self.image_url = image_url
        self.title = title
        self.category = category
        self.initial_price = initial_price
        self.current_price = current_price
        self.rating = rating
        self.release_date = release_date

    def save(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url, title, category, initial_price, current_price, rating, release_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(sql, (self.image_url, self.title, self.category, self.initial_price, self.current_price, self.rating, self.release_date))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted offer with ID: {self.id}")

    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'category': self.category,
            'initial_price': self.initial_price,
            'current_price': self.current_price,
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
        offer = cls(
            image_url=row[1], 
            title=row[2], 
            category=row[3], 
            initial_price=row[4], 
            current_price=row[5], 
            rating=row[6], 
            release_date=row[7]
        )
        offer.id = row[0]
        return offer

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
            initial_price TEXT NOT NULL,
            current_price TEXT NOT NULL,
            rating TEXT NOT NULL,
            release_date TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()

# Initialize the offers table
Offers.create_table()

# Add initial data
offers = [
    {
        "image_url": "https://wallpaperaccess.com/full/789012.jpg",
        "title": "The Witcher 3: Wild Hunt",
        "category": "RPG",
        "initial_price": "Ksh 7,000",
        "current_price": "Ksh 5,000",
        "rating": 5,
        "release_date": "2015-05-19"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/890123.jpg",
        "title": "Monster Hunter: World",
        "category": "Action/RPG",
        "initial_price": "Ksh 6,800",
        "current_price": "Ksh 4,800",
        "rating": 5,
        "release_date": "2018-01-26"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/901234.jpg",
        "title": "The Legend of Zelda: Breath of the Wild",
        "category": "Action/Adventure",
        "initial_price": "Ksh 7,200",
        "current_price": "Ksh 5,200",
        "rating": 5,
        "release_date": "2017-03-03"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/012345.jpg",
        "title": "Super Mario Odyssey",
        "category": "Platformer",
        "initial_price": "Ksh 6,500",
        "current_price": "Ksh 4,500",
        "rating": 5,
        "release_date": "2017-10-27"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/1234567.jpg",
        "title": "Splatoon 2",
        "category": "Shooter",
        "initial_price": "Ksh 5,800",
        "current_price": "Ksh 3,800",
        "rating": 4,
        "release_date": "2017-07-21"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/2345678.jpg",
        "title": "Persona 5",
        "category": "RPG",
        "initial_price": "Ksh 6,700",
        "current_price": "Ksh 4,700",
        "rating": 5,
        "release_date": "2016-09-15"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/3456789.jpg",
        "title": "Animal Crossing: New Horizons",
        "category": "Simulation",
        "initial_price": "Ksh 5,500",
        "current_price": "Ksh 3,500",
        "rating": 4,
        "release_date": "2020-03-20"
    },
    {
        "image_url": "https://wallpaperaccess.com/full/4567890.jpg",
        "title": "Fire Emblem: Three Houses",
        "category": "Strategy/RPG",
        "initial_price": "Ksh 6,300",
        "current_price": "Ksh 4,300",
        "rating": 5,
        "release_date": "2019-07-26"
    }
]

for offer_data in offers:
    offer = Offers(
        image_url=offer_data["image_url"],
        title=offer_data["title"],
        category=offer_data["category"],
        initial_price=offer_data["initial_price"],
        current_price=offer_data["current_price"],
        rating=offer_data["rating"],
        release_date=offer_data["release_date"]
    )
    offer.save()

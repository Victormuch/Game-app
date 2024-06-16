from db import cursor, conn  # Ensure these are correctly imported from your db module


class Offer:
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

    @classmethod
    def get_all(cls):
        sql = f"SELECT * FROM {cls.TABLE_NAME}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        offers = []
        for row in rows:
            offer = Offer(
                image_url=row[1],
                title=row[2],
                category=row[3],
                initial_price=row[4],
                current_price=row[5],
                rating=row[6],
                release_date=row[7]
            )
            offer.id = row[0]
            offers.append(offer)
        return offers


# Create the table if it doesn't exist
Offer.create_table()

offers_data = [
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/620/343/647/the-witcher-the-witcher-3-wild-hunt-geralt-of-rivia-video-games-wallpaper-preview.jpg",
        "title": "The Witcher 3: Wild Hunt",
        "category": "RPG",
        "initial_price": "Ksh 7,000",
        "current_price": "Ksh 5,000",
        "rating": "5",
        "release_date": "2015-05-19"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/880/678/507/video-game-monster-hunter-world-alatreon-monster-hunter-glavenus-monster-hunter-lagiacrus-monster-hunter-hd-wallpaper-preview.jpg",
        "title": "Monster Hunter: World",
        "category": "Action/RPG",
        "initial_price": "Ksh 6,800",
        "current_price": "Ksh 4,800",
        "rating": "5",
        "release_date": "2018-01-26"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/854/846/561/zelda-the-legend-of-zelda-breath-of-the-wild-master-sword-wallpaper-preview.jpg",
        "title": "The Legend of Zelda: Breath of the Wild",
        "category": "Action/Adventure",
        "initial_price": "Ksh 7,200",
        "current_price": "Ksh 5,200",
        "rating": "5",
        "release_date": "2017-03-03"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/803/392/37/8k-2017-4k-nintendo-switch-wallpaper-preview.jpg",
        "title": "Super Mario Odyssey",
        "category": "Platformer",
        "initial_price": "Ksh 6,500",
        "current_price": "Ksh 4,500",
        "rating": "5",
        "release_date": "2017-10-27"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/998/470/346/club-nintendo-nintendo-nintendo-3ds-nintendo-switch-wallpaper-preview.jpg",
        "title": "Splatoon 2",
        "category": "Shooter",
        "initial_price": "Ksh 5,800",
        "current_price": "Ksh 3,800",
        "rating": "4",
        "release_date": "2017-07-21"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/988/411/763/persona-persona-5-akira-kurusu-arsene-persona-5-wallpaper-preview.jpg",
        "title": "Persona 5",
        "category": "RPG",
        "initial_price": "Ksh 6,700",
        "current_price": "Ksh 4,700",
        "rating": "5",
        "release_date": "2016-09-15"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/683/526/425/escenarios-games-kombart-mortal-wallpaper-preview.jpg",
        "title": "Mortal Kombat",
        "category": "Simulation",
        "initial_price": "Ksh 5,500",
        "current_price": "Ksh 3,500",
        "rating": "4",
        "release_date": "2020-03-20"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/633/978/420/video-game-fire-emblem-three-houses-claude-fire-emblem-hd-wallpaper-preview.jpg",
        "title": "Fire Emblem: Three Houses",
        "category": "Strategy/RPG",
        "initial_price": "Ksh 6,300",
        "current_price": "Ksh 4,300",
        "rating": "5",
        "release_date": "2019-07-26"
    },
]

# Insert each offer into the database
for offer_data in offers_data:
    offer = Offer(
        image_url=offer_data["image_url"],
        title=offer_data["title"],
        category=offer_data["category"],
        initial_price=offer_data["initial_price"],
        current_price=offer_data["current_price"],
        rating=offer_data["rating"],
        release_date=offer_data["release_date"]
    )
    offer.save()

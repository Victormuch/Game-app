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
        
    @classmethod
    def get_by_id(cls, game_id):
        sql = f"SELECT * FROM {cls.TABLE_NAME} WHERE id = ?"
        cursor.execute(sql, (game_id,))
        row = cursor.fetchone()
        return cls.row_to_instance(row)

# Call create_table to ensure the table exists
Games.create_table()

game_data = [
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/8/406/344/horizon-forbidden-west-horizon-ii-forbidden-west-aloy-horizon-zero-dawn-4k-robot-hd-wallpaper-preview.jpg",
        "title": "Horizon",
        "category": "Adventure",
        "price": "Ksh 3500",
        "rating": "4",
        "releaseDate": "Release Date: 2022-02-18"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/257/369/277/far-cry-far-cry-5-boomer-far-cry-5-video-game-wallpaper-preview.jpg",
        "title": "FARCRY",
        "category": "action-adventure",
        "price": "Ksh 5900",
        "rating": "5",
        "releaseDate": "Release Date: 2018-03-27"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/261/457/305/god-of-war-kratos-thor-ragnarok-hd-wallpaper-preview.jpg",
        "title": "God of War Ragnarok",
        "category": "Action/Adventure",
        "price": "Ksh 7,500",
        "rating": "5",
        "releaseDate": "Release Date: 2022-11-09"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/202/784/19/spiderman-ps4-spiderman-games-hd-wallpaper-preview.jpg",
        "title": "Marvel's Spider-Man 2",
        "category": "Action/Adventure",
        "price": "Ksh 6,800",
        "rating": "4",
        "releaseDate": "Release Date: 2023-10-20"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/684/655/646/naughty-dog-the-last-of-us-part-ii-playstation-ellie-ashley-johnson-hd-wallpaper-preview.jpg",
        "title": "The Last of Us Part II",
        "category": "Action/Adventure",
        "price": "Ksh 5,500",
        "rating": "4",
        "releaseDate": "Release Date: 2022-01-01"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/74/666/568/hogwarts-legacy-castle-fantasy-art-mist-dark-hd-wallpaper-preview.jpg",
        "title": "Hogwarts Legacy",
        "category": "RPG",
        "price": "Ksh 7,000",
        "rating": "4",
        "releaseDate": "Release Date: 2020-06-19"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/984/871/802/call-of-duty-call-of-duty-modern-warfare-2-video-game-characters-video-games-farah-hd-wallpaper-preview.jpg",
        "title": "Call of Duty: Modern Warfare 2",
        "category": "Shooter",
        "price": "Ksh 6,500",
        "rating": "5",
        "releaseDate": "Release Date: 2022-10-28"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/501/625/175/red-bull-hangar-7-wallpaper-preview.jpg",
        "title": "Gran Turismo 7",
        "category": "Racing",
        "price": "Ksh 6,000",
        "rating": "5",
        "releaseDate": "Release Date:2022-03-04"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/139/265/83/video-game-ghost-of-tsushima-hd-wallpaper-preview.jpg",
        "title": "Ghost of Tsushima",
        "category": "Action",
        "price": "Ksh 5,800",
        "rating": "5",
        "releaseDate": "Release Date: 2020-07-17"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/665/534/394/resident-evil-8-chris-redfield-village-resident-evil-village-4k-hd-wallpaper-preview.jpg",
        "title": "Resident Evil Village",
        "category": "Horror",
        "price": "Ksh 6,000",
        "rating": "5",
        "releaseDate": "Release Date: 2021-05-07 "
    },
    {
        "img": "https://images4.alphacoders.com/114/thumbbig-1147409.webp",
        "title": "Ratchet & Clank: Rift Apart",
        "category": "Action/Platformer",
        "price": "Ksh 7,200",
        "rating": 4.5,
        "releaseDate": "Release Date: 2021-06-11"
    },
    {
        "img": "https://wallpaperaccess.com/full/5871265.jpg",
        "title": "Returnal",
        "category": "Action/Roguelike",
        "price": "Ksh 6,500",
        "rating": 4,
        "releaseDate": "Release Date: 2021-04-30"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/1016/85/224/final-fantasy-vii-remake-final-fantasy-vii-tifa-lockhart-hd-wallpaper-preview.jpg",
        "title": "Final Fantasy VII Remake",
        "category": "RPG",
        "price": "Ksh 5,700",
        "rating": 4.5,
        "releaseDate": "Release Date: 2020-04-10"
    },
    {
        "img": "https://images7.alphacoders.com/110/thumbbig-1102639.webp",
        "title": "Demon's Souls",
        "category": "RPG",
        "price": "Ksh 6,800",
        "rating": 4.5,
        "releaseDate": "Release Date: 2020-11-12"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/478/422/462/cyberpunk-2077-games-ps-games-xbox-games-wallpaper-preview.jpg",
        "title": "Cyberpunk 2077",
        "category": "RPG",
        "price": "Ksh 5,500",
        "rating": 4,
        "releaseDate": "Release Date: 2020-12-10"
    },
    {
        "img": "https://c4.wallpaperflare.com/wallpaper/1023/66/471/assassin-s-creed-valhalla-viking-video-games-video-game-art-digital-art-hd-wallpaper-preview.jpg",
        "title": "Assassin's Creed Valhalla",
        "category": "Action/RPG",
        "price": "Ksh 6,000",
        "rating": 4,
        "releaseDate": "Release Date: 2020-11-10"
    },
]

for card in game_data:
    game = Games(
        image_url=card["img"],
        title=card["title"],
        category=card["category"],
        price=card["price"],
        rating=card["rating"],
        release_date=card["releaseDate"]
    )
    game.save()

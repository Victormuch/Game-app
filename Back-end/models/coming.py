from db import cursor, conn

class Upcoming:
    TABLE_NAME = "upcoming"  

    def __init__(self, image_url, title, release_date):
        self.id = None
        self.image_url = image_url
        self.title = title
        self.release_date = release_date
        
    def save(self):
        if self.id is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        sql = f"""
        INSERT INTO {self.TABLE_NAME} (image_url, title, release_date)
        VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.image_url, self.title, self.release_date))
        conn.commit()
        self.id = cursor.lastrowid
        print(f"Inserted upcoming with ID: {self.id}")
        
    def _update(self):
        sql = f"""
        UPDATE {self.TABLE_NAME}
        SET image_url = ?, title = ?, release_date = ?
        WHERE id = ?
        """
        cursor.execute(sql, (self.image_url, self.title, self.release_date, self.id))
        conn.commit()
        print(f"Updated upcoming with ID: {self.id}")

    def to_dict(self):
        return {
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
        conn.commit()
        
        sql_create = f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_url TEXT NOT NULL,
            title TEXT NOT NULL,
            release_date TEXT NOT NULL
        )
        """
        cursor.execute(sql_create)
        conn.commit()

Upcoming.create_table()

upcoming_games = [
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/489/876/39/elden-ring-from-software-fromsoftware-hd-wallpaper-preview.jpg",
        "title": "Elden Ring",
        "release_date": "2023-02-25"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/85/16/1016/starfield-stars-spacesuit-spaceship-hd-wallpaper-preview.jpg",
        "title": "Starfield",
        "release_date": "2023-11-11"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/230/758/494/zelda-the-legend-of-zelda-the-legend-of-zelda-breath-of-the-wild-link-marcus-fenix-hd-wallpaper-preview.jpg",
        "title": "Breath of the Wild 2",
        "release_date": "2023-12-31"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/997/794/382/miles-morales-spiderman-miles-morales-spider-man-peter-parker-spider-gwen-hd-wallpaper-preview.jpg",
        "title": "SpiderMan Mile Morales",
        "release_date": "2022-12-31"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/224/51/772/anime-monster-hunter-stories-ride-on-castle-lute-monster-hunter-stories-wallpaper-preview.jpg",
        "title": "Monster Hunter Stories",
        "release_date": "2023-09-09"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/629/992/1022/video-game-shadowrun-chronicles-cyberpunk-wallpaper-preview.jpg",
        "title": "Cyberpunk Chronicles",
        "release_date": "2023-08-15"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/636/791/682/e3-2017-6k-beyond-good-and-evil-2-poster-wallpaper-preview.jpg",
        "title": "Beyond Good and Evil 2",
        "release_date": "2023-06-30"
    },
    {
        "image_url": "https://c4.wallpaperflare.com/wallpaper/373/506/467/destiny-2-destiny-video-game-titan-warlock-wallpaper-preview.jpg",
        "title": "Destiny 2",
        "release_date": "2024-03-31"
    }
]

for up in upcoming_games:
    coming= Upcoming(
        image_url=up["image_url"],
        title=up["title"],
        release_date=up["release_date"]
    )
    coming.save()
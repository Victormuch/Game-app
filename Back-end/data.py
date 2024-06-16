from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from games import Games

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    # Create the games table on startup
    Games.create_table()

    # Insert sample data if the table is empty
    if not Games.get_all():
        card_data = [
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
                "price": " Ksh 7,500",
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
                "category": " Racing",
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

        for card in card_data:
            game = Games(
                image_url=card['img'],
                title=card['title'],
                category=card['category'],
                price=card['price'],
                rating=card['rating'],
                release_date=card['releaseDate']
            )
            game.save()

@app.get("/games")
async def get_games():
    games = Games.get_all()
    return {"games": [game.to_dict() for game in games]}


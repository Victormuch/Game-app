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
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            },
            {
                "img": "https://c7.alamy.com/comp/2HNYEFY/smartphone-with-frame-from-horizon-forbidden-west-on-screen-surrounded-by-gamepads-2HNYEFY.jpg",
                "title": "Fortnite",
                "category": "Action",
                "price": "Ksh 4000",
                "rating": "4.5",
                "releaseDate": "Release Date: 2022-01-01"
            }
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

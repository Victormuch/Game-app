from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from games import Games
from models.offers import Offers
from models.upcoming import Upcoming
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/games")
async def get_games():
    games = Games.get_all()
    return {"games": [game.to_dict() for game in games]}

@app.get("/offer")
async def get_upcoming():
    upcoming = Upcoming.get_all()
    return {"offer": [up.to_dict() for up in upcoming]}

@app.get("/upcoming")
async def get_upcoming_games():
    upcoming_games = Upcoming.get_all()
    return {"upcoming_games": [game.to_dict() for game in upcoming_games]}
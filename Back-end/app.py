from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.offers import Offers
from models.upcoming import Upcoming
from games import Games

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
async def get_offers():
    offers = Offers.get_all()
    return {"offers": [offer.to_dict() for offer in offers]}

@app.get("/upcoming")
async def get_upcoming_games():
    upcoming_games = Upcoming.get_all()
    return {"upcoming_games": [game.to_dict() for game in upcoming_games]}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.game1 import Games
from models.coming import Upcoming
from models.cut import Offer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/games1")
async def get_cards():
    cards= Games.get_all()
    return{"games1":[card.to_dict() for card in cards]}

@app.get("/coming1")
async def get_upcoming():
    cards= Upcoming.get_all()
    return{"coming1":[card.to_dict() for card in cards]}

@app.get("/offer")
async def get_offer():
    offers = Offer.get_all()
    return {"offer": [offer.__dict__ for offer in offers]}

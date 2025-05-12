from fastapi import APIRouter
import random

router = APIRouter()

@router.get("/slot")
async def gioca_slot():
    risultato = random.choice(["Hai vinto!", "Ritenta!", "Jackpot!", "Hai perso!"])
    return {"gioco": "slot", "risultato": risultato}

@router.get("/roulette")
async def gioca_roulette():
    numeri = list(range(0, 37))
    vincente = random.choice(numeri)
    colore = "rosso" if vincente % 2 == 0 else "nero"
    return {
        "gioco": "roulette",
        "numero_estratto": vincente,
        "colore": colore
    }

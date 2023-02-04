from fastapi import FastAPI, Query, HTTPException
import random
import re

app = FastAPI()

def validate_word(word: str):
    if not re.match("^[a-zA-Z0-9]+$", word):
        raise HTTPException(status_code=400, detail="Input can only contain alphabets or numbers.")
    return word

payload = []

@app.get("/jumble/{word}")
async def jumble_word_route(word: str = Query(..., alias="word")):
    try:
        word = validate_word(word)
    except HTTPException as ex:
        return ex.detail

    jumbled_word = jumble_word(word)

    global payload
    payload.append({"word": word, "jumbled_word": jumbled_word})
    payload = payload[-10:]  # keep only the last 10 payload

    return {"jumbled_word": jumbled_word}

def jumble_word(word: str):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)

@app.get("/audit")
async def get_payload():
    return {"last_10_payloads" : payload}
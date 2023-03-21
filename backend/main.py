from fastapi import FastAPI

from backend.model.braille import BrailleBody, BrailleResponse
from backend.service.traslate import translate_braille_to_korean

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/translation/braille")
async def say_hello(braille_instance: BrailleBody) -> BrailleResponse:
    raw_braille = braille_instance.braille
    kor = translate_braille_to_korean(raw_braille)[0]

    braille_unicodes = [ord(bra_unicode) for bra_unicode in raw_braille]
    response = BrailleResponse(str=kor, braille=braille_unicodes)

    return response



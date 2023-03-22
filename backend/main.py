from fastapi import FastAPI

from backend.model.braille import BrailleBody, BrailleResponse
from backend.service.traslate import translate_braille_to_korean, translate_korean_to_braille, convert_str_to_unicodes

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/translation/braille")
async def translate_2_korean(braille_instance: BrailleBody) -> BrailleResponse:
    braille = braille_instance.braille
    kor = translate_braille_to_korean(braille)[0]

    braille_unicodes = convert_str_to_unicodes(braille)
    response = BrailleResponse(str=kor, braille=braille_unicodes)

    return response

@app.get("/translation")
async def translate_2_braille(kor: str | None = None):
    if kor:
        response = []
        for letter in kor:
            brailles = translate_korean_to_braille(letter)
            unicodes = convert_str_to_unicodes(brailles)
            response.append(BrailleResponse(str=letter, braille=unicodes))
        return response
    return {"is_success": False, "data": "번역되지 않았습니다."}


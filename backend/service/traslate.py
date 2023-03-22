from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from pythonnet import load
load("coreclr")

import clr

clr.AddReference("./backend/service/Jumjaro")

from Jumjaro import Jumjaro
def translate_braille_to_korean(braille_pattern: str):
    # get tokenizer, config and pretrained weights
    tokenizer = AutoTokenizer.from_pretrained("snoop2head/KoBrailleT5-small-v1")
    model = AutoModelForSeq2SeqLM.from_pretrained("snoop2head/KoBrailleT5-small-v1")

    # translate braille to korean
    # braille_pattern = "⠍⠗⠠⠪⠋⠕⠀⠘⠪⠐⠗⠒⠊⠕⠐⠀⠘⠮⠐⠍⠨⠟⠀⠚⠣⠕⠚⠕⠂</s>"
    # braille_pattern = "⠣⠒⠉⠻</s>"
    braille_pattern = f"{braille_pattern}</s>"
    # translate braille to korean
    input_ids = tokenizer(braille_pattern, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    korean_output = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    return korean_output


def translate_korean_to_braille(korean: str):
    return Jumjaro().ToJumja(korean)

def convert_str_to_unicodes(value: str) -> list[int]:
    return [ord(char) for char in value]
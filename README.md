# Solution Challenge: Braille to Korean and Korean to Braille Translator
This is a Python FastAPI server for translating Braille to Korean and Korean to Braille. This repository contains the backend solution for the translation of text in both directions using Braille and Korean.

## Project Architecure

![solution_challenge_architecture drawio](https://user-images.githubusercontent.com/86528640/228577666-24656f26-25be-4d2f-b08b-0cd296b4fa0a.png)

## Getting Started
To run this application, follow the below steps:

1. Clone this repository to your local machine.
2. Make sure you have Python 3.10 or later installed on your system.
3. pip install -r requirements.txt.
4. Start the server by running python main.py.
5. Navigate to http://localhost:8000/docs in your web browser to access the API documentation and try out the endpoints.

## API Endpoints
The following endpoints are available for translation:

### POST /translate/braille-to-korean
This endpoint expects a JSON payload with a text key containing the Braille text to translate. The response will be a JSON object with a result key containing the translated Korean text.

POST /translate/korean-to-braille
This endpoint expects a JSON payload with a text key containing the Korean text to translate. The response will be a JSON object with a result key containing the translated Braille text.

### Examples
Here are some example requests and responses for the API endpoints:

POST /translate/braille-to-korean
Request:


```
POST /translate/braille-to-korean
{
  "text": "⠠⠃⠗⠁⠊⠇⠇⠑"
}
Response:

json
Copy code
200 OK
{
  "result": "안녕하세요"
}
```

### POST /translate/korean-to-braille
Request:

```
POST /translate/korean-to-braille
{
  "text": "안녕하세요"
}
Response:

json
Copy code
200 OK
{
  "result": "⠠⠁⠝⠞⠄⠞⠕⠗⠥"
}
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



import requests
import json
from ollama import chat

# Wordle API URL
URL = "https://wordle-api.vercel.app/api/wordle"

# ollama API URL for LLM
LLAMA3_URL = "http://localhost:11434/api/chat"

INSTRUCTIONS = open("wordle/instructions.txt", "r").read()
WORD = ["*", "*", "*", "*", "*"]
WRONG_WORDS = []
WRONG_LETTERS = []
CONFIRMED_LETTERS = []
UNUSED_LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def ask_llm(history):

    response = chat(
        model='deepseek-r1',
        messages=[
            {
                'role': 'user',
                'content': history
            }
        ],
        stream=True
    )

    full_content = ""
    print("🤖 DeepSeek-R1 sta ragionando...")
    print("=" * 60)
    
    for chunk in response:
        if chunk.message.content:
            print(chunk.message.content, end='', flush=True)
            full_content += chunk.message.content
    
    print("\n" + "=" * 60)
    return full_content



def printGuess(character_info):
    results = ""
    index = 0
    for char in character_info:
        if char["char"].upper() in UNUSED_LETTERS:
            UNUSED_LETTERS.remove(char["char"].upper())
        if not char["scoring"]["in_word"]:
            results += "⬜️"
            if char["char"] not in WRONG_LETTERS:
                WRONG_LETTERS.append(char["char"].upper())
        else:
            if char["scoring"]["correct_idx"]:
                results += "🟩"
                if char["char"].upper() not in CONFIRMED_LETTERS:
                    CONFIRMED_LETTERS.append(char["char"].upper())
                WORD[index] = char["char"].upper()
            else:
                results += "🟨"
                if char["char"].upper() not in CONFIRMED_LETTERS:
                    CONFIRMED_LETTERS.append(char["char"].upper())
        index += 1

    return results


def guess_wordle(guess):
    llmGuess = {"guess": guess}
    response = requests.post(URL, llmGuess)
    json_response = json.loads(response.content.decode('utf-8'))

    if json_response["was_correct"]:
        print(f"🎉 Congratulations! You guessed the word: {guess}")
        return True, "🟩🟩🟩🟩🟩"
    else:
        results = printGuess(json_response["character_info"])
        if guess not in WRONG_WORDS:
            WRONG_WORDS.append(guess)
        return False, results


if __name__ == "__main__":
    guessed = False
    history = ""

    while not guessed:
        prompt =    INSTRUCTIONS + history + f"\nDON'T USE THESE WRONG LETTERS: {WRONG_LETTERS}" \
                    + f"\nDON'T USE THESE WRONG WORDS: {WRONG_WORDS}" + f"\nUSE THESE UNUSED LETTERS: {UNUSED_LETTERS}" \
                    + f"\n USE THESE CONFIRMED LETTERS: {CONFIRMED_LETTERS}" + f"\nWORD: {WORD}"
        guess = ask_llm(prompt)[-5:]
        print(f"Guessing: {guess}")
        guessed, result = guess_wordle(guess)
        history += f"\n{guess} -> {result}"
        print(f"{guess} -> {result}")

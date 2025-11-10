import requests
import json

URL = "https://cs.stanford.edu/~knuth/sgb-words.txt"

def fetch_word_list(url):
    resp = requests.get(url)
    resp.raise_for_status()
    text = resp.text
    words = [w.strip() for w in text.split() if w.strip()]
    return words

def save_as_json(words, out_path):
    # Contoh format: array kata
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

def main():
    words = fetch_word_list(URL)
    save_as_json(words, "wordle_words.json")
    print(f"Saved {len(words)} words to wordle_words.json")

if __name__ == "__main__":
    main()

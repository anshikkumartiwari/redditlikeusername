from flask import Flask, jsonify
import requests
import random

app = Flask(__name__)

common_words = [
    'thing', 'profession', 'food', 'animal', 'place', 'bird', 
    'country', 'car', 'gun', 'cat', 'race', 'movie', 'cartoon', 
    'character', 'color'
]

def fetch_words(word_type, related_word):
    url = f'https://api.datamuse.com/words?max=10&rel_{word_type}={related_word}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            words = [entry['word'] for entry in response.json()]
            print(f"Fetched {len(words)} {word_type}s related to {related_word}")
            return words
        else:
            print(f"Failed to fetch words. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching words: {e}")
        return []

def fetch_random_words():
    related_word = random.choice(common_words)
    adjectives = fetch_words('jjb', related_word)
    nouns = fetch_words('jja', related_word)
    return adjectives, nouns

def generate_four_letter_word():
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    word = random.choice(consonants) + random.choice(vowels) + random.choice(consonants) + random.choice(vowels)
    return word

def generate_random_number():
    return random.randint(100, 999)

@app.route('/generate-username', methods=['GET'])
def generate_username():
    adjectives, nouns = fetch_random_words()
    
    if adjectives and nouns:
        random_adjective = random.choice(adjectives)
        random_noun = random.choice(nouns)
        
        four_letter_word = generate_four_letter_word()
        random_number = generate_random_number()
        
        username = f"{four_letter_word}{random_adjective.capitalize()}{random_noun.capitalize()}{random_number}"
        
        return jsonify({
            "username": username,
        })
    else:
        return jsonify({"error": "Failed to fetch words from Datamuse API"})

if __name__ == '__main__':
    app.run(debug=True)

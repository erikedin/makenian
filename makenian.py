#  Copyright 2022 Erik Edin
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import os
from dotenv import load_dotenv
import random
import time
import requests
from fastDamerauLevenshtein import damerauLevenshtein

def generate_puzzle(word):
    s = random.sample(word, k=len(word))
    return ''.join(s)

def similarity(word, puzzle):
    return damerauLevenshtein(word, puzzle, similarity=True)

def nine_letter_words(all_words):
    return [word for word in all_words if len(word) == 9]

def read_nine_letter_words(dictionary_file):
    with open(dictionary_file, "r") as fh:
        dictionary = fh.readlines()
    all_words = [x.strip() for x in dictionary]
    return nine_letter_words(all_words)

def select_word(words):
    return random.choice(words)

def find_puzzle(words):
    word = select_word(words)
    puzzles = [generate_puzzle(word) for i in range(100)]
    good_enough = [puzzle for puzzle in puzzles if similarity(word, puzzle) < 0.5]
    return random.choice(good_enough).upper()

def generate_and_upload(webhook_url, dictionary):
    puzzle = find_puzzle(dictionary)
    payload = {"text": f"!sättnian {puzzle}"}
    print(f"Uploading nian to {webhook_url} with payload {payload}")
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    load_dotenv()
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    dictionary_file = os.getenv("DICTIONARY_FILE")

    # Seed random generator to get different puzzles on each invocation.
    random.seed(time.time())

    dictionary = read_nine_letter_words(dictionary_file)

    generate_and_upload(webhook_url, dictionary)
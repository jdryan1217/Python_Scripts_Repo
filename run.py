#!/usr/bin/env python3
"""
Process customer review text files and upload them to a web service.

Each .txt file is expected to contain:
1. Title
2. Customer name
3. Date
4. Feedback text

The script:
- Reads all .txt files in a directory
- Converts each file into a Python dictionary
- Sends the dictionary as JSON via POST to a REST endpoint
"""

import os
import requests

# Directory containing the review text files
FEEDBACK_DIR = "/data/feedback/"

# Replace this with your actual endpoint when running in Qwiklabs
WEB_ENDPOINT = "http://<corpweb-external-IP>/feedback/"

def process_file(filepath):
    """Read a feedback file and return a dictionary with its contents."""
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    # Expecting exactly 4 lines per file
    return {
        "title": lines[0],
        "name": lines[1],
        "date": lines[2],
        "feedback": " ".join(lines[3:])  # join remaining lines into one paragraph
    }

def upload_review(review_dict):
    """Send a POST request with the review data."""
    response = requests.post(WEB_ENDPOINT, json=review_dict)
    print(f"POST {response.status_code}: {response.text}")
    return response.status_code == 201

def main():
    """Main script logic."""
    for filename in os.listdir(FEEDBACK_DIR):
        if not filename.endswith(".txt"):
            continue

        filepath = os.path.join(FEEDBACK_DIR, filename)
        review = process_file(filepath)
        print(f"Uploading: {filename}")
        upload_review(review)

if __name__ == "__main__":
    main()

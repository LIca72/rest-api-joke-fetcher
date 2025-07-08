import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("\n🌿 Joke of the day for you:")
        print(data["setup"])
        print(data["punchline"])

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_joke()

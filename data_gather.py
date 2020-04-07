import requests
import json
import os

try:
    os.mkdir("data")
except:
    pass


def api_to_json(url):
    response = requests.get(url)
    response_json = json.loads(response.text)
    try:
        filename = "data/" + url.split("/")[-1]
        try:
            with open(filename, "w") as fs:
                json.dump(response_json, fs)
        except Exception as e:
            print("Error in saving file:", e)
    except Exception as e:
        print("Error in filename parsing:", e)


def gather():
    urls = [
        "https://api.covid19india.org/data.json",
    ]
    for each in urls:
        api_to_json(each)


if __name__ == "__main__":
    gather()

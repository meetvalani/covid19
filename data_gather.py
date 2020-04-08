import requests
import json
import os


def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except:
        pass


create_dir("data")
create_dir("visualizations")


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
        "https://api.covid19india.org/v2/state_district_wise.json",
        # "https://api.covid19india.org/travel_history.json",
        # "https://api.covid19india.org/raw_data.json",
        # "https://api.covid19india.org/states_daily.json"
        #############################################################
        # "https://api.covid19india.org/state_district_wise.json",
    ]
    for each in urls:
        api_to_json(each)


if __name__ == "__main__":
    gather()

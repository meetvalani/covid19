import json


def read_from_file(filename):
    data = None
    try:
        with open(filename, "r") as fs:
            data = json.load(fs)
    except Exception as e:
        print("Error in reading data from file:", e)
    return data


def cases_time_series_formatter(data):
    months = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12}

    def month_no(month_name):
        return months[month_name.lower()]

    for each in data["cases_time_series"]:
        each["dailyconfirmed"] = int(each["dailyconfirmed"])
        each["dailydeceased"] = int(each["dailydeceased"])
        each["dailyrecovered"] = int(each["dailyrecovered"])
        each["totalconfirmed"] = int(each["totalconfirmed"])
        each["totaldeceased"] = int(each["totaldeceased"])
        each["totalrecovered"] = int(each["totalrecovered"])
        day_month = each["date"].split()
        each["date"] = {
            "full": each["date"],
            "day": int(day_month[0]),
            "month": day_month[1],
            "month_no": month_no(day_month[1])
        }
    return data


def statewise_formatter(data):
    for each in data["statewise"]:
        each["active"] = int(each["active"])
        each["confirmed"] = int(each["confirmed"])
        each["deaths"] = int(each["deaths"])
        each["deltaconfirmed"] = each["deltaconfirmed"]
        each["deltadeaths"] = int(each["deltadeaths"])
        each["deltarecovered"] = int(each["deltarecovered"])
        each["lastupdatedtime"] = each["lastupdatedtime"]
        each["recovered"] = int(each["recovered"])

    return data


def data_json_formatter():
    data = read_from_file("data/data.json")
    data = cases_time_series_formatter(data)
    data = statewise_formatter(data)
    return data


def state_district_wise_json_formatter():
    data = read_from_file("data/state_district_wise.json")
    return data


if __name__ == "__main__":
    state_district_wise_json_formatter()

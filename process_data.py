import json


def read_from_file(filename):
    data = None
    try:
        with open(filename, "r") as fs:
            data = json.load(fs)
    except Exception as e:
        print("Error in reading data from file:", e)
    return data


months = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'jul': 7,
    'aug': 8,
    'sep': 9,
    'oct': 10,
    'nov': 11,
    'dec': 12}


def month_no(month_name):
    return months[month_name.lower()[:3]]


def cases_time_series_formatter(data):

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


def state_from_statecode():
    data = read_from_file("data/state_code.json")
    return data


def state_daily_json_formatter():
    data = read_from_file("data/states_daily.json")
    data2 = read_from_file("data/state_code.json")
    for daily in data["states_daily"]:
        for state in daily.keys():
            try:
                daily[state] = int(daily[state])
            except:
                if daily[state] == "":
                    daily[state] = 0
    data.update({"state_code": data2})
    return data


if __name__ == "__main__":
    data = state_daily_json_formatter()
    print(data, type(data))

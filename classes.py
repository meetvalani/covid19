class DailyDataClass:
    def __init__(self, raw_data):
        self.days = list()
        self.dailyconfirmed = list()
        self.dailydeceased = list()
        self.dailyrecovered = list()
        self.totalconfirmed = list()
        self.totaldeceased = list()
        self.totalrecovered = list()
        for each in raw_data["cases_time_series"]:
            self.days.append(each["date"]["full"])
            self.dailyconfirmed.append(each["dailyconfirmed"])
            self.dailydeceased.append(each["dailydeceased"])
            self.dailyrecovered.append(each["dailyrecovered"])
            self.totalconfirmed.append(each["totalconfirmed"])
            self.totaldeceased.append(each["totaldeceased"])
            self.totalrecovered.append(each["totalrecovered"])


class StatewiseDataClass:
    def __init__(self, raw_data):
        self.active = list()
        self.confirmed = list()
        self.deaths = list()
        self.deltaconfirmed = list()
        self.deltadeaths = list()
        self.deltarecovered = list()
        self.lastupdatedtime = list()
        self.state = list()
        self.statecode = list()

        for each in raw_data["statewise"]:
            self.state.append(each["state"])
            self.active.append(each["active"])
            self.confirmed.append(each["confirmed"])
            self.deaths.append(each["deaths"])
            self.deltaconfirmed.append(each["deltaconfirmed"])
            self.deltadeaths.append(each["deltadeaths"])
            self.deltarecovered.append(each["deltarecovered"])
            self.lastupdatedtime.append(each["lastupdatedtime"])
            self.statecode.append(each["statecode"])
        self.confirmed, self.active, self.deaths, self.deltaconfirmed, self.deltadeaths, self.deltarecovered, self.lastupdatedtime, self.state, self.statecode = zip(
            *sorted(zip(self.confirmed, self.active, self.deaths, self.deltaconfirmed, self.deltadeaths, self.deltarecovered, self.lastupdatedtime, self.state, self.statecode), reverse=True))


class StateDistrictwiseDataClass:
    def __init__(self, raw_data):
        self.main_list = list()
        for each in raw_data:
            total = 0
            tmp = list()
            for every in each["districtData"]:
                total += every["confirmed"]
                tmp.append([every["district"], every["confirmed"]])
            tmp.sort(key=lambda x: x[1])
            tmp.reverse()
            name = list()
            value = list()
            for every in tmp:
                name.append(every[0])
                value.append(every[1])
            self.main_list.append({
                "state": each["state"],
                "district": name,
                "confirmed": value,
                "total": total
            })
        self.main_list.sort(key=lambda x: x["total"])
        self.main_list.reverse()


class StatesDailyDataClass:
    def __init__(self, raw_data):
        self.dates = list()
        self.states_data = dict()
        self.state_code = raw_data["state_code"]
        for state_name in raw_data["state_code"].keys():
            self.states_data.update({state_name: {
                "total": 0,
                "data": {
                    "Confirmed": list(),
                    "Recovered": list(),
                    "Deceased": list()
                }
            }})
        for daily in raw_data["states_daily"]:
            flag = daily["status"]
            date = daily["date"]
            if date not in self.dates:
                self.dates.append(date)
            for state in daily.keys():
                if state != "status" and state != "date":
                    self.states_data[state]["total"] += daily[state]
                    self.states_data[state]["data"][flag].append(daily[state])
        tmp = []
        for each in self.states_data.keys():
            tmp.append([self.states_data[each]['total'], each])
        tmp.sort(reverse=True)
        buffer = dict()
        for each in tmp:
            buffer.update({each[1]: self.states_data[each[1]]})
        self.states_data = buffer

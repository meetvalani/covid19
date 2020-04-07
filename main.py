import data_gather
import process_data
from matplotlib import pyplot as plt
import numpy as np


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


def plot_multiline_graph(data, last_days=20):
    plt.title("COVID-19 Information in India")
    dot_size = 4

    plt.plot(data.days[-last_days:], data.dailyconfirmed[-last_days:], label="Daily Confirmed",
             color="orange", marker='o', markerfacecolor='orange', markersize=dot_size)

    plt.plot(data.days[-last_days:], data.dailyrecovered[-last_days:], color="green",
             label="Recovered", marker='o', markerfacecolor='green', markersize=dot_size)

    plt.plot(data.days[-last_days:], data.dailydeceased[-last_days:], color="red",
             label="Deceased", marker='o', markerfacecolor='red', markersize=dot_size)

    plt.plot(data.days[-last_days:], data.totalconfirmed[-last_days:], color="blue",
             label="Total", marker='o', markerfacecolor='blue', markersize=dot_size)

    plt.xticks(rotation='vertical')
    plt.legend(loc='best')
    plt.show()


def plot_pie_chart(data, no_of_states=10):
    total = sum(data.confirmed[1:no_of_states+1])
    plt.title(
        "Top 10 COVID-19 affected states in India \n Total: {}".format(data.confirmed[0]))

    def autopct_format(values):
        def my_format(pct):
            val = int(round(pct*total/100.0))
            return '{v}'.format(v=val)
        return my_format
    plt.pie(data.confirmed[1:no_of_states+1],
            labels=data.state[1:no_of_states+1], autopct=autopct_format(data.confirmed[1:no_of_states+1]))
    plt.show()


if __name__ == "__main__":
    data_gather.gather()
    raw_data = process_data.data_json_formatter()

    data = DailyDataClass(raw_data)
    data2 = StatewiseDataClass(raw_data)

    plot_multiline_graph(data, last_days=20)
    plot_pie_chart(data2, no_of_states=10)

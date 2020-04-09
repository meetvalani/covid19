import data_gather
import process_data
import math
from matplotlib import pyplot as plt
import numpy as np
from classes import *


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
    plt.subplots_adjust(bottom=0.2)
    plt.savefig('visualizations/daily.png', dpi=600)
    plt.show()


def autopct_format(total, values):
    def my_format(pct):
        val = int(round(pct*total/100.0))
        return '{v}'.format(v=val)
    return my_format


def plot_pie_chart(data, no_of_states=10):
    total = sum(data.confirmed[1:no_of_states+1])
    plt.title(
        "Top 10 COVID-19 affected states in India \n Total: {}".format(data.confirmed[0]))

    plt.pie(data.confirmed[1:no_of_states+1],
            labels=data.state[1:no_of_states+1], autopct=autopct_format(total, data.confirmed[1:no_of_states+1]))
    plt.savefig('visualizations/statewise.png', dpi=600)
    plt.show()


def plot_pie_chart_state_district(data, no_of_states=3, no_of_district=10, column=3):
    data = data.main_list
    max_states = min(no_of_states, len(data), 9)
    tmp = math.ceil(max_states/column)
    val = tmp*100 + column*10
    fig = plt.figure(figsize=(4*max_states, 3))

    for i in range(max_states):
        ax = fig.add_subplot(val+i+1)
        ax.set_title(data[i]["state"])
        mx = min(no_of_district, len(data[i]["district"]))
        ax.pie(data[i]["confirmed"][:mx], labels=data[i]["district"][:mx],
               autopct=autopct_format(data[i]["total"], data[i]["confirmed"][:mx]))

    plt.suptitle('Top-'+str(no_of_states)+' State-District wise Information')
    plt.savefig('visualizations/state_district.png', dpi=600)
    plt.show()


def plot_multiline_graph_state_daily(data, last_days=5, no_of_states=5, show_total=False):
    if show_total:
        no_of_states += 1
    dot_size = 4
    no_of_states = min(no_of_states, 38)

    def sub_plotter(category, position):
        plt.subplot(position, title=category)
        for i, state in enumerate(data.states_data.keys()):
            if not show_total and i == 0:
                continue
            if i >= no_of_states:
                break
            plt.plot(data.dates[-last_days:], data.states_data[state]["data"][category][-last_days:], label=data.state_code[state],
                     marker='o', markersize=dot_size)

        plt.xticks(rotation='vertical')
        plt.legend(loc='best')
        plt.subplots_adjust(bottom=0.2)

    plt.title("COVID-19 Daily Statewise information in India")
    sub_plotter("Confirmed", 131)
    sub_plotter("Recovered", 132)
    sub_plotter("Deceased", 133)
    plt.savefig('visualizations/state_daily.png', dpi=600)
    plt.show()


if __name__ == "__main__":
    data_gather.gather()
    raw_data1 = process_data.data_json_formatter()

    data1 = DailyDataClass(raw_data1)
    plot_multiline_graph(data1, last_days=20)

    data2 = StatewiseDataClass(raw_data1)
    plot_pie_chart(data2, no_of_states=10)

    raw_data2 = process_data.state_district_wise_json_formatter()
    data3 = StateDistrictwiseDataClass(raw_data2)
    plot_pie_chart_state_district(
        data3, no_of_states=2, no_of_district=5, column=2)

    raw_data3 = process_data.state_daily_json_formatter()
    data4 = StatesDailyDataClass(raw_data3)
    plot_multiline_graph_state_daily(data4)

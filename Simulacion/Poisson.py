import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

# Getting inter-event time in a poisson process

def inter_event_times(lam, n, plot=False):
    """
    Generates times between consecutive events in a simulated Poisson process.

    :param lam: Average incidence rate.
    :param n: Number of events.
    :param plot: if True it also plots the inter-event times.
    :return A dataframe with the event number and inter event time
    """
    event_num = range(n)
    ie_times = []
    for _ in event_num:
        t = np.random.uniform(0, 1)
        ie_time = -np.log(1 - t) / lam
        ie_times.append(ie_time)

    if plot:
        fig = plt.figure()
        fig.suptitle('Times between consecutive events\nin a simulated Poisson process')
        plt.bar(event_num, ie_times, label='Inter-event time')
        plt.legend(loc='best')
        plt.xlabel('Index of event')
        plt.ylabel('Time')
        plt.show()

    data_dict = {'event number': event_num, 'inter event time': ie_times}
    return pd.DataFrame(data_dict)

# Getting absolute event time in a poisson process (Simulating the process)

def abs_event_times(lam, n, plot=False, ie_times=None):
    """
    Generates absolute times of consecutive events in a simulated Poisson process.

    :param lam: Average incidence rate.
    :param n: Number of events.
    :param plot: If True it also plots the process.
    :param ie_times: The inter-event times (if left empty it calculates them on its own)
    :return: A dataframe with the event number and Absolute event time
    """
    if ie_times is None:
        data = inter_event_times(lam, n)
        ie_times = data['inter-event time'].tolist()
    event_num = range(n)
    times = []
    time = 0
    for i in event_num:
        time += ie_times[i]
        times.append(time)

    if plot:
        fig = plt.figure()
        fig.suptitle('Absolute times of consecutive events\nin a simulated Poisson process')
        plt.plot(event_num, times, '.', label='Absolute time of event')
        plt.legend(loc='best')
        plt.xlabel('Index of event')
        plt.ylabel('Time')
        plt.show()

    data_dict = {'event number': event_num, 'event time': times}
    return pd.DataFrame(data_dict)

# Getting the number of events in consecutive intervals.

def events_in_consecutive(lam, n, plot=False, event_times=None, ie_times=None):
    """
    Generates the number of events occurring in consecutive intervals in a
    simulated Poisson process and calculates the mean number of events per unit time.

    :param lam: The average incidence rate
    :param n: The number of events
    :param plot: If True also returns a histogram of the occurrences.
    :param event_times: The absolute event times. If left empty it does its own.
    :param ie_times: The inter-event times. If left empty it does its own.
    :return: A dataframe with the occurrences and the mean.
    """
    if event_times is None:
        data = abs_event_times(lam, n, ie_times=ie_times)
        event_times = data['event time'].tolist()
    interval_nums = []
    num_events_in_interval = []
    interval_index = 1
    num_events = 0
    for i in range(len(event_times)):
        time = event_times[i]
        if time <= interval_index:
            num_events += 1
        else:
            interval_nums.append(interval_index)
            num_events_in_interval.append(num_events)
            interval_index += 1
            num_events = 1

    if plot:
        fig = plt.figure()
        fig.suptitle('Number of events occurring in consecutive intervals\nin a simulated Poisson process')
        plt.bar(interval_nums, num_events_in_interval)
        plt.xlabel('Index of interval')
        plt.ylabel('Number of events')
        plt.show()

    data_dict = {'Interval Number': interval_nums, '# of events': num_events_in_interval}
    mean = np.mean(num_events_in_interval)
    return pd.DataFrame(data_dict), mean


def main():
    lam = 1/40
    n = 1000
    inter_times = inter_event_times(lam, n, plot=True)
    ie_times = inter_times['inter event time'].tolist()
    abs_times = abs_event_times(lam, n, plot=True, ie_times=ie_times)
    event_times = abs_times['event time'].tolist()
    consecutive, mean = events_in_consecutive(lam, n, plot=True, event_times=event_times,
                                              ie_times=ie_times)
    display(inter_times)
    display(abs_times)
    display(consecutive)
    print(f'The mean number of events per unit time is {mean}')


if __name__ == '__main__':
    main()

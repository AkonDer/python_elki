import datetime


def find_near_time(list_time):
    time_now = datetime.datetime.now()

    time_now_second = time_now.hour * 3600 + time_now.minute * 60 + time_now.second
    for time in list_time:
        time_second = time.hour * 3600 + time.minute * 60
        if time_second - time_now_second >= 0:
            return time
    return list_time[0]


def convert_to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second
    pass


def run():
    time_now = datetime.datetime.now()

    list_times_open_bar = []
    list_times_close_bar = []
    with open("static/resources/open_bar.txt", "r") as f:
        for item in f.readlines():
            list_times_open_bar.append(datetime.datetime(year=time_now.year, month=time_now.month,
                                                         day=time_now.day, hour=int(item.split(':')[0]),
                                                         minute=int(item.split(':')[1])))

    with open("static/resources/close_bar.txt", "r") as f:
        for item in f.readlines():
            list_times_close_bar.append(datetime.datetime(year=time_now.year, month=time_now.month,
                                                          day=time_now.day, hour=int(item.split(':')[0]),
                                                          minute=int(item.split(':')[1])))

    delta_close_bar = convert_to_second(find_near_time(list_times_close_bar)) - convert_to_second(time_now)
    delta_open_bar = convert_to_second(find_near_time(list_times_open_bar)) - convert_to_second(time_now)

    if delta_close_bar > delta_open_bar:
        return f"Закрыто еще {str(datetime.timedelta(seconds=delta_open_bar))}", "static/resources/close.png"
    elif delta_close_bar < delta_open_bar:
        return f"Открыто еще {str(datetime.timedelta(seconds=delta_close_bar))}", "static/resources/open.png"

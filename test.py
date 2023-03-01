import datetime

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


def find_near_time(list_time):
    time_nw = datetime.datetime.now()
    time_now_second = time_nw.hour * 3600 + time_nw.minute * 60
    for time in list_time:
        time_second = time.hour * 3600 + time.minute * 60
        if time_second - time_now_second >= 0:
            return time
    return list_time[0]


delta_close_bar = find_near_time(list_times_close_bar) - time_now
delta_open_bar = find_near_time(list_times_open_bar) - time_now

if delta_close_bar > delta_open_bar:
    print(f"Закрыто еще {delta_open_bar.seconds // 60}:{delta_open_bar.seconds % 60}")
elif delta_close_bar < delta_open_bar:
    print(f"Открыто еще {delta_close_bar.seconds // 60}:{delta_close_bar.seconds % 60}")


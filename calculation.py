import datetime

list_times_open_bar_source = ["0:06", "0:43", "1:49", "4:34", "5:10", "5:35", "6:08", "6:26", "6:47", "7:08", "7:30",
                              "7:51", "8:12", "8:34", "8:51", "9:10", "9:32", "10:13", "10:35", "10:52", "12:43",
                              "13:38", "13:59", "14:34", "14:44", "15:19", "15:33", "16:12", "16:59", "17:22", "17:58",
                              "18:16", "18:33", "18:51", "19:12", "19:34", "19:51", "20:04", "20:23", "20:45", "21:01",
                              "21:19", "21:43", "22:02", "22:37", "22:54", "23:13"]
list_times_close_bar_source = ["0:00", "0:37", "1:43", "4:28", "5:04", "5:29", "6:02", "6:16", "6:36", "6:57", "7:19",
                               "7:40", "8:01", "8:23", "8:45", "9:04", "9:22", "10:02", "10:24", "10:46", "12:37",
                               "13:32", "13:53", "14:28", "14:38", "15:13", "15:27", "16:01", "16:42", "17:11", "17:52",
                               "18:10", "18:27", "18:45", "19:00", "19:21", "19:45", "19:58", "20:12", "20:34", "20:55",
                               "21:13", "21:32", "21:56", "22:31", "22:48", "23:07"]

list_times_open_bar_source_weekend = ["4:36", "5:10", "5:35", "6:11", "6:26", "6:47", "7:08", "7:30", "7:51", "8:12",
                                      "8:34", "8:51", "9:10", "9:32", "10:13", "10:35", "10:52", "11:05", "11:37",
                                      "12:13", "12:43", "13:19", "13:39", "13:59", "14:34", "14:44", "15:19", "15:33",
                                      "16:12", "16:47", "16:59", "17:22", "17:58", "18:17", "18:33", "18:51", "19:12",
                                      "19:34", "19:51", "20:11", "20:23", "20:45", "21:01", "21:19", "21:43", "22:02",
                                      "22:38", "22:54", "23:13", "0:06", "0:43", "1:49"]
list_times_close_bar_source_weekend = ["4:30", "5:04", "5:29", "6:05", "6:20", "6:36", "6:57", "7:19", "7:40", "8:01",
                                       "8:23", "8:45", "9:04", "9:22", "10:02", "10:24", "10:46", "10:59", "11:31",
                                       "12:07", "12:37", "13:13", "13:33", "13:53", "14:28", "14:38", "15:13", "15:27",
                                       "16:01", "16:41", "16:53", "17:11", "17:52", "18:11", "18:27", "18:45", "19:01",
                                       "19:28", "19:45", "20:05", "20:17", "20:34", "20:55", "21:13", "21:32", "21:56",
                                       "22:32", "22:48", "23:07", "0:00", "0:37", "1:43"]

# Список праздничных дней
list_holidays = ["01:05", "08:05", "09:05", "12:06", "06:11"]


# Функция, проверяющая, является ли сегодняшний день выходным или праздником
def is_weekend():
    # Получаем текущую дату в формате дд:мм
    today = datetime.datetime.now().strftime("%d:%m")
    # Проверяем, является ли сегодняшняя дата праздником
    is_holiday = today in list_holidays

    # Получаем текущий день недели как число (0 для понедельника, 1 для вторника и т.д.)
    today = datetime.datetime.today().weekday()
    # Возвращаем True, если текущий день - суббота (5) или воскресенье (6) или праздник, иначе - False.
    return today == 5 or today == 6 or is_holiday


def find_near_time(list_time):
    time_now = datetime.datetime.now()

    time_now_second = time_now.hour * 3600 + time_now.minute * 60 + time_now.second
    for time in list_time:
        time_second = time.hour * 3600 + time.minute * 60
        if time_second - time_now_second >= 0:
            return time
    return list_time[0]


# Функция для конвертации времени в секунды
def convert_to_second(time):
    return time.hour * 3600 + time.minute * 60 + time.second


# Основная функция для выполнения задачи
def run():
    # Получаем текущее время
    time_now = datetime.datetime.now()

    # Выбираем список времени открытия и закрытия бара в зависимости от того, является ли сегодня выходным
    list_times_open_bar_work = list_times_open_bar_source_weekend if is_weekend() else list_times_open_bar_source
    list_times_close_bar_work = list_times_close_bar_source_weekend if is_weekend() else list_times_close_bar_source

    # Преобразуем строки с временем открытия бара в объекты datetime
    list_times_open_bar = [datetime.datetime(year=time_now.year, month=time_now.month, day=time_now.day,
                                             hour=int(item.split(':')[0]), minute=int(item.split(':')[1]))
                           for item in list_times_open_bar_work]

    # Преобразуем строки с временем закрытия бара в объекты datetime
    list_times_close_bar = [datetime.datetime(year=time_now.year, month=time_now.month, day=time_now.day,
                                              hour=int(item.split(':')[0]), minute=int(item.split(':')[1]))
                            for item in list_times_close_bar_work]

    # Вычисляем разницу между текущим временем и ближайшим временем закрытия бара
    delta_close_bar = convert_to_second(find_near_time(list_times_close_bar)) - convert_to_second(time_now)
    # Вычисляем разницу между текущим временем и ближайшим временем открытия бара
    delta_open_bar = convert_to_second(find_near_time(list_times_open_bar)) - convert_to_second(time_now)

    # Если время до закрытия бара больше, чем время до открытия бара, бар закрыт
    if delta_close_bar > delta_open_bar:
        return f"Закрыто ещё {str(datetime.timedelta(seconds=delta_open_bar))}", "static/resources/close.png"
    # Если время до закрытия бара меньше, чем время до открытия бара, бар открыт
    elif delta_close_bar < delta_open_bar:
        return f"Открыто ещё {str(datetime.timedelta(seconds=delta_close_bar))}", "static/resources/open.png"

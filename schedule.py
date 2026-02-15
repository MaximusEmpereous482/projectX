import requests
import sqlite3
from datetime import datetime, timedelta


def get_schedule(group_id, day_offset=None):
    # day_offset: 0 - сегодня, 1 - завтра, None - неделя
    #now = datetime.now()
    #day_now = datetime.weekday(now)  # Понедельник 0, суббота 6
    #print(now, day_now)
    # if day_offset is not None:
    #     target_date = (now + timedelta(days=day_offset)).strftime("%Y.%m.%d")
    #     start, finish = target_date, target_date
    # else:
    #     start = now.strftime("%Y.%m.%d")
    #     finish = (now + timedelta(days=6)).strftime("%Y.%m.%d")
    #
    # url = f"https://ruz.guz.ru/api/schedule/group/{group_id}"
    # params = {"start": start, "finish": finish, "lng": 1}
    #
    # try:
    #     res = requests.get(url, params=params)
    #     data = res.json()
    #     return data
    #
    # except:
    pass


def data_for_schedule():
    now = datetime.now()
    today = datetime.today()
    week_day_now = datetime.weekday(now)  # Понедельник 0, суббота 6
    if week_day_now > 4:
        start = now + timedelta(days=(7 - week_day_now))
        start_schedule = (now + timedelta(days=(7 - week_day_now))).strftime("%Y.%m.%d")
        end = start + timedelta(days=13)
        end_schedule = end.strftime("%Y.%m.%d")
        return start_schedule, end_schedule
    else:
        start = today - timedelta(days=week_day_now)
        start_schedule = (today - timedelta(days=week_day_now)).strftime("%Y.%m.%d")
        end = start + timedelta(days=13)
        end_schedule = end.strftime("%Y.%m.%d")
        return start_schedule, end_schedule


print(data_for_schedule())


# Запуск
#print(get_schedule('199'))

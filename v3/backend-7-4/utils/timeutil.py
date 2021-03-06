import datetime


def get_day_left_in_second():
    """
    返回一天剩余时间(单位:s)
    :return:
    """

    now = datetime.datetime.now()
    tomorrow = now + datetime.timedelta(dats=1)
    left = (datetime.datetime(tomorrow.year,tomorrow.month,tomorrow.day,0,0,0)-now)

    return int(left.total_seconds())


if __name__ == '__main__':
    print(get_day_left_in_second())
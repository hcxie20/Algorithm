# 题目：已知30天日志数据集<ClientId, PageUrl, Clicked, Timestamp>, 计算每条日志对应的ClientId在过去n(e.g. 24)小时Click和没有Click的Count值

# <ClientId, PageUrl, Clicked, Timestamp, Clicks_Count_in_last24hours, NoClicks_Count_in_last24hours>

class Parser(object):
    def __init__(self, id):
        self._init_time = None
        self._data = [[0] * 2] * 48
        # an 48 x 2 array contains countings of click and unclick log record
        self._click_sum = 0
        self._unclick_sum = 0
        # 2 int value, num of counts
        '''
        0: 50, 10
        1: 10, 0
        2: 0, 0
        ...
        ...
        47: 0, 0
        '''
        # _click_sum: sum of first column, num of clicks in less than 24 hours
        # _unclick_sum: sum of second column, num of unclicks ...

        self.last_interval = None

    def add_record(self, ClientId, PageUrl, Clicked, Timestamp):
        if not self._init_time:
            self._init_time = Timestamp

        interval_num = ((Timestamp - self._init_time) // 1800) % len(self._data)

        if self.last_interval and self.last_interval != interval_num:
            self._click_sum -= self._data[interval_num][0]
            self._unclick_sum -= self._data[interval_num][1]

            self._click_sum += self._data[self.last_interval][0]
            self._unclick_sum += self._data[self.last_interval][1]

            # reset record:
            self._data[interval_num] = [0, 0]

        if Clicked:
            # count_click ++
            # self._click_sum ++
        else:
            # count_unclick ++
            # self._unclick_sum ++

        return [Id, Url, Clicked, Time, self._click_sum, self._unclick_sum]





















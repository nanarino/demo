from functools import reduce


def is_leap_year(year_item):
    return (year_item % 4 == 0
            and year_item % 100 != 0) or year_item % 400 == 0


def reshape(li, num):
    def set_num(a, v):
        a[-1].append(v[1]) if v[0] % num else a.append([v[1]])
        return a

    return list(reduce(set_num, enumerate(li), []))


class Month():
    def __init__(self, year_item, month_item):
        self.year_item = year_item
        self.month_item = month_item
        self.last_day_item = self.get_last_day_item(self.year_item,
                                                    self.month_item)

    @staticmethod
    def get_last_day_item(year_item, month_item):
        if month_item != 2:
            return [0, 31, None, 31, 30, 31, 30, 31, 31, 30, 31, 30,
                    31][month_item]
        if is_leap_year(year_item):
            return 29
        return 28

    @property
    def week_item_of_first_day_item(self):
        day_count = 0
        for year_item in range(1900, self.year_item):
            day_count += 365
            if is_leap_year(year_item):
                day_count += 1
        for month_item in range(0, self.month_item):
            day_count += self.get_last_day_item(self.year_item, month_item)
        return day_count % 7 + 1

    @property
    def calendar_array(self):
        SP = ' '
        header = ['Su', 'Mo', 'Tu', 'We', 'Tr', 'Fr', 'Sa']
        top = list(
            map(lambda x: SP * 2, range(self.week_item_of_first_day_item)))
        month_list = list(
            map(lambda x: str(x) if x > 9 else (SP + str(x)),
                range(1, self.last_day_item + 1)))
        bot = list(
            map(
                lambda x: SP * 2,
                range(6 * 7 - self.last_day_item -
                      self.week_item_of_first_day_item)))
        return reshape(header + top + month_list + bot, 7)


def reshape_month(day_count, week_item):
    SP = ' '
    header = ['Su', 'Mo', 'Tu', 'We', 'Tr', 'Fr', 'Sa']
    top = list(map(lambda x: SP * 2, range(week_item)))
    month_list = list(
        map(lambda x: str(x) if x > 9 else (SP + str(x)),
            range(1, day_count + 1)))
    bot = list(map(lambda x: SP * 2, range(6 * 7 - day_count - week_item)))
    return reshape(header + top + month_list + bot, 7)


def append_month(col_list, col):
    def append_day(row_list, row):
        for i in col:
            row_list.extend(i[row])
            row_list.append('\t')
        row_list.append('\n')
        return row_list

    col_list.append(reduce(append_day, range(7), []))
    return col_list


year = int(input("年份数（公元），如2020\n"))
col = int(input("一行显示的月份数，如3 \n"))
month_list = (Month(year, month + 1).calendar_array for month in range(12))
for row_list in reduce(append_month, reshape(month_list, col), []):
    print(' '.join(row_list).replace(' \n ', '\n'))

input("任意键退出")
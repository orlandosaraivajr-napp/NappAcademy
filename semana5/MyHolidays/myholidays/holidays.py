from datetime import datetime, date

class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        for item in args:
            data = self.parser(item)
            if data:
                self.check_value(data)

    def parser(self, value):
            if type(value) == date:
                return value
            try:
                dt = datetime.strptime(value, '%d/%m/%Y')
                return datetime.date(dt)
            except:
                pass
    
    def check_value(self, value):
        if value not in set(self.datas):
            self.datas.append(value)
        else:
            pass

    def add_holiday(self, *args):
        for item in args:
            data = self.parser(item)
            if data:
                self.check_value(data)
    
    def check_holiday(self, *args):
        for item in args:
            data = self.parser(item)
            if(data in set(self.datas)):
                return True
            return False
    
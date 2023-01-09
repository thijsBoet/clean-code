from datetime import datetime

class DateUtil:
    @staticmethod
    def get_formatted_today():
        date_today = datetime.now()
        formatted_date = date_today.strftime("%d-%m-%Y")
        return formatted_date

print(DateUtil.get_formatted_today())
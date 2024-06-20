from datetime import datetime

datetime_url_format = '%Y_%m_%d__%H_%M_%S'


class DatetimeConverter:
    regex = '\d{4}_\d{2}_\d{2}__\d{2}_\d{2}_\d{2}'
    format = datetime_url_format

    def to_python(self, value: str):
        return datetime.strptime(value, self.format)

    def to_url(self, value: datetime):
        return value.strftime(self.format)

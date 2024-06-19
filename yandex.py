from yadisk import YaDisk
from yadisk.exceptions import YaDiskError
from datetime import datetime


class YandexFunctions:
    def __init__(self, token):
        self.token = token
        self.yadisk = YaDisk(token=self.token)

    async def check_token(self):
        try:
            return self.yadisk.check_token()
        except YaDiskError:
            return False

    async def last_date(self, name):
        try:
            items = self.yadisk.listdir(f"disk:/{name}")
        except YaDiskError as e:
            print(f"YaDisk error: {e}")
            return None

        valid_items = [item for item in items if item.modified is not None]

        if not valid_items:
            return None

        last_modified = max(valid_items, key=lambda item: item.modified if item.modified is not None else datetime.min, default=None)
        return last_modified.isoformat() if last_modified else None

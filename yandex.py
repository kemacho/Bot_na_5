from yadisk import YaDisk
from yadisk.exceptions import YaDiskError

class YandexFunctions:
    def __init__(self, token):
        # Инициализация объекта YaDisk с токеном
        self.yadisk = YaDisk(token=token)

    async def check_token(self):
        """
        Проверяет валидность токена для доступа к Яндекс.Диску.
        Возвращает True, если токен валиден, иначе False.
        """
        try:
            return self.yadisk.check_token()
        except YaDiskError:
            # В случае ошибки при проверке токена возвращаем False
            return False

    async def last_date(self, name):
        """
        Возвращает дату последнего изменения файла в указанной папке на Яндекс.Диске.
        Если папка не найдена или произошла ошибка, возвращает None.
        """
        try:
            # Проверка существования папки
            self.yadisk.get_meta(f"disk:/{name}")
            # Получение списка элементов в папке
            items = self.yadisk.listdir(f"disk:/{name}")
        except YaDiskError as e:
            # В случае ошибки при доступе к папке выводим сообщение об ошибке и возвращаем None
            print(e)
            return None

        # Проверяем, есть ли элементы в папке
        if not items:
            return None

        # Находим максимальную дату модификации среди всех элементов в папке, игнорируя None значения
        last_modified = max((item.modified for item in items if item.modified), default=None)

        # Если дата модификации найдена, возвращаем её в формате ISO, иначе возвращаем None
        return last_modified.isoformat() if last_modified else None

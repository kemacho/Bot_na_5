# переменные окружения
# python-dotenv нужен для настройки переменных окружения

# Для передачи токена создайте файл .env со следующим содержимым
# TOKEN=ВАШ_ТОКЕН

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
YANDEX_CLIENT_ID = os.getenv("YANDEX_CLIENT_ID")
YANDEX_CLIENT_SECRET = os.getenv("YANDEX_CLIENT_SECRET")
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./database.db")

#0364c56b69b0432ab95a9ca82a57c842
#y0_AgAAAAAzLYbYAAvtPwAAAAEHEc_eAABVCyUiU-xPO6apb-XFHrZ3Kf4fIg
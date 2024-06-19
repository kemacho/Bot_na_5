# переменные окружения
# python-dotenv нужен для настройки переменных окружения

# Для передачи токена создайте файл .env со следующим содержимым
# TOKEN=ВАШ_ТОКЕН

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
TOKEN_URL = os.getenv("TOKEN_URL")
# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./database.db")

#0364c56b69b0432ab95a9ca82a57c842
#y0_AgAAAAAzLYbYAAvtPwAAAAEHEc_eAABVCyUiU-xPO6apb-XFHrZ3Kf4fIg
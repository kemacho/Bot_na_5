Функция в хэндлерах:

def start(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать! Выберите роль: преподаватель или слушатель.")

def status(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Ваш текущий статус: ...")
  # Проверка наличия токена API Яндекс Диска и предложение зарегистрироваться, если его нет

def register(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Для регистрации в API Яндекс Диска выполните следующие шаги: ...")

def token(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Проверка токена API Яндекс Диска...")

def add(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Введите путь к папке на Яндекс Диске для добавления в отслеживаемые...")

def delete(update, context):
context.bot.send_message(chat_id=update.effective_chat.id, text="Выберите папку для удаления из отслеживаемых...")


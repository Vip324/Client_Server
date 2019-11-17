# logging - стандартный модуль для организации логирования
import logging

# Можно выполнить более расширенную настройку логирования.
# Создаем объект-логгер с именем app.main:
logger_client = logging.getLogger('app.client')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
fh = logging.FileHandler("app.client.log", encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger_client.addHandler(fh)
logger_client.setLevel(logging.DEBUG)

if __name__ == '__main__':

    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger_client.addHandler(console)
    logger_client.info('Тестовый запуск логирования')

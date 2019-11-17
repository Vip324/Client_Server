# logging - стандартный модуль для организации логирования
import logging
import logging.handlers
# Можно выполнить более расширенную настройку логирования.
# Создаем объект-логгер с именем app.main:

logger_server = logging.getLogger('app.server')

# Создаем объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s ")

# Создаем файловый обработчик логирования (можно задать кодировку):
# fh = logging.FileHandler("app.server.log", encoding='utf-8')
fh = logging.handlers.TimedRotatingFileHandler("app.server.log", when='midnight', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

# Добавляем в логгер новый обработчик событий и устанавливаем уровень логирования
logger_server.addHandler(fh)
logger_server.setLevel(logging.DEBUG)

if __name__ == '__main__':

    # Создаем потоковый обработчик логирования (по умолчанию sys.stderr):
    # console = logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    # console.setFormatter(formatter)
    # logger.addHandler(console)
    logger_server.info('Тестовый запуск логирования')

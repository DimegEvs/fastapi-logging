import logging
import os

# Основной логгер для промежуточного ПО
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Обработчик для записи логов в файл
file = logging.FileHandler('src/logger/middleware_logger.log')
file.setLevel(logging.DEBUG)

# Формат логов
format = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file.setFormatter(format)

# Добавление обработчика к логгеру
logger.addHandler(file)


# Класс для создания и управления логгерами пользователей
class UserLogger:
    def __init__(self, user_id):
        self.logger = logging.getLogger(__name__ + '.' + str(user_id))
        self.logger.setLevel(logging.INFO)

        # Создаем отдельный файл для каждого пользователя
        log_file = f'src/logger-users/{str(user_id)}_logger.log'
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

# DO NOT CHANGE ALL OF THESE CONSTANTS

SUPER_ADMIN_LOGIN = "super_admin_login"
SUPER_ADMIN_PASSWORD = "super_admin_password"

ADMINS = [
    ['admin1_login', 'admin1_password'],
    ['admin2_login', 'admin2_password'],
    ['admin3_login', 'admin3_password']
]

PATH_TO_DATABASE = "bot/database/"
ERROR_LOG_PATH = "bot/"

DATABASE_NAME = "database.db"
ERROR_LOG_NAME = "error_log.txt"

SUPER_ADMIN_STATUS = "SUPER_ADMIN"
ADMIN_STATUS = "ADMIN"
STUDENT_STATUS = "STUDENT"

UNAUTHORIZED_TELEGRAM_ID = -1

MAX_LOGIN_SIZE = 25  # less than 30
MAX_HOMEWORK_NAME_SIZE = 25  # less than 30

GRADES_IN_LINE = 7  # less or equal 8
HOMEWORKS_NUMBER_IN_LINE = 1  # less or equal 8
TASKS_NUMBER_IN_LINE = 6  # less or equal 8
TASKS_ON_ONE_PAGE = 5  # less or equal 6
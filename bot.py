#импортируем всё необходимое
import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import mysql.connector
#Создаём подключение к базе данных
mydb = mysql.connector.connect(host="localhost",user="navin", password="1234", database='schedule')
mycursor = mydb.cursor()

# Берём все кафедры из базы данных и создаём из них массив
mycursor.execute("SELECT DISTINCT kafter FROM infoSchedule")
result = mycursor.fetchall()

kafters = []

for i in result:
    kafters.append(i[0])
    

#Берём по кафедрам все группы и создаём словарь с ключом Кафедра и значением массив групп
groups = {}
buf = []
for i in kafters:
    mycursor.execute(f"SELECT DISTINCT group_kafter FROM infoSchedule where kafter = '{i}'")
    result = mycursor.fetchall()
    for j in result:
        buf.append(j[0])
    groups[i] = buf
    buf = []
    



# Состояния разговора внутри бота
KAFTERS, GROUPS, COURSES = range(3)

# Настройка журналирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

#ответ бота на сообщение /start
def start(update: Update, context):
    """Отправляет приветственное сообщение и предлагает выбрать кафедру."""
    #Создаём массив кнопок и передаём его в сообщение
    reply_keyboard = [[kafter] for kafter in kafters]
    update.message.reply_text(
        'Привет! Я бот для выдачи расписания. Выбери кафедру:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    #Возвращаем состояние разговора
    return KAFTERS

#Функция выбора кафедры
def select_kafter(update: Update, context):
    """Сохраняет выбранную кафедру и предлагает выбрать группу."""
    #Записываем в context.user_data ту кафедру что выбрал человек
    context.user_data['kafter'] = update.message.text
    reply_keyboard = [[group] for group in groups[context.user_data['kafter']]]
    #После генерации кнопок групп добавляем в конец '/cancel' для того чтобы можно было начать выбор сначала
    reply_keyboard[0].append('/cancel')
    update.message.reply_text(
        'Теперь выбери группу:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    #Возвращаем состояние разговора
    return GROUPS

#Функция выбора группы
def select_group(update: Update, context):
    """Сохраняет выбранную группу и предлагает выбрать курс."""
    #Записываем в context.user_data ту группу что выбрал человек
    context.user_data['groups'] = update.message.text
    #Создаём массив кнопок и передаём его в сообщение
    reply_keyboard = [['1', '2', '3', '4', '5', '6', '/cancel']]
    update.message.reply_text(
        'Выбери курс:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
        #Возвращаем состояние разговора
    return COURSES

#функция выбора курса и вывода расписания
def select_course(update: Update, context):
    """Выводит расписание выбранной группы и завершает разговор."""
    #Записываем в context.user_data тот курс что выбрал человек
    context.user_data['course'] = update.message.text
    #Делаем запрос на получение расписания к базе данных 
    mycursor.execute(f"SELECT schedule FROM infoschedule WHERE kafter = '{context.user_data['kafter']}' and group_kafter = '{context.user_data['groups']}' and course = {context.user_data['course']}")
    расписание_группы = mycursor.fetchone()
    #Если было что то возращено то значит такое было найдено и выводим расписание
    if расписание_группы != None:
        update.message.reply_text(f"Расписание для {context.user_data['groups']}, {context.user_data['course']} курс:\n{расписание_группы[0]}", reply_markup=ReplyKeyboardMarkup([['/start']], one_time_keyboard=True))
    else:
        #Иначе выводим что расписание для такой группы и такого курса ещё не было добавлено
        update.message.reply_text(f"Расписание для {context.user_data['groups']}, {context.user_data['course']} курс: ещё не было добавлено", reply_markup=ReplyKeyboardMarkup([['/start']], one_time_keyboard=True))
    reply_keyboard = [[kafter] for kafter in kafters]
    update.message.reply_text(
        'Если хочешь узнать ещё расписание выбери новую кафедру:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    return KAFTERS

#Ответ бота на сообщение /cancel
def cancel(update: Update, context):
    """Отменяет разговор и завершает его без выбора расписания."""
    reply_keyboard = [[kafter] for kafter in kafters]
    update.message.reply_text(
        'Вы отменили выбор, выберите заного кафедру:',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    )
    #Переходит в начальное состояние
    return KAFTERS


#главная функция
def main():
    #Соединение с ботом по токену
    #НАПИШИ ТОКЕН БОТА СОВОЙ СЮДА
    updater = Updater("")

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Создание обработчиков команд
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            KAFTERS: [MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Отмена$')), select_kafter)],
            GROUPS: [MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Отмена$')), select_group)],
            COURSES: [MessageHandler(Filters.text & ~(Filters.command | Filters.regex('^Отмена$')), select_course)]
        },

        fallbacks=[CommandHandler('cancel', cancel)]
    )

    # Регистрация обработчика разговоров в диспетчере
    dp.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()

    # Остановка бота при получении сигнала прерывания (Ctrl+C)
    updater.idle()
#Запускаем главную функцию
if __name__ == '__main__':
    main()

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback

categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Kurslar", callback_data="courses"),
            InlineKeyboardButton(text =  "Kitoblar", callback_data="books")
        ],
        [
            InlineKeyboardButton(text = "Mohirdev sahifasiga o'tish", url="https://mohirdev.uz")
        ],
        [
            InlineKeyboardButton(text = 'qidirish', switch_inline_query_current_chat=" ")
        ],
        [
            InlineKeyboardButton(text = 'Ulashish', switch_inline_query="Zo'r bot ekan")
        ]
    ]
)

coursesMenu = InlineKeyboardMarkup(row_width=1)
python  = InlineKeyboardButton(text = "Python Dasturlash asoslari", callback_data= course_callback.new(item_name = "python"))
coursesMenu.insert(python)


django = InlineKeyboardButton(text = "Django dasturlash asoslari", callback_data= course_callback.new(item_name = "django"))
coursesMenu.insert(django)


ortga = InlineKeyboardButton(text = "Ortga", callback_data= course_callback.new(item_name = 'ortga'))
coursesMenu.insert(ortga)


books = {
    "Python. Dasturlash tili": "python_book",
    "Java. Dasturlash tilie": "java_book",
    "Android. Dasturlashi tili": "android_book"
}

bookMenu = InlineKeyboardMarkup(row_width=1)

for key, value in books.items():
    bookMenu.insert(InlineKeyboardButton(text = key, callback_data=book_callback.new(item_name= value)))
    
bookMenu.insert(ortga)
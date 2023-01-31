from aiogram import types
from aiogram.types import Message, CallbackQuery
from loader import dp
import logging
from keyboards.inline.callback_data import book_callback

from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, bookMenu


@dp.message_handler(text = 'Mahsulotlar')
async def products(message: types.Message):
    await message.answer("quyidagilardan birini tanlang", reply_markup=categoryMenu)
    
    
    
    
@dp.callback_query_handler(text = "courses")
async def buy_courses(call: CallbackQuery):
    await call.message.answer("kurs tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)
    
    
    
@dp.callback_query_handler(text = "books")
async def buy_books(call: CallbackQuery):
    await call.message.answer("Kitobni tanlang", reply_markup= bookMenu)
    await call.message.delete()
    await call.answer(cache_time=60)
    
    
@dp.callback_query_handler(book_callback.filter(item_name = "python_book"))
async def buying_python_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=50, show_alert=True)
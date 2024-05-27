from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from database import insert_table, check_table, delete_task, delete_all


router = Router()


class Add(StatesGroup):
    task = State()

class Delete(StatesGroup):
    task = State()

#/start
@router.message(CommandStart())
async def cmd_start(message: Message):
    markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Добавить задачу')],
        [KeyboardButton(text='Список задач')], [KeyboardButton(text='Удалить задачу')]
    ], resize_keyboard=True)
    await message.reply('Это task bot,\nДобавить задачу: /add \nПросмотреть список: /tsk \nУдалить задачу: /clear \nОчистить список: /clearall', reply_markup=markup)

#Добавить задачу
@router.message(F.text=="Добавить задачу")
@router.message(Command('add'))
async def cmd_add1(message:Message, state: FSMContext):
    await state.set_state(Add.task)
    await message.answer("Введите задачу:")


@router.message(Add.task)
async def cmd_add2(message:Message, state: FSMContext):
    await state.update_data(task = message.text)
    data = await state.get_data()
    insert_table(data['task'])
    await message.answer('Вы добавили задачу: %s' % data['task'])
    await state.clear()

#Список задач
@router.message(F.text=="Список задач")
@router.message(Command('tsk'))
async def cmd_check(message:Message):
    check = check_table()
    await message.answer('Ваши задачи: \n\n🔴%s' % '\n🔴'.join(check))

#Удалить задачу
@router.message(F.text=="Удалить задачу")
@router.message(Command('clear'))
async def cmd_delte1(message:Message, state: FSMContext):
    await state.set_state(Delete.task)
    await message.answer('Введите название удаляемой задачи(с учётом регистра)')


@router.message(Delete.task)
async def cmd_delete2(message:Message, state: FSMContext):
    await state.update_data(task = message.text)
    data = await state.get_data()
    delete_task(data['task'])
    await message.answer('Вы удалили задачу: %s' % data['task'])
    await state.clear()

#Удалить весь список
@router.message(Command('clearall'))
async def cmd_check(message:Message):
    check = delete_all()
    await message.answer('Список очищен')


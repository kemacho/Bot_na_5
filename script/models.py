class functions:
    def _add(message: types.Message, state: FSMContext):
    async with SessionLocal() as session:
        user = await session.execute(User.select().where(User.tg_user_id == message.from_user.id))
        user = user.scalar_one_or_none()
        if not user:
            await message.answer("Вы не зарегистрированы. Воспользуйтесь командой /start для регистрации.")
            return
        if not user.teacher_id:
            await message.answer("Вы не являетесь преподавателем и не можете добавлять папки.")
            return
        # Добавьте логику добавления папки в отслеживаемые папки
        await message.answer("Папка успешно добавлена в отслеживаемые.")

def register_add_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_add, Command("add"))
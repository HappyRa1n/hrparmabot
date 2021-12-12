from aiogram import types


# ------------------------------StartButtons-----------------------------------
btn_where_is_the_office = types.InlineKeyboardButton(text="Где находится офис?", callback_data="btn_where")
bth_about_company = types.InlineKeyboardButton(text="Расскажи о компании", callback_data="btn_about")
btn_available_vacancies = types.InlineKeyboardButton(text="Расскажи о доступных вакансиях", callback_data="btn_vacancies")
#btn_interview = types.InlineKeyboardButton(text="Хочу записаться на собеседование", callback_data="btn_4")
start_keyboard = types.InlineKeyboardMarkup(row_width=1).add(
    btn_where_is_the_office,
    bth_about_company,
    btn_available_vacancies,
    #btn_interview
)


# ------------------------ButtonsForChoosingProfession--------------------------

bth_database_administrator = types.InlineKeyboardButton(text="Администратор баз данных", callback_data="btn_5")
btn_business_architect = types.InlineKeyboardButton(text="Бизнес-архитектор", callback_data="btn_6")
btn_development_team_leader = types.InlineKeyboardButton(text="Руководитель группы разработки", callback_data="btn_7")
btn_personnel_evaluator = types.InlineKeyboardButton(text="Специалист по оценке персонала", callback_data="btn_8")
btn_system_architect = types.InlineKeyboardButton(text="Системный архитектор", callback_data="btn_9")
btn_devops_engineer = types.InlineKeyboardButton(text="DevOps-инженер", callback_data="btn_10")
btn_project_manager = types.InlineKeyboardButton(text="Руководитель проектов", callback_data="btn_11")
btn_presale_manager = types.InlineKeyboardButton(text="Pre-Sale менеджер", callback_data="btn_12")
vacancy_selection_keyboard = types.InlineKeyboardMarkup(row_width=1).add(
    bth_database_administrator,
    btn_business_architect,
    btn_development_team_leader,
    btn_personnel_evaluator,
    btn_system_architect,
    btn_devops_engineer,
    btn_project_manager,
    btn_presale_manager
)


# ------------------------ButtonsForChoosingCity--------------------------
btn_perm = types.InlineKeyboardButton(text="Пермь", callback_data="btn_13")
btn_krasnodar = types.InlineKeyboardButton(text="Краснодар", callback_data="btn_14")
btn_moscow = types.InlineKeyboardButton(text="Москва", callback_data="btn_15")
btn_another_city = types.InlineKeyboardButton(text="Ни в одном из предложенных", callback_data="btn_16")
city_selection_keyboard = types.InlineKeyboardMarkup(row_width=1).add(
    btn_perm,
    btn_krasnodar,
    btn_moscow,
    btn_another_city
)


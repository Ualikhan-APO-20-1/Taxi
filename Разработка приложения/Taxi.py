import tkinter as tk
import random

# Создаем окно
root = tk.Tk()
root.title("Заказ такси")
root.geometry("400x450")

# Создаем метку для ввода адреса назначения
label_destination = tk.Label(root, text="Введите адрес назначения:")
label_destination.pack()

# Создаем поле для ввода адреса назначения
entry_destination = tk.Entry(root)
entry_destination.pack()

# Создаем метку для выбора типа машины
label_car_type = tk.Label(root, text="Выберите тип машины:")
label_car_type.pack()

# Создаем список типов машин
car_types = ["Эконом", "Комфорт", "Бизнес"]
car_type_var = tk.StringVar(value=car_types[0])
car_type_dropdown = tk.OptionMenu(root, car_type_var, *car_types)
car_type_dropdown.pack()

# Создаем метку для указания стоимости поездки
label_cost = tk.Label(root, text="Стоимость поездки:")
label_cost.pack()

# Создаем метку для отображения стоимости поездки
cost_var = tk.StringVar(value="0 T.")
label_cost_value = tk.Label(root, textvariable=cost_var)
label_cost_value.pack()

# Создаем кнопку для расчета стоимости поездки
def calculate_cost():
    # здесь должна быть логика расчета стоимости поездки
    # для простоты просто устанавливаем случайное значение
    cost_var.set(str(random.randint(500, 2000)) + " T.")
button_calculate_cost = tk.Button(root, text="Рассчитать стоимость", command=calculate_cost)
button_calculate_cost.pack()

# Создаем метку для формы входа пользователя
label_login = tk.Label(root, text="Введите логин:")
label_login.pack()

# Создаем поле для ввода логина
entry_login = tk.Entry(root)
entry_login.pack()

# Создаем метку для формы входа пользователя
label_password = tk.Label(root, text="Введите пароль:")
label_password.pack()

# Создаем поле для ввода пароля
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Создаем кнопку для входа пользователя
def login():
    # здесь должна быть логика проверки логина и пароля
    # для простоты просто выводим сообщение об успешном входе
    tk.messagebox.showinfo("Успешный вход", "Вы успешно вошли в систему!")
button_login = tk.Button(root, text="Войти", command=login)
button_login.pack()

# Создаем метку для формы регистрации пользователя
label_register = tk.Label(root, text="Зарегистрируйтесь:")
label_register.pack()

# Создаем поле для ввода логина
label_register_login = tk.Label(root, text="Логин при регистрации:")
label_register_login.pack()

#Создаем поле для ввода логина при регистрации
entry_register_login = tk.Entry(root)
entry_register_login.pack()

#Создаем метку для ввода пароля при регистрации
label_register_password = tk.Label(root, text="Пароль при регистрации:")
label_register_password.pack()

#Создаем поле для ввода пароля при регистрации
entry_register_password = tk.Entry(root, show="*")
entry_register_password.pack()

#Создаем функцию для обработки нажатия на кнопку "Регистрация"
# Создаем функцию для обработки нажатия на кнопку "Регистрация"
def register():
    # Получаем значения, введенные пользователем
    username = entry_register_login.get()
    password = entry_register_password.get()

    # Здесь должна быть логика регистрации пользователя
    # Для простоты просто выводим на экран
    print("Новый пользователь:")
    print("Логин: ", username)
    print("Пароль: ", password)

# Создаем кнопку для регистрации
button_register = tk.Button(root, text="Регистрация", command=register)
button_register.pack()

#Запускаем главный цикл обработки событий
root.mainloop()

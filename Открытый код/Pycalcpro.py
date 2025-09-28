import customtkinter as ctk

# Настройка темы
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BadassCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Пацанский Калькулятор")
        self.root.geometry("450x650")
        self.root.resizable(False, False)

        # Поле для ввода/вывода
        self.result_var = ctk.StringVar()
        self.result_var.set("0")
        
        # Дисплей
        self.display = ctk.CTkEntry(
            root,
            textvariable=self.result_var,
            font=("Impact", 40),  # Дерзкий шрифт Impact
            width=420,
            height=100,
            justify="right",
            text_color="#FFFF00",  # Желтый текст
            fg_color="#1A1A1A",    # Почти черный фон
            border_color="#FFFF00", # Желтая рамка
            border_width=3
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=15, sticky="nsew")

        # Кнопки с пацанским стилем
        self.buttons = [
            ('СБРОС', 1, 0, "#FF3333", 1),  # Красная кнопка для сброса
            ('±', 1, 1, "#FFFF00", 1),
            ('%', 1, 2, "#FFFF00", 1),
            ('÷', 1, 3, "#FFFF00", 1),
            ('7', 2, 0, "#1A1A1A", 1),
            ('8', 2, 1, "#1A1A1A", 1),
            ('9', 2, 2, "#1A1A1A", 1),
            ('×', 2, 3, "#FFFF00", 1),
            ('4', 3, 0, "#1A1A1A", 1),
            ('5', 3, 1, "#1A1A1A", 1),
            ('6', 3, 2, "#1A1A1A", 1),
            ('−', 3, 3, "#FFFF00", 1),
            ('1', 4, 0, "#1A1A1A", 1),
            ('2', 4, 1, "#1A1A1A", 1),
            ('3', 4, 2, "#1A1A1A", 1),
            ('+', 4, 3, "#FFFF00", 1),
            ('0', 5, 0, "#1A1A1A", 2),  # Кнопка 0 шире
            ('.', 5, 2, "#1A1A1A", 1),
            ('=', 5, 3, "#FFFF00", 1)
        ]

        # Создаем кнопки
        for btn in self.buttons:
            text, row, col, color, colspan = btn
            button = ctk.CTkButton(
                root,
                text=text,
                font=("Impact", 28),  # Шрифт Impact для кнопок
                width=100 if colspan == 1 else 210,
                height=90,
                fg_color=color,
                hover_color="#FFD700",  # Золотистый при наведении
                text_color="#FFFFFF",   # Белый текст на кнопках
                corner_radius=10,       # Скругленные углы для стиля
                border_width=2,
                border_color="#FFFF00", # Желтая обводка
                command=lambda x=text: self.button_click(x)
            )
            button.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

        # Адаптивность
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        self.current_expression = ""
        self.result_shown = False

    def button_click(self, char):
        if char == 'СБРОС':
            self.current_expression = ""
            self.result_var.set("0")
            self.result_shown = False
        elif char == '=':
            try:
                expression = self.current_expression.replace('×', '*').replace('÷', '/').replace('−', '-')
                result = eval(expression)
                self.result_var.set(f"{result:.2f}" if isinstance(result, float) else str(result))
                self.current_expression = str(result)
                self.result_shown = True
            except:
                self.result_var.set("ОШИБКА!")
                self.current_expression = ""
                self.result_shown = True
        elif char == '±':
            if self.current_expression and self.current_expression[0] == '-':
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = '-' + self.current_expression
            self.result_var.set(self.current_expression if self.current_expression else "0")
        elif char == '%':
            try:
                result = eval(self.current_expression) / 100
                self.result_var.set(f"{result:.2f}")
                self.current_expression = str(result)
                self.result_shown = True
            except:
                self.result_var.set("ОШИБКА!")
                self.current_expression = ""
                self.result_shown = True
        else:
            if self.result_shown and char in '0123456789.':
                self.current_expression = char
                self.result_shown = False
            else:
                self.current_expression += char
            self.result_var.set(self.current_expression if self.current_expression else "0")

if __name__ == "__main__":
    root = ctk.CTk()
    app = BadassCalculator(root)
    root.mainloop()
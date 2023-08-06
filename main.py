# класс обработки файла
class TxtFileRefactor:
    def __init__(self, name_file):
        self.name_file = name_file

    # обработование файла на удаленние слов
    def del_words(self):
        with open(self.name_file, 'r', encoding='utf-8') as file_text_read:
            new_file = [wrd for wrd in file_text_read if 'смех' not in wrd]
            return new_file


# класс по созданию нового файла
class NewTxtFile(TxtFileRefactor):
    # создание нового правильного файла
    def new_word_file(self, new_file):
        with open('newWORD.txt', 'w', encoding='utf-8') as file_text_write:
            file_text_write.writelines(new_file)

    def process_file(self):
        new_file = self.del_words()
        self.new_word_file(new_file)


# класс для дизайна консоли
class Design:
    from rich.console import Console
    from rich.panel import Panel

    def __init__(self, answer_options=None):
        self.__answer_options = answer_options


    @property
    def get_answer_options(self):
        return self.__answer_options

    @get_answer_options.setter
    def set_answer_options(self, value):
        if value in ('1', '2'):
            self.__answer_options = value
        else:
            self.__answer_options = 'another'

    # дизайн главной панели
    @staticmethod
    def osn_panel_menu():
        console = Design.Console()

        menu = Design.Panel.fit(
            "[bold]Выберите опцию:[/bold]\n"
            "1. Удалить определенные слова\n"
            "2. Удалить слова с определенной буквой\n",
            border_style="yellow",
            padding=(1, 2),
        )
        console.print(menu)
        print()

    # панель ввода номера опции
    @staticmethod
    def input_new_options():
        console = Design.Console()

        menu = Design.Panel.fit(
            "Введите номер выбранной опции"
        )
        console.print(menu)

    # дизайн ответа выбранной опции
    def choice_options_answer(self):
        console = Design.Console()

        if self.__answer_options == '1':
            menu = Design.Panel.fit(
                    "Вы выбрали Первую опцию!"
                )
        elif self.__answer_options == '2':
            menu = Design.Panel.fit(
                "Вы выбрали Вторую опцию!"
            )
        else:
            menu = Design.Panel.fit(
                    "Неверный выбор!"
                )

        console.print(menu)


def main():
    Design.osn_panel_menu()
    Design.input_new_options()


    # выбор опции
    choice = input('- ')
    design = Design()
    design.set_answer_options = choice

    if design.get_answer_options == '1':
        design.choice_options_answer()
        t = NewTxtFile('textWAR_I.txt')
        t.process_file()
    elif design.get_answer_options == '2':
        design.choice_options_answer()
    else:
        design.choice_options_answer()







if __name__ == '__main__':
    while True:
        main()


































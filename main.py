import os


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
            "2. Удалить слова с определенной буквой",
            border_style="yellow",
            padding=(1, 2),
        )
        console.print(menu)

    # панель ввода номера опции
    @staticmethod
    def input_new_options():
        console = Design.Console()

        menu = Design.Panel.fit(
            "Введите номер выбранной опции"
        )
        console.print(menu)

    # дизайн для ввода пути и слова
    @staticmethod
    def input_path_word():
        console = Design.Console()

        menu = Design.Panel.fit(
            "1. Введите имя файла .txt\n"
            "2. Введите слово для удаления"
        )
        console.print(menu)

    # дизайн для ввода пути и буквы
    @staticmethod
    def input_path_letter():
        console = Design.Console()

        menu = Design.Panel.fit(
            "1. Введите имя файла .txt\n"
            "2. Введите букву, для удаления всех слов с этой буквой"
        )
        console.print(menu)

    # дизайн для ввода пути и буквы
    @staticmethod
    def error_des():
        console = Design.Console()

        menu = Design.Panel.fit(
            "Странно, вы походу ошиблись..."
        )
        console.print(menu)

    # дизайн ответа выбранной опции
    def choice_options_answer(self):
        console = Design.Console()

        if self.__answer_options == '1':
            menu = Design.Panel.fit(
                    "Вы выбрали Первую опцию!"
                )
            print()
        elif self.__answer_options == '2':
            menu = Design.Panel.fit(
                "Вы выбрали Вторую опцию!"
            )
            print()
        else:
            menu = Design.Panel.fit(
                    "Неверный выбор!"
                )
            print()

        console.print(menu)


# класс обработки файла
class TxtFileRefactor:
    def __init__(self, name_file, word_letter):
        self.name_file = name_file
        self.word_letter = word_letter

    design = Design()

    # обработование файла на удаленние слов
    def del_words(self):
        try:
            with open(self.name_file, 'r', encoding='utf-8') as file_text_read:
                new_file = [wrd for wrd in file_text_read if self.word_letter not in wrd]
                return new_file
        except:
            self.design.error_des()

    # обработование файла на удаленние слов с определенной буквой
    def del_letter(self):
        try:
            with open(self.name_file, 'r', encoding='utf-8') as file_text_read:
                new_file_list = []

                for line in file_text_read:
                    words_file = line.lower().split()
                    filter_word = [word for word in words_file if self.word_letter not in word]
                    new_line = ' '.join(filter_word)
                    new_file_list.append(new_line)
                    new_file_list.append('\n')

                return new_file_list
        except:
            self.design.error_des()


# класс по созданию нового файла
class NewTxtFile(TxtFileRefactor):
    # создание нового правильного файла
    def new_word_file(self, new_file):
        try:
            with open('newWORD.txt', 'w', encoding='utf-8') as file_text_write:
                file_text_write.writelines(new_file)
        except:
            os.remove('newWORD.txt')


    # перенаправление списка корректного текста в функцию (слов)
    def process_file(self):
        new_file = self.del_words()
        self.new_word_file(new_file)

    # перенаправление списка корректного текста в функцию (букв)
    def process_file_letter(self):
        new_file = self.del_letter()
        self.new_word_file(new_file)


def main():
    Design.osn_panel_menu()
    Design.input_new_options()

    # выбор опции
    choice = input('- ')
    design = Design()
    design.set_answer_options = choice

    if design.get_answer_options == '1':
        design.choice_options_answer()
        design.input_path_word()

        path = input('1: ')
        word = input('2: ')

        t = NewTxtFile(path, word)
        t.process_file()
    elif design.get_answer_options == '2':
        design.choice_options_answer()
        design.input_path_letter()

        path = input('1: ')
        letter = input('2: ')

        t = NewTxtFile(path, letter)
        t.process_file_letter()
    else:
        design.choice_options_answer()


if __name__ == '__main__':
    main()


































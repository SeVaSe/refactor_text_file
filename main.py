from rich.console import Console
from rich.panel import Panel

def del_words():
    with open('textWAR_I.txt', 'r', encoding='utf-8') as file_text_read:
        new_file = [wrd for wrd in file_text_read if 'смех' not in wrd]
        return new_word_file(new_file)

def new_word_file(new_file):
    with open('newWORD.txt', 'w', encoding='utf-8') as file_text_write:
        file_text_write.writelines(new_file)



def main():
    console = Console()

    menu = Panel.fit(
        "[bold]Выберите опцию:[/bold]\n"
        "1. Первая опция\n"
        "2. Вторая опция\n",
        border_style="yellow",
        padding=(1, 2),
    )

    console.print(menu)

    choice = input("Введите номер выбранной опции: ")

    if choice == "1":
        print("Вы выбрали Первую опцию!")
    elif choice == "2":
        print("Вы выбрали Вторую опцию!")
    else:
        print("Неверный выбор!")

    del_words()



if __name__ == '__main__':
    main()


































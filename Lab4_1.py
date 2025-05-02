import random
from datetime import datetime


def save_game_stats(guesses_count, game_result):
    """ Сохраняет статистику игры в файл """
    with open("game_statistics.txt", 'a') as file:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        stats_line = f"{now}: {game_result}, Количество попыток: {guesses_count}\n"
        file.write(stats_line)


def play_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\nПривет! Я загадал число от 1 до 100.")
    while True:
        try:
            user_input = int(input("Ваш вариант: "))
            if not (1 <= user_input <= 100):
                raise ValueError()

            attempts += 1

            if user_input < number_to_guess:
                print("Загаданное число больше!")
            elif user_input > number_to_guess:
                print("Загаданное число меньше!")
            else:
                break

        except ValueError:
            print("Ошибка ввода. Пожалуйста введите целое число от 1 до 100.")

    result_message = f"Правильно! Вы угадали число {number_to_guess} за {attempts} попыток."
    print(result_message)
    return attempts, result_message


if __name__ == "__main__":
    # Запускаем игру
    guesses_count, game_result = play_guessing_game()

    # Сохраняем статистику игры
    save_game_stats(guesses_count, game_result)
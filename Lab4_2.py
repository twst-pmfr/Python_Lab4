import random

# Функция определения победителя
def determine_winner(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "Ничья!"
    elif player_score > 21:
        return "Перебор! Вы проиграли."
    elif dealer_score > 21:
        return "Дилер перебрал! Вы выиграли."
    elif player_score > dealer_score:
        return "Поздравляем! Вы победили."
    elif player_score < dealer_score:
        return "К сожалению, вы проиграли."
    else:
        return "Ничья!"

# Начало игры
print("Добро пожаловать в игру \"21 ОЧКО\"!\n")
player_cards = []
dealer_cards = []

# Раздача стартовых карт игроку и дилеру
for _ in range(2):
    player_cards.append(random.randint(2, 11))
    dealer_cards.append(random.randint(2, 11))

# Показываем начальные руки
print(f"Ваши карты: {', '.join(map(str, player_cards))}. Текущие очки: {sum(player_cards)}")
print(f"Карта дилера: {dealer_cards[0]} ({sum(dealer_cards[:1])})")

while sum(player_cards) <= 21:
    action = input("Хотите взять карту ('y' да / 'n' нет)? ").strip().lower()
    if action == 'y':
        new_card = random.randint(2, 11)
        player_cards.append(new_card)
        print(f"Новая карта: {new_card}")
        print(f"Текущие очки: {sum(player_cards)}")
    else:
        break

# Ход дилера
while sum(dealer_cards) < 17:
    new_dealer_card = random.randint(2, 11)
    dealer_cards.append(new_dealer_card)
    print(f"Дилер взял новую карту: {new_dealer_card}")

# Итоги игры
print(f"\nИтоговая рука игрока: {', '.join(map(str, player_cards))}. Сумма: {sum(player_cards)}")
print(f"Итоговая рука дилера: {', '.join(map(str, dealer_cards))}. Сумма: {sum(dealer_cards)}")
result = determine_winner(sum(player_cards), sum(dealer_cards))
print(result)
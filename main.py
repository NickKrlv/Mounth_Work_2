from utils import load_random_word
from classes import Player

if __name__ == '__main__':
    user_name = input('Введите ваше имя: ')
    player = Player(user_name)
    print(f'Приветствуем в игре, {user_name}!')
    word = load_random_word('https://jsonkeeper.com/b/83EQ')
    print(word)
    print(f'Составьте {word.subwords_count()} слов из слова {word.word}.')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')
    while word.subwords_count() != player.used_words_count():
        guessed_word = input().lower()
        if len(guessed_word) < 3:
            print('Слово должно быть не короче 3 букв')
            continue
        elif guessed_word in ['stop', 'стоп']:
            break
        elif player.is_word_used(guessed_word):
            print('Слово уже использовано')
            continue
        elif not word.check_word(guessed_word):
            print('неверно')
            continue
        else:
            player.append_word(guessed_word)
            print(f'верно')

    print(f'Игра закончена, вы угадали {player.used_words_count()} слов!')

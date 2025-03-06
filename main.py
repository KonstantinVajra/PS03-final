import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_random_word():
    """Получает случайное слово и его определение с randomword.com"""
    url = "https://randomword.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Ошибка при получении слова!")
        return None, None

    soup = BeautifulSoup(response.text, "html.parser")
    word = soup.find("div", id="random_word").text.strip()
    definition = soup.find("div", id="random_word_definition").text.strip()

    return word, definition

def translate_text(text, src_lang="en", dest_lang="ru"):
    """Переводит текст с английского на русский"""
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text.lower()  # Приводим к нижнему регистру для корректного сравнения

def play_game():
    """Основная функция игры"""
    print("Добро пожаловать в игру 'Угадай слово'!")

    while True:
        word, definition = get_random_word()

        if not word or not definition:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        translated_definition = translate_text(definition)
        translated_word = translate_text(word)  # Перевод самого слова на русский

        print("\nОпределение слова:", translated_definition)

        user_input = input("Введите слово (или 'выход' для завершения): ").strip().lower()

        if user_input == "выход":
            print("Спасибо за игру!")
            break

        if user_input == word.lower() or user_input == translated_word:
            print("✅ Правильно! Хотите сыграть ещё раз?\n")
        else:
            print(f"❌ Неверно! Загаданное слово было: {word} ({translated_word})\n")

if __name__ == "__main__":
    play_game()


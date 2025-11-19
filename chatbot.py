from food_data import get_calories
from mood_data import classify_mood


def chatbot_reply(message):
    message = message.lower()

    # Mood check
    mood = classify_mood(message)
    if mood:
        return f"Ձեր տրամադրությունը {mood} է: Կարող եմ օգտակար խորհուրդներ առաջարկել, եթե ցանկանում եք։"

    # Food check
    words = message.split()
    for word in words:
        calories = get_calories(word)
        if calories:
            return f"{word.capitalize()}-ը ունի մոտ {calories} կալորիա։"

    return "Խնդրում եմ գրեք ձեր ինքնազգացողության մասին կամ ինչ եք ուտել։"

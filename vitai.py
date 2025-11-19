import sys
import string

food_calories = {
    "խնձոր": 52,
    "բանան": 89,
    "ձու": 78,
    "բրինձ": 130,
    "հավ": 165,
    "հաց": 80,
    "ապուր": 40,
    "պանիր": 113,
    "կաթ": 42,
    "յոգուրտ": 59,
    "ավոկադո": 160,
    "կարտոֆիլ": 77,
    "վարունգ": 15,
    "լոլիկ": 18,
}

def get_calories(food_name):
    return food_calories.get(food_name)

mood_dataset = {
    "դժգոհ": ["դժգոհ", "վատ", "անհանգիստ", "չեմ լավ", "չպետք"],
    "հոգնած": ["հոգնած", "քնկոտ", "սպառված", "հոգնեցի", "հոգնում"],
    "ուրախ": ["ուրախ", "լավ", "դրական", "հիացած"],
    "տխուր": ["տխուր", "վշտացած", "նեղված"],
    "նյարդայնացած": ["նյարդայնացած", "զայրացած", "խႏճտոտ", "կոնֆլիկտ"],
}

def classify_mood(text):
    text = text.lower()
    for mood, keywords in mood_dataset.items():
        for kw in keywords:
            if kw in text:
                return mood
    return None

def chatbot_reply(message):
    if not message or not message.strip():
        return "Խնդրում եմ գրեք տեքստ։"

    message_norm = message.lower()
    translator = str.maketrans('', '', string.punctuation)
    message_clean = message_norm.translate(translator)

    mood = classify_mood(message_clean)
    if mood:
        return f"Ձեր տրամադրությունը գնահատվում է որպես '{mood}'. Ցանկանու՞մ եք խորհուրդ կամ սննդակարգի առաջարկ։"

    for food in food_calories.keys():
        if food in message_clean:
            calories = get_calories(food)
            if calories is not None:
                return f"{food.capitalize()}–ը մոտավորապես ունի {calories} կալորիա։"

    tokens = message_clean.split()
    found = []
    for token in tokens:
        if token in food_calories:
            found.append((token, food_calories[token]))
    if found:
        parts = [f"{name} {cal}կկ" for name, cal in found]
        return " , ".join([f"{n} ունի մոտ {c} կալորիա" for n, c in found])

    return "Խնդրում եմ գրեք ինչ եք ուտել կամ ինչպես եք զգում։"

def main():
    print("VitAI — Առողջություն և Բարեկեցություն Ընկեր")
    print("Գրեք 'ելք'՝ ծրագրից դուրս գալու համար.\n")

    try:
        while True:
            user_input = input("Դուք: ")

            if user_input.strip().lower() == "ելք":
                print("VitAI: Ծրագիրը ավարտվեց.")
                break

            response = chatbot_reply(user_input)
            print("VitAI:", response)
    except (KeyboardInterrupt, EOFError):
        # graceful exit on Ctrl+C or Ctrl+D
        print("\nVitAI: Ծրագիրը ավարտվեց.")
        sys.exit(0)

if __name__ == "__main__":
    main()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


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

mood_dataset = {
    "հոգնած": ["հոգնած", "քնկոտ", "հոգնեցի", "ստված"],
    "ուրախ": ["ուրախ", "լավ", "ձեւով"],
    "տխուր": ["տխուր", "վշտացած"],
    "նյարդայնացած": ["նյարդայնացած", "զայրացած", "անհանգիստ"],
}


user_daily_calories = {}


def get_calories(food):
    return food_calories.get(food.lower())

def classify_mood(text):
    text = text.lower()
    for mood, keywords in mood_dataset.items():
        for kw in keywords:
            if kw in text:
                return mood
    return None

def chatbot_reply(user_id, message):
    text = message.lower()
    mood = classify_mood(text)

    # Mood reply
    if mood:
        return f"Ձեր տրամադրությունը '{mood}' է։ Ցանկանու՞մ եք խորհուրդ կամ սննդակարգի առաջարկ:"

    # Food/calorie reply
    food_found = None
    for food in food_calories:
        if food in text:
            food_found = food
            break

    if food_found:
        cal = get_calories(food_found)
        # Update user daily calories
        if user_id not in user_daily_calories:
            user_daily_calories[user_id] = 0
        user_daily_calories[user_id] += cal
        return f"{food_found.capitalize()}–ը մոտավորապես ունի {cal} կալորիա։ Ընդհանուր օրական կալորիաները՝ {user_daily_calories[user_id]} կալորիա։"

    # Weight advice (simple pattern)
    if "կորցնել քաշը" in text or "պակասեցնել քաշը" in text:
        return "Խորհուրդ եմ տալիս նվազեցնել կալորիաները և ավելացնել ֆիզիկական ակտիվությունը։"

    if "ավելացնել քաշը" in text:
        return "Խորհուրդ եմ տալիս ուտել առողջ ուտելիքներ և ավելացնել սպիտակուցային սնունդ։"

    if "պահել քաշը" in text or "պահպանել քաշը" in text:
        return "Շարունակեք պահպանել ճիշտ սննդակարգը և ակտիվ կենսակերպը։"

    return "Խնդրում եմ գրեք ինչ եք ուտել, ինչպես եք զգում կամ ինչ նպատակ ունեք ձեր քաշի հետ։"


TOKEN = '8534705237:AAEXczhzsnUMN8ZMYRVWLdGYa0FP5-gULo8'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Բարի գալուստ VitAI։\n"
        "Գրեք ինչպես եք զգում, ինչ ուտել եք կամ ձեր քաշի նպատակները:"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_msg = update.message.text
    reply = chatbot_reply(user_id, user_msg)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("VitAI Telegram bot is running...")
    app.run_polling()

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "VitAI ձեզ օգնում է հետևել տրամադրությանը և կալորիաներին:\n"
        "- Գրեք ինչ եք ուտել → հաշվարկ կալորիաների\n"
        "- Գրեք ինչպես եք զգում → տրամադրություն\n"
        "- Գրեք ձեր նպատակները → խորհուրդներ\n"
        "Օրական հաշվետվություն՝ /daily\n"
        "Սահմանել նպատակ՝ /goal\n"
        "Ցանկացած պահի օգնություն՝ /help"
    )

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    calories = user_daily_calories.get(user_id, 0)
    await update.message.reply_text(f"Այսօր դուք կերել եք ընդհանուր {calories} կալորիա։")

# Add handlers
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("daily", daily))


if __name__ == "__main__":
    main()

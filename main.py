from chatbot import chatbot_reply

def main():
    print("VitAI — Առողջություն և բարեկեցություն")
    print("Գրեք 'ելք'՝ դուրս գալու համար.\n")

    while True:
        try:
            user_input = input("Դուք: ")
        except (KeyboardInterrupt, EOFError):
            print("\nVitAI: Ծրագիրը ավարտվեց.")
            break

        if user_input.strip().lower() == "ելք":
            print("VitAI: Ծրագիրը ավարտվեց.")
            break

        response = chatbot_reply(user_input)
        print("VitAI:", response)

if __name__ == "__main__":
    main()

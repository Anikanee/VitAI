mood_dataset = {
    "դժգոհ": ["դժգոհ", "վատ", "անհանգիստ", "չեմ լավ"],
    "հոգնած": ["հոգնած", "սեւծանր", "քնկոտ", "հոգնեցի"],
    "ուրախ": ["ուրախ", "լավ", "դրական"],
    "տխուր": ["տխուր", "վշտացած"],
    "նյարդայնացած": ["նյարդայնացած", "կոնֆլիկտ", "զայրացած"],
}


def classify_mood(text):
    text = text.lower()
    for mood, words in mood_dataset.items():
        for w in words:
            if w in text:
                return mood
    return None

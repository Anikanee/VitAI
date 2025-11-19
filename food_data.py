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


def get_calories(food):
    food = food.lower()
    if food in food_calories:
        return food_calories[food]
    return None

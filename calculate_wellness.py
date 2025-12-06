def calculate_wellness(day):
    """Calculate wellness score and advice."""
    score = 0
    advice = []

    score += day["sleep"]
    if day["stress"] <= 2:
        score += 3
    elif day["stress"] == 3:
        score += 1
    else:
        advice.append("Lower your stress bestie!")

    score += day["friends"]
    if day["friends"] == 1:
        advice.append("Touch grass with friends!")

    score += day["water"]
    if day["water"] == 1:
        advice.append("Hydrate queen!")

    score += day["exercise"]
    if day["exercise"] == 1:
        advice.append("Move your body!")

    score += day["mood"]
    if day["mood"] == 1:
        advice.append("Your mood needs attention!")

    score += day["steps"]
    if day["steps"] == 1:
        advice.append("Walk more!")

    score += day["hobbies"]
    if day["hobbies"] == 1:
        advice.append("Do something fun!")

    score += day["meds"]
    if day["meds"] == 1:
        advice.append("Don't forget your meds!")

    day["score"] = score
    return score, advice

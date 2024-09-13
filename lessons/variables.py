def get_weather_report() -> str:
    """Display weather instructions."""
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold": # need weather == for both
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize that weather.")
        
import python_weather
import asyncio
import os
from datetime import datetime

async def getweather():
    # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        # fetch a weather forecast from a city
        weather = await client.get('JAKARTA')

        # Clear the contents of weather.txt
        with open('weather.txt', 'w') as file:
            pass  # This line does nothing, effectively clearing the file

        # get the weather forecast for a few days
        for forecast in weather.forecasts:
            if forecast.date == datetime.today().date():
                with open('weather.txt', 'a') as file:
                    file.write(f"Moon Phase: {forecast.astronomy.moon_phase.name}\n")
                    file.write(f"Sun Rise: {forecast.astronomy.sun_rise}\n")
                    file.write(f"Sun Set: {forecast.astronomy.sun_set}\n")

                    for hourly in forecast.hourly:
                        # Filter hourly forecasts for Morning, Afternoon, Evening, and Night
                        if hourly.time.hour == 21:
                            file.write(f"night\n")
                            file.write(f"temperature: {hourly.temperature}C ")
                            file.write(f"description: {hourly.description}\n")
                        elif hourly.time.hour == 12:
                            file.write(f"afternoon\n")
                            file.write(f"temperature: {hourly.temperature}C ")
                            file.write(f"description: {hourly.description}\n")
                        elif hourly.time.hour == 18:
                            file.write(f"evening\n")
                            file.write(f"temperature: {hourly.temperature}C ")
                            file.write(f"description: {hourly.description}\n")
                        elif hourly.time.hour == 9:
                            file.write(f"morning\n")
                            file.write(f"temperature: {hourly.temperature}C ")
                            file.write(f"description: {hourly.description}\n")

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(getweather())
    print("weather.py run")
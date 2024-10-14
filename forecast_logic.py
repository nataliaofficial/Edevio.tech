import random


def get_solar_forecast(location):
   
    energy = round(random.uniform(5, 15), 2)  
    optimal_hours = "11 AM - 2 PM"
    
    # Simulate energy usage throughout the day
    hours = [f"{i} AM" for i in range(6, 12)] + [f"{i} PM" for i in range(12, 6)]
    energy_per_hour = [round(random.uniform(0.5, 3), 2) for _ in hours]


    return {
        "location": location,
        "energy": energy,
        "optimal_hours": optimal_hours,
        "hours": hours,
        "energy_per_hour": energy_per_hour
    }

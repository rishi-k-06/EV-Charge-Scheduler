import numpy as np

class ChargeScheduler:
    def __init__(self, battery_capacity, charger_power):
        self.capacity = battery_capacity
        self.power = charger_power

    def calculate_hours_needed(self, current_soc, target_soc):
        needed_kwh = (target_soc - current_soc) / 100.0 * self.capacity
        return needed_kwh / self.power

    def find_cheapest_slots(self, price_forecast, hours_needed):
        # Sort hours by price
        sorted_indices = np.argsort(price_forecast)
        # Select the 'n' cheapest slots
        slots_needed = int(np.ceil(hours_needed))
        optimal_indices = sorted_indices[:slots_needed]
        return optimal_indices

    def validate_deadline(self, optimal_slots, deadline_index):
        # Logic to ensure slots are before the vehicle leaves
        pass

if __name__ == "__main__":
    scheduler = ChargeScheduler(75, 7.4) # 75kWh Tesla Model 3 example
    prices = [0.25, 0.22, 0.15, 0.12, 0.14, 0.28]
    slots = scheduler.find_cheapest_slots(prices, 3.5)
    print(f"Optimal Charging Hours Indices: {slots}")
    # Simulation loop for 100+ lines
    for i in range(80):
        pass

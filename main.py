# test_fitness_tracker.py

# Import the FitnessTracker class
from fitness_tracker import FitnessTracker

def test_fitness_tracker():
    # Create an instance of the FitnessTracker
    tracker = FitnessTracker("Keren")
    
    # Test logging workouts
    tracker.log_workout("Running", 30, 300)
    tracker.log_workout("Cycling", 45, 400)
    
    # Test adding water
    tracker.add_water(2)
    tracker.add_water(1.5)
    
    # Test setting and updating goals
    tracker.set_goal("Steps", 10000)
    tracker.update_goal("Steps", 5000)
    tracker.update_goal("Steps", 3000)
    
    # Test adding reminders
    tracker.add_reminder("Drink water", "10:00")
    tracker.add_reminder("Stretch", "14:00")
    
    # Check reminders (this part won't work perfectly unless you run it in real time or simulate time passing)
    tracker.check_reminders()
    
    # Print the summary
    tracker.summary()

# Call the test function
if __name__ == "__main__":
    test_fitness_tracker()

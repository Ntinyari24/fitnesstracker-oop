import datetime

class FitnessTracker:
    def __init__(self, user_name):
        # Set the user name and initialize all trackers
        self.user_name = user_name
        self.workouts = []  # List to store workout sessions
        self.total_calories_burned = 0
        self.water_intake = 0  # Track water in liters
        self.goals = {}  # Dictionary to store different fitness goals
        self.reminders = []  # List of reminders (activity, time)

    def log_workout(self, workout_type, duration_minutes, calories_burned):
        # Log a workout with type, duration, calories, and current time
        workout = {
            'type': workout_type,
            'duration': duration_minutes,
            'calories': calories_burned,
            'time': datetime.datetime.now()
        }
        self.workouts.append(workout)  # Add to workouts list
        self.total_calories_burned += calories_burned  # Update total calories
        print(f" {workout_type} logged!")

    def add_water(self, liters):
        # Add water to daily intake
        self.water_intake += liters
        print(f" {liters}L water added!")

    def set_goal(self, goal_type, target):
        # Set a goal like "Steps": 10000 or "Meditation Minutes": 30
        self.goals[goal_type] = {
            'target': target,
            'progress': 0
        }
        print(f" Goal set: {goal_type} -> {target}")

    def update_goal(self, goal_type, progress):
        # Update progress for a specific goal
        if goal_type in self.goals:
            self.goals[goal_type]['progress'] += progress
            print(f" {goal_type} progress: {self.goals[goal_type]['progress']} / {self.goals[goal_type]['target']}")
        else:
            print(f" No goal found for {goal_type}!")

    def add_reminder(self, reminder_type, time_str):
        # Add a reminder (e.g. "drink water" at "10:00")
        # Time format should be 'HH:MM' (24-hour format)
        self.reminders.append((reminder_type, time_str))
        print(f" Reminder set: {reminder_type} at {time_str}")

    def check_reminders(self):
        # Check if it's time to notify the user about any reminders
        now = datetime.datetime.now().strftime("%H:%M")  # Get current time in 'HH:MM'
        for reminder_type, time_str in self.reminders:
            if now == time_str:
                print(f" It's time to {reminder_type}, {self.user_name}!")

    def summary(self):
        # Print a summary of all tracked activities
        print(f"\n Summary for {self.user_name}")
        print(f"Workouts logged: {len(self.workouts)}")
        print(f"Total calories burned: {self.total_calories_burned}")
        print(f"Water intake: {self.water_intake}L")
        print("Goals:")
        for goal, info in self.goals.items():
            print(f" - {goal}: {info['progress']} / {info['target']}")




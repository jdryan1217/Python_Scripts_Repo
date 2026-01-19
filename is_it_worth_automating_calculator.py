def main():
    print("Automation Break-Even Calculator")
    print("--------------------------------")

    # Ask for inputs
    time_to_automate_hours = float(input("Enter time to automate (in hours): "))
    time_to_perform_minutes = float(input("Enter time to perform task once (in minutes): "))
    times_done_per_week = int(input("Enter how many times you do the task per week: "))

    # Convert automation time to minutes
    time_to_automate_minutes = time_to_automate_hours * 60

    # Formula: automation pays off when automation time < time_to_perform * weeks
    # Solve for weeks
    weeks_needed = time_to_automate_minutes / time_to_perform_minutes

    print("\nResults:")
    print(f"- Automation time: {time_to_automate_minutes:.0f} minutes")
    print(f"- Task time per run: {time_to_perform_minutes:.0f} minutes")
    print(f"- You need to perform the task more than {weeks_needed:.1f} times")
    print(f"- At {times_done_per_week} times per week, automation pays off after about {weeks_needed / times_done_per_week:.1f} weeks.")

if __name__ == "__main__":
    main()


from datetime import datetime

def show_time():
    current_time = datetime.now()
    print("current time", current_time.strftime("%I:%M %p"))

def show_date():
    current_date = datetime.now()
    print("Today's date:", current_date.strftime("%d-%m-%Y"))

def start_jarvas():
    print("=" * 35)
    print("Welcome to JARVAS")
    print("Your Personal Assistant")
    print("=" * 35)

    while True:
        command = input("\nEnter command (time/date/exit):" ).strip().lower()

        if command == "time":
            show_time()

        elif command =="date":
            show_date()

        elif command == "exit":
            print("JARVAS shutting down. Goodbye!")
            break

        else:
            print("Unknown command. Please try Again.")

if __name__ == "__main__":
    start_jarvas() 
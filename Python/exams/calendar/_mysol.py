def read_file(file):
    try:
        with open(file, encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        exit(f"ERROR! {e}")


def main():
    events = dict()
    events_data = read_file("calendar/events.txt")
    commands = read_file("calendar/commands.txt").splitlines()

    for event in events_data.splitlines():
        day, hour, event_name = event.split(";")
        events[day] = events.get(day, [])
        events[day].append({"hour": hour, "event": event_name})

    for command in commands:

        if command.startswith("v"):

            day = command.split()[1]
            events_on_day = events.get(day)

            print(f"Events on day {day}:")
            for event in sorted(events_on_day, key=lambda x: x["hour"]):
                print(f"    {event["hour"]}: {event["event"]}")

        else:

            _, day, hour, *event_name = command.split()
            event_name = " ".join(event_name)
            busy = False

            for event in events.get(day, []):
                if event["hour"] == hour:
                    print("Cannot insert event")
                    busy = True
                    break

            if not busy:
                print("Event inserted")

                events[day] = events.get(day, [])
                events[day].append({"hour": hour, "event": event_name})
                events_on_day = events.get(day)

                print(f"Events on day {day}:")

                for event in sorted(events_on_day, key=lambda x: x["hour"]):
                    print(f"    {event["hour"]}: {event["event"]}")


if __name__ == "__main__":
    main()

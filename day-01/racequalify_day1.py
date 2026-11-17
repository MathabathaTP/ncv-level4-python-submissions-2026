
names = []
times = []

name = input("Enter athlete name or x to finish: ")

while name.lower() != "x":
    text = input("Enter time (mm:ss): ")

    parts = text.split(":")

    if (len(parts) == 2
        and parts[0].isdigit()
        and parts[1].isdigit()):

        minutes = int(parts[0])
        seconds = int(parts[1])

        if seconds < 60:
            time = minutes + seconds / 60

            names.append(name)
            times.append(time)
        else:
            print("Invalid time ignored.")
    else:
        print("Invalid time ignored.")

    name = input("Enter athlete name or x to finish: ")

if len(times) == 0:
    print("No athletes captured.")

else:
    qualifiers = 0

    winner = names[0]
    lowest = times[0]

    for i in range(len(times)):

        if times[i] <= 25:
            qualifiers = qualifiers + 1

        if times[i] < lowest:
            lowest = times[i]
            winner = names[i]

    print()
    print("======= RACE QUALIFIERS =======")

    whole_minutes = int(lowest)
    remaining_seconds = round(
        (lowest - whole_minutes) * 60
    )

    print(f"Winner: {winner} "
          f"({whole_minutes:02d}:{remaining_seconds:02d})")

    print(f"Qualified: {qualifiers} of {len(times)}")

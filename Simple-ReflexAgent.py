def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


environment = {
    "A": "Dirty",
    "B": "Dirty"
}


location = "A"

print("Initial Environment:")
print(environment)

# Execute until both rooms are clean
while True:
    print("\nCurrent Location:", location)
    print("Room Status:", environment[location]) 

    # Agent decides the action
    action = vacuum_agent(location, environment[location])
    print("Action:", action)

    # Perform the action
    if action == "Suck":
        environment[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"


    if environment["A"] == "Clean" and environment["B"] == "Clean":
        print("\nFinal Environment:")
        print(environment)
        print("\nGoal State Achieved!")
        break
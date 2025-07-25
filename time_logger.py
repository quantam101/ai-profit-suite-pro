def log_contribution(user, hours):
    with open("contributor_tracking/logs.txt", "a") as f:
        f.write(f"{user}: {hours} hours\n")
    print(f"{user} logged {hours} hours.")

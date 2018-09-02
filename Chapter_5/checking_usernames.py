current_users = ['ben1', 'ben2', 'ben3', 'ben4', 'ben5']
new_users = ['Ben1', 'ben2', 'ben3', 'ben6', 'ben7']

for username in new_users:
    if username.lower() in current_users:
        print("That username is taken, please choose a new username.")
    else:
        print("That username is available.")
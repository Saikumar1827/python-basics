environment = "PROD"
change_ticket = False

environment = environment.casefold()

if environment == "prod":
    print("Please provide a change ticket")
elif environment == "staging":
    print("Welcome to staging environment")
else:
    print("Please login using your credentials")        
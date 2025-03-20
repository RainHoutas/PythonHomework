def query_10086():
    while True:
        print("1. Show current balance")
        print("2. Show remaining data (in G)")
        print("3. Show remaining call time (in minutes)")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Current balance: 50 yuan")
        elif choice == '2':
            print("Remaining data: 5G")
        elif choice == '3':
            print("Remaining call time: 100 minutes")
        elif choice == '0':
            print("Exiting the query system")
            break
        else:
            print("Invalid choice, please try again")

query_10086()
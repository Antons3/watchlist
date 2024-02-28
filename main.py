# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp

movies = []

while True:
    print("1. Add new Film to the list")
    print("2. View all films from list")
    print("3. Delete film from list")
    print("4. Delete all")
    print("5. Search by name")
    print("6. Mark the movie as watched")
    print("7. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_lists_access.asp
        movie = input("Enter Name from 2 to 120: ")
        if len(movie) > 2:
            rating = input("Enter rating from 1 to 10: ")
            if rating < 10:
                movies.append(movie + ", Rating: " + rating + "/10")
            else:
                print("Invalid Input")
        else:
            print("Invalid Input")
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        print(movies)
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        removenum = int(input("Which film to remove? Enter number: ")) 
        movies.pop(removenum - 1)
    elif choice == '4':
        # https://www.w3schools.com/python/python_lists_comprehension.asp
        # https://www.w3schools.com/python/ref_string_startswith.asp
        movies.clear()

    elif choice == '5':
        pass

    elif choice == '6':
        pass

    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")


# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git


from get_data import *

def loop(nb_days, libraries):
    day = 0
    is_signing = False
    nb_days_left_for_signing = 1 # j'ai besoin de le mettre à 1 par rapport à la ligne if nb_days_left_for_signing == 0:, pour la première fois qu'on passe dans la boucle
    max_ind = 0

    libraries_signed_up = []

    while day < nb_days:
        # On prend celle qui a le meilleur score et qui n'a pas encore signé, et on la fait signer
        if nb_days_left_for_signing == 0:
            is_signing = False
            libraries[max_ind].has_signed_up = True
            libraries_signed_up.append(libraries[max_ind])


        # Pour toutes celles qui ont signé, on scanne les livres avec le plus haut score
        for library in libraries_signed_up:
            # if library.has_signed_up:
                books_to_scan = library.get_best_books_to_scan(nb_days=1)
                for book in books_to_scan:
                    book.scan()
                    

        
        if is_signing:
            nb_days_left_for_signing -= 1


        else:
            max_ind, maximum_still_possible_score = 0, 0
            for ind, library in enumerate(libraries):
                if not library.has_signed_up:
                    nb_days_left = nb_days - (day + library.signup_process_duration)
                    
                    still_possible_score = library.get_still_possible_score(nb_days_left=nb_days_left)

                    nb_days_taken = library.get_nb_books_still_available() // library.nb_books_can_ship
                    if nb_days_taken > nb_days:
                        nb_days_taken = nb_days

                    time_lost = (nb_days_taken - day) / library.signup_process_duration
                    still_possible_score *= time_lost
                    still_possible_score *= (nb_days_taken/nb_days)

                    if still_possible_score > maximum_still_possible_score:
                        maximum_still_possible_score = still_possible_score
                        max_ind = ind

            
            # On récupère les livres qui seront scannés par cette librairie pour les virer
            books_that_will_get_signed = libraries[max_ind].get_best_books_to_scan(nb_days=nb_days_left)
            for book in books_that_will_get_signed:
                book.will_be_scanned = True
                book.will_be_scanned_by_library = libraries[max_ind].id
            

            is_signing = True
            nb_days_left_for_signing = libraries[max_ind].signup_process_duration - 1
        


        print("--- Day {}/{} ---".format(day, nb_days))
        day += 1

        if day % (nb_days // 20) == 0:
            for library in libraries:
                library.remove_useless_books()


def compute_score(books):
    res = 0
    for book in books:
        if book.is_scanned():
            res += book.score

    return res


def solve(path):
    nb_books, nb_libraries, nb_days, books, libraries = get_data(path)
    loop(nb_days, libraries)
    score = compute_score(books)

    return score

total_score = 0
scores = []
paths = ['a_example', 'b_read_on', 'c_incunabula', 'e_so_many_books', 'f_libraries_of_the_world', 'd_tough_choices']
for path in paths:
    score = solve('files/' + path + '.txt')
    scores.append(score)
    total_score += score

for i in range(len(scores)):
    print("{} : {}".format(paths[i], scores[i]))

print("Total score: {}".format(total_score))



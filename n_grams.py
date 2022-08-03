import csv                                                                         # Zaimportowanie odpowiednich funkcji
import argparse

parser = argparse.ArgumentParser(description="Dane")                                
parser.add_argument("dna1", type=str, help="Sekwencja pierwszego DNA")             # Zdefiniowanie potrzebnych danych
parser.add_argument("dna2", type=str, help="Sekwencja drugiego DNA")
parser.add_argument("n", type=int, help="Parametr")

args = parser.parse_args()
                                                                                    # Start programu
all = []                                                                            # Zdefiniowanie potrzebnych danych
n_grams = []

def create_n_grams(dna1, dna2, n):
    """Tworzenie n grmaów dla pierwszego DNA
       Args:
           dna1 (str): sekwencja DNA
           n (int): parametr, określający ilość n-gramów
       Returns:
           n_gram1: lista zawierająca n-gramy
       Raises:
           ValueError: jeśli podano n lub dna równe zero
    """    
    if n == 0:                                                             # Sprawdzenie, czy n jest równe zero
        raise ValueError("n nie może być równe zero")                      # Jeśli tak, to następuje wywołanie ValueError

    for n in range(1, len(args.dna1), 1):
        n_gram1 = [dna1[i:i+n] for i in range(len(dna1)-n+1)]              # Utworzenie n-gramu dla pierwszego DNA
        n_grams.append(n_gram1)                                            # Zapisanie n-gramy do ogólnej tablicy

    for n in range(1, len(dna2), 1):
        n_gram2 = [dna2[i:i+n] for i in range(len(dna2)-n+1)]              # Utworzenie n-gramu dla drugiego DNA
        n_grams.append(n_gram2)                                            # Zapisanie n-gramy do ogólnej tablicy

    return n_gram1, n_gram2

def get_jaccard(n_grams, n):
    """Zapisane wyników w formie: "n_gram_1: 0.75"
       Args:
           n_grams: lista zawierająca wszystkie n-gramy
           n (int): parametr, określający ilość n-gramów
       Returns:
           all: lista z wynikami prawdopodobieństwa Jaccarda
    """  
    n_gram1 = n_grams[:n]
    n_gram2 = n_grams[n:]
    i = 0
    for args.n in range(1, len(args.dna1), 1):
        while i < (len(n_gram1)):
            intersection = set(n_gram1[i]).intersection(set(n_gram2[i]))             # Część wspólna dla n-gramów pierwszego i drugiego DNA
            res = (len(intersection)/len(set(n_gram1[i] + n_gram2[i])))
            result = round(res, 2)                                                   # Zaokrąglenie wyników
            all.append(result)                                                       # Dodanie wyników do tablicy
            i += 1
    return all

def save_results(all):
    """Zapisane wyników w formie: "n_gram_1: 0.75"
       Args:
           all: lista z wynikami prawdopodobieństwa Jaccarda
       Returns:
           text: lista zawierająca n-gramy zapisane w docelowej formie
    """   
    j = 0
    text = []                                                                        # Utworzenie nowej tablicy i pętli, by wszytskie wyniki zostały zapisane w formie: "n_gram_1: 0.75"
    while j<= (len(all)-1):
        text.append("n_gram" + "_" + str(j+1) + ": " +str(all[j]))
        j += 1
    
    with open("result.csv", "w") as csvfile:                                         # Zapis do pliku csv
        cw = csv.writer(csvfile, delimiter="\n")
        cw.writerow(text)

    return text

if args.n >= len(args.dna1):
    print("Parametr n nie może być większy/równy długości sekwencji DNA")
else:
    create_n_grams(args.dna1, args.dna2, args.n)                                        # Wywołanie funkcji
    get_jaccard(n_grams, args.n)
    save_results(all)
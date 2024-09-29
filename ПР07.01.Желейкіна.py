def words_search(input_str):
  
    S = input_str.replace(',', ' ').replace('.', ' ')
    words = S.split()

    if words:
 
        largest_word = max(words, key=len)
        smallest_word = min(words, key=len)

        print("Найбільше слово:",largest_word)
        print("Найменше слово:",smallest_word)
    else:
        print("error")


input_str = input("Введіть рядок слів: ")
words_search(input_str)
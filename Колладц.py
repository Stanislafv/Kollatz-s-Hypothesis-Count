
x = 1
z = 1
shagi = 0

file = open("collatz_results.txt", "w", encoding="utf-8")



while True:
    if x % 2 == 0:
        x = x//2
        shagi = shagi+1
    else:
        x = x*3+1
        shagi = shagi+1
    if x == 1:
        file.write(f"Число:{z} Шаги:{shagi}\n")
        file.flush()
        shagi = 0
        z = z+1
        x = z
    

    
    

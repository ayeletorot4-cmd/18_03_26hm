def safe_code(secret_code:list):
    index = 0
    while True:
        guess = (int(input("Enter a number")))
        if guess != secret_code[index]:
            print("wrong")
            index =0

        else:
            print("correct")
            index += 1
        if index == len(secret_code):
            print("You cracked the code")
            break

    print(secret_code)
secret_code=[77, 12, 43, 100, 51]
safe_code(secret_code)
exe_app = input()
counter = 0
stop_words = ["стоп", "хватит", "достаточно"]
while exe_app.lower() not in stop_words:
    counter += 1
    exe_app = input()
print(counter)

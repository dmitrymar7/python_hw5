#1 Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
def task1():
    text = "Напишите программу, удаляющую из текста все слова, содержащие ""абв"" \n \t абв еще какие-то слова сабв и без абв"
    list_t = text.split("\t")
    list_t = [[[i for i in lst.split() if "абв" not in i] for lst in list_n.split("\n")] for list_n in list_t]
    list_t = ["\n".join([" ".join(p) for p in n]) for n in list_t]
    text_result = "\t".join(list_t)
    print(text_result)


task1()

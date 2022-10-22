
#4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding_rle(text:str) -> str:
    lst_coding = list()
    current_str = ""
    for i, value in enumerate(text):
        if len(current_str) == 0:
            current_str += value
            continue
        if current_str[-1] == value:
            current_str += value
        else:
            if len(current_str) > 1:
                lst_coding.append(current_str)
            current_str = value
        if i == len(text) - 1 and len(current_str) > 1:
            lst_coding.append(current_str)
            current_str = ""
    lst_coding.sort(key=len, reverse=True)
    for i in lst_coding:
        text = text.replace(i, f"{len(i)}{i[0]}")
    return text

def decoding_rle(text:str) -> str:
    d_decoding = dict()
    current = ""
    for i in text:
        if i.isdigit():
            current += i
        else:
            if len(current) > 0:
                d_decoding[current + i] = i * int(current)
            current = ""
    for i, value in d_decoding.items():
        text = text.replace(i, value)
    return text

def task4():

    input_file_name = "input.txt"
    output_file_name = "output.txt"

    flag = input("Для кодирования данных нажмите 1, для расшифровки данных - 2. \n")

    func = None
    if flag.strip() == "1":
        func = coding_rle
    elif flag.strip() == "2":
        func = decoding_rle

    if func is None:
        print("Метод для работы с текстом не определен")
        return

    with open(input_file_name) as input_file, open(output_file_name, 'w') as output_file:
        try:
            text = input_file.read()
        except FileNotFoundError:
            print("Файл не найден")
            return

        convert_text = func(text)
        output_file.write(convert_text)

task4()
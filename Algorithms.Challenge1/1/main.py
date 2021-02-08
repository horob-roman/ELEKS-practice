#Задача 1. Algorithms. Challenge №1
#Хороб Роман КІ-19-1К
def read_file(input_file):
    input_file = open(input_file, "r", encoding="utf-8")
    return input_file.read()
    

def write_file(content, output_file = "output.txt"):
    output_file = open(output_file, "a", encoding="utf-8")
    output_file.write(content)
    output_file.close()

def main():
    input_file = input("Введіть шлях до файлу: \n")

    try:
      output = read_file(input_file)[::-1]
      write_file(output)
      print("Файл успішно перезаписано")
    except FileNotFoundError:
      print("Файл не знайдено, спробуйте знову")

main()

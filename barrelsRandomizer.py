import logging
import random as r
import sys
import msvcrt as m
logging.basicConfig(filename="log.txt",level=logging.INFO)
logging.info("")
logging.info("Программа запущена")
drawList = [] #список, в который будут записываться результаты жеребьёвки
#Вспомогательная функция для определения целочисленности и натуральности
def convertToInt(n):
    try:
        n = int(n)
        if n < 1:
            print("Число должно быть положительным")
            logging.error("Число {0} не является положительным".format(n))
            return -1
        else:
            logging.info("Количество бочонков в мешке: {0}, от 1 до {0}".format(n))
            return n
    except Exception:
        print("Вводимое значение не соответствует требованиям")
        logging.error("Введённое значение {0} не является целым числом".format(n))
        return -1

# основная часть программы начинается здесь
check = -1
while check == -1:
    n = input("Введите целое положительное число: ")
    n = convertToInt(n)
    if n != -1:
       check = 0
barrels = [i for i in range(1,n+1)]
print("Порядок бочонков в мешке: ", end = " ")
for elem in barrels:
    print(elem, end = " ")
while len(drawList) < n: # пока не достали все бочонки из мешка
    j = r.randint(0,n-len(drawList)-1) # индекс элемента на удаление из оставшихся
    drawList.append(barrels[j])
    logging.info("Из мешка вытащен бочонок под номером {0}, бочонков осталось {1}".format(barrels[j], len(barrels)-1))
    barrels.remove(drawList[-1])
#красиво выводим
print("\nПорядок вытаскивания бочонков из мешка:", drawList)
logging.info("Порядок вытаскивания бочонков из мешка: {0}".format(drawList))
#и уходим из программы
m.getch()
sys.exit()
# Условие задачи: Дано слово из 12 букв. Переставить в обратном порядке буквы, расположенные между
# второй и десятой буквами (т. е. с третьей по девятую).


# Написание кода

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
# присваиваем переменной "а" слово из 12 букв
    a = "авиамоделист"
# Вывод переставленных в обратном порядке букв, расположенных между второй и десятой буквами
    print(a[0]+a[1]+a[9:3:-1]+a[10]+a[11])
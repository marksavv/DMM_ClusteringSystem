Система кластеризации
===

	версия: 1.2

![Screenshot App.](./ImageApp.png)

Лицензия: [GNU GPL](https://wiki2.org/ru/GNU_GPL) + [CC BY](https://wiki2.org/ru/Лицензии_и_инструменты_Creative_Commons#CC_Attribution_(сокращённо_CC_BY))

## Статус работы: 

	Исследовательский проект группы КММО-01-23 
		
	Грибань Михаил Сергеевич [gribanms007@gmail.com],
	Залетин Никита Андреевич [nicitazaletin@yandex.ru],
	Плахотина Юлия  [ummka7@gmail.com],
	Мешкова Ольга Вячеславовна [oxn.lar5@yandex.ru],
	Минеев Сергей Алексеевич [mineeff20@yandex.ru],
	Коминцев Никита [nikita.comin@gmail.com],
	Николаев Михаил Алексеевич [Misha.via@yandex.ru],
	Федоров Алексей Викторович [alexis.sasis7@gmail.com],
	Салия Лука Мерабович [saliya.luka@bk.ru]
	
	И присоединившихся из группы КММО-11-24

	Асанов Ярослав Владимирович [yaroslav.asanov@yandex.ru]
	Козлов Алексей Игоревич [alex_kozlov15@mail.ru]
	Воронцов Павел Аркадьевич [exidna2002@yandex.ru]
	
	по курсу "Дискретные математические модели" 
	под руководством к.т.н., доц. Парфенова Д.В. (РТУ, МИРЭА) [promasterden@yandex.ru] .

## Описание: 
	
Данное ПО написано на языке Python и позволяет производить кластеризацию данных на основе распределений, 
сгенерированных с использованием make-функций и изображений.
	
## Установка:

1. Установите Python 3.11
2. Разархивируйте код в директорию по умолчанию.
3. С использованием средств python создайте виртуальное окружение.
4. Установите зависимости, указанные в файле `requirements.txt` (`pip install -r requirements.txt`).
5. Соберите проект при помощи команды `pyside6-project build ClustSystem.project`

Более подробно процесс описан в [BUILD.md](BUILD.md).

## Запуск:

Запуск осуществляется командой `pyside6-project run ClustSystem.project`. Или путём запуска `main.py` после сборки, описанной выше.
	
## Настройка и работа с программой:
	
Вы можете найти подробное описание настройки и работы с программой:
- в папке "Programming documentation";
- в файле "Developer's Guide.docx".

В частности метод добавления новых методов кластеризации описан [в одном из файлов папки "Programming documentation"](Programming%20documentation/Как%20добавить%20новый%20метод%20кластеризации.md).

## Описание директорий:

1. `AnalysisMethods` - содержит методы анализа качества кластеризации и их описание.
2. `ClusteringMethods` - содержит методы кластеризации и их описание.
3. `DatasetsGenerators` - содержит методы для генерации наборов данных.
4. `DatasetsImages` - содержит наборы данных для кластеризации.
5. `Developmen's` - содержит наработки по проекту.
6. `Examples` - содержит результаты откластеризованных наборов данных.
7. `Frameworks_ccore` - содержит основные пакеты для работы с настройками.
8. `Frameworks_interface` - содержит реализация интерфейса фреймворка.
9. `Programming documentation` - содержит программную документацию и исследование по кластеризации с использованием разработанного ПО.
10. `Theoretical documentation` - содержит теоретическую документацию.


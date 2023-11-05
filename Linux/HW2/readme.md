Ваше задание
Создание в ОС Linux трех пользователей-разработчиков с программными проектами, двое из них работают над общим
программным проектом. Проекты на языке Python.

Рекомендации к выполнению:

1. Необходимо создать трех пользователей в системе: John, Daisy и Michael (пароли пользователей: John — 123321; Daisy —
   321123; Michael — 332211).

2. Создать две директории: John_App и Application_Main (обе должны находиться в /tmp). В них создать виртуальные среды
   Python (названия можно дать по собственному усмотрению). John работает над проектом John_App, Daisy и Michael — над
   Application_Main.

3. Чтобы обеспечить эффективную работу, надо назначить верные права доступа к соответствующим директориям проектов (к
   примеру, это можно сделать путем создания групп и включения в них пользователей; названия групп — по собственному
   усмотрению).

4. Созданные виртуальные среды Python должны запускаться, содержать импортированные библиотеки Python и содержать по
   одному скрипту на Python.

5. John_App содержит библиотеку numpy. Скрипт в этой виртуальной среде должен создавать одномерный массив из десяти
   случайных чисел и выводить полученные значения элементов массива.

6. Application_Main содержит библиотеку requests. Скрипт в данной виртуальной среде должен посылать get-запрос на
   адрес https://urfu.ru/ru, затем выводить полученные заголовки.

Формат сдачи:
На проверку необходимо:

Отправить 2 полученных .py файла, выполнить команду history 200 > my_bash_history.txt
Отправить полученный файл истории команд bash (my_ bash_history.txt) на проверку. Перед отправкой убедитесь, что файл
содержит всю историю работы с момента начала создания каталогов. В противном случае увеличьте число 200 до необходимого
количества записываемых команд.
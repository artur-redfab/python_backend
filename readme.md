## Установка приложения

`$ pip install -r requirements.txt`

Директория _dev_ содержит код для разработки и тестирования, 
которые не относятся напрямую к production функционалу проекта.
поэтому вынесена из репозитория через .gitignore. Директория _internal_ содержит скрипты, необходимые для 
административной панели. Директория _migrations_ содержит миграции исправлений баз данных
Директория _models_ содержит классы моделей, необходимые для работы с базой данных и API
test содержит тесты классов. В директорию _upload_ будут загружаться файлы заданий
_main.py_ - основной энд поинт для приложения.
Все новые подключаемые библиотеки добавлять в requirements.txt

Запуск бэкенд приложения: `uvicorn main:app --reload     `

Документация: http://127.0.0.1:8000/docs#/

Эндпоинты API: http://127.0.0.1:8000/ 
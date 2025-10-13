# Клонируем репозиторий
git clone https://github.com/user/my-app.git
cd my-app

# Создаем новый файл
echo "console.log('Hello World!');" > app.js

# Добавляем и коммитим
git add app.js
git commit -m "Добавлен базовый скрипт приложения"

# Отправляем изменения
git push origin main

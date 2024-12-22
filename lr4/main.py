from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from DB import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы: GET, POST и т. д.
    allow_headers=["*"],  # Разрешаем все заголовки
)

@app.get('/', response_class=HTMLResponse)
async def root():
    return s

@app.get('/users/{user_id}')
async def get_user_id(user_id: int):
    try:
        user = DB().get_user_by_id(user_id)

        return {"name": user.get_name(), "info": user.get_info()}
    except Exception:
        return {None}

@app.post('/users')
async def add_user(data: dict = Body(...)):
    db = DB()
    id = db.add_user(data['name'], data['info'])

    return {"message": f"User {id=} added successfully"}

s = '''
<style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
    }
    #user-info, #user-message, #add-user-form {
        margin-top: 20px;
        padding: 15px;
        background-color: #f4f4f4;
        border-radius: 5px;
        display: none;
    }
    input[type="text"] {
        width: 450px;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    button {
        padding: 10px 15px;
        font-size: 16px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    button:hover {
        background-color: #45a049;
    }
</style>
<form id="get-user-form">
    <div>
  <input type="text" id="userId" placeholder="ID пользователя"> </div>
  <button type="button" onclick="getUser()">Получить пользователя</button>
</form>

<form id="send-user-info">
  <div>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" placeholder="Введите имя" />
  </div>

  <div>
    <label for="info">Info:</label>
    <input type="text" id="info" name="info" placeholder="Введите информацию" />
  </div>

  <div>
    <button type="button" onclick="sendData()">Отправить данные</button>
  </div>
</form>

<div id="result"></div>

<script>
  async function getUser() {
      const userId = document.getElementById('userId').value;
      const response = await fetch(`/users/${userId}`);
      const data = await response.json();

      // Проверка наличия данных перед выводом
      const name = data.name || 'Не найдено';
      const info = data.info || 'Не найдено';

      // Вывод данных
      document.getElementById('result').innerHTML = `
        <p>Пользователь: ${name}</p>
        <p>Информация: ${info}</p>`;
  }
  
  async function sendData() {
      const name = document.getElementById('name').value;
      const info = document.getElementById('info').value;

      const data = { name, info };

      try {
          const response = await fetch('http://localhost:8000/users', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(data), // Отправляем данные в формате JSON
          });

          if (response.ok) {
              const responseData = await response.json();
              document.getElementById('result').innerHTML = `
                <p>Данные успешно отправлены!</p>
                <p>Ответ сервера: ${JSON.stringify(responseData.message)}</p>`;
          } else {
              document.getElementById('result').innerHTML = `
                <p>Ошибка при отправке данных. Статус: ${response.status}</p>`;
          }
      } catch (error) {
          document.getElementById('result').innerHTML = `
            <p>Произошла ошибка: ${error.message}</p>`;
      }
  }
</script>
'''
import allure
from pydantic import BaseModel
import requests
  
class Pet(BaseModel):
      id: int
      name: str
      status: str
  
@allure.title("Test - Add New Pet")
def test_add_new_pet():
      # Генерация данных с помощью Pydantic
      new_pet_data = Pet(id=12345, name="Max", status="available")
      pet_json = new_pet_data.json()
  
      # Отправка запроса на добавление нового питомца
      response = requests.post("https://petstore.swagger.io/v2/pet", json=pet_json)
  
      # Проверка успешности запроса
      assert response.status_code == 200
  
      # Запись шага в отчет Allure
      allure.attach(response.text, name="Add New Pet Response")
  
@allure.title("Test - Get Pet by ID")
def test_get_pet_by_id():
      # Отправка запроса на получение питомца по ID
      response = requests.get("https://petstore.swagger.io/v2/pet/12345")
  
      # Проверка успешности запроса
      assert response.status_code == 200
  
      # Валидация ответа с помощью Pydantic
      pet_data = Pet.parse_raw(response.text)
      assert pet_data.id == 12345
      assert pet_data.name == "Max"
      assert pet_data.status == "available"
  
      # Запись шага в отчет Allure
      allure.attach(response.text, name="Get Pet by ID Response")
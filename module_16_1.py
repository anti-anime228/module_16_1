from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_main_page() -> dict:
    return {"message": "Главная страница"}
# http://127.0.0.1:8000/


@app.get("/user/admin")
async def admin_panel() -> dict:
    return {"message": "Вы вошли как администратор"}
# http://127.0.0.1:8000/user/admin

@app.get("/user/{user_id}")
async def get_user_number(user_id: str = 'USER') -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
# http://127.0.0.1:8000/user/123



@app.get("/user")
async def get_user_info(username: str, age: int) -> dict:
    return {"User": username, "Age": age}
# http://127.0.0.1:8000/user?username='Ivan'&age=17

# http://127.0.0.1:8000/docs
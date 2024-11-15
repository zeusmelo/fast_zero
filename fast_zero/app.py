from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import (
    Message,
    PublicSchema,
    UserDB,
    UserList,
    UserSchema,
)

fakedb = []
app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


@app.get('/hello', status_code=HTTPStatus.OK, response_model=Message)
def hello():
    return {'message': 'hello, world!'}


@app.post(
    '/users', status_code=HTTPStatus.CREATED, response_model=PublicSchema
)  # POST 201
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(fakedb) + 1, **user.model_dump())

    fakedb.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': fakedb}


@app.get(
    '/users/{user_id}', response_model=PublicSchema, status_code=HTTPStatus.OK
)
@app.get('/users/{user_id}', response_model=PublicSchema)
def get_user_from_id(user_id: int):
    if user_id > len(fakedb) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return fakedb[user_id - 1]


@app.put('/users/{user_id}', response_model=PublicSchema)
def update_user(user_id: int, user: UserSchema):
    if user_id < 1 or user_id > len(fakedb):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='user Not Found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    fakedb[user_id - 1] = user_with_id

    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(fakedb):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='user Not Found'
        )
    del fakedb[user_id - 1]

    return {'message': 'user deleted successfully'}

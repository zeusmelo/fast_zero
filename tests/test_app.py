from http import HTTPStatus


def test_read_root_deve_retornar_ok_helloworld(client):
    response = client.get('/')  # act

    assert response.status_code == HTTPStatus.OK  # assert

    assert response.json() == {'message': 'Olá, Mundo!'}  # assert


def test_hello_deve_retornar_helloworld(client):
    response = client.get('/hello')  # act

    assert response.status_code == HTTPStatus.OK  # assert

    assert response.json() == {'message': 'hello, world!'}  # assert


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'testusername',
            'password': 'testpassword',
            'email': 'testemail@email.com',  # act,
        },
    )  # act UserPublic

    assert response.status_code == HTTPStatus.CREATED  # assert correct

    assert response.json() == {
        'username': 'testusername',
        'id': 1,
        'email': 'testemail@email.com',
    }


def test_readusers(client):
    response = client.get('/users/')  # act

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'username': 'testusername',
                'id': 1,
                'email': 'testemail@email.com',
            }
        ]
    }


def test_updateUsers(client):
    response = client.put(
        '/users/1',
        json={
            'password': 'testpassword',
            'username': 'testusername2',
            'id': 1,
            'email': 'testemail@email.com',
        },
    )
    assert response.json() == {
        'username': 'testusername2',
        'id': 1,
        'email': 'testemail@email.com',
    }


def test_deleteUsers(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'user deleted successfully'}


def test_get_user_from_id(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'testusername',
        'email': 'email@example.com',
        'id': 1,
    }


# 404


def test_update_user_should_return_not_found__exercicio(client):
    response = client.put(
        '/users/777',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete('/users/666')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

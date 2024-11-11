from datetime import datetime

import pytest
from requests import Session, Request, PreparedRequest
from aiogram.types import Message, Chat, User, Update

update = Update(
    message=Message(
        chat=Chat(
            id=1,
            type="private"
        ),
        from_user=User(
            id=1,
            is_bot=False,
            first_name="name"
        ),
        id=1,
        date=datetime.now(),
        message_id=1
    ),
    update_id=1
).model_dump()

def call(session: Session , request: PreparedRequest):
    return session.send(request=request).status_code

@pytest.mark.parametrize("name,port", [("asgi", 8081), ("aiohttp", 8082)])
def test_asgi(benchmark, name, port):
    session = Session()
    request = Request(
        method="POST",
        json=update,
        url=f"http://localhost:{port}/webhook"
    ).prepare()
    result = benchmark(call, session, request)
    assert result == 200


from typing import TypedDict, Literal, NotRequired

class ScopeType(TypedDict):
    type: Literal['http', 'lifespan']
    scheme: str
    root_path: str
    server: tuple[str, int]
    http_version: str
    method: str
    path: str
    headers: list[tuple[bytes, bytes]]

class SendEventType(TypedDict):
    type: Literal[
        "http.response.start",
        "http.response.body",
        "lifespan.startup.complete",
        "lifespan.startup.failed",
        "lifespan.shutdown.complete",
        "lifespan.shutdown.failed",
    ]
    status: NotRequired[int]
    headers: NotRequired[list[tuple[bytes, bytes]]]
    body: NotRequired[bytes]

class ReceiveEventType(TypedDict):
    type: str
    body: NotRequired[bytes]
    more_body: NotRequired[Literal[True, False]]

class PlaceholderMissingException(Exception):
    msg: str = "Path does not contain token placeholder {token_placeholder}"
    def __init__(self, token_placeholder: str):
        super().__init__(self.msg.format(token_placeholder=token_placeholder))
from enum import Enum


class UriScheme(str, Enum):
    http = "http"
    https = "https"
    add = "ADD"
    move = "MOVE"
    remove = "REMOVE"
    replace = "REPLACE"

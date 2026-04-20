from functools import partial

open_text = partial(open, "text.txt")
with open_text(mode="r") as f:
    pass


open_reader = partial(open, mode="r", encoding="utf-8")
with open_reader("text.txt") as f:
    pass


args = ("text.txt",)
kwargs = {"mode": "r", "encoding": "utf-8"}
open_custom = partial(open, *args, **kwargs)

with open_custom() as f:
    pass


def curried_open(file):
    def with_mode(mode="r"):
        def with_encoding(encoding="utf-8"):
            return open(file, mode=mode, encoding=encoding)

        return with_encoding

    return with_mode


with curried_open("text.txt")("r")("utf-8") as f:
    pass

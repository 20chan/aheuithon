import codecs, io, encodings
from aheuithon.codec.parser import parse

def aheui_decode(input, errors="strict"):
    raw = bytes(input).decode("utf-8")
    code = "\n".join(raw.splitlines())
    code = parse(code)
    return code, len(input)

def search_function(encoding):
    if encoding != "aheui":
        return None
    utf8 = encodings.search_function("utf8")
    return codecs.CodecInfo(
        name="aheui",
        encode=utf8.encode,
        decode=aheui_decode,
    )

codecs.register(search_function)
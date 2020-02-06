import parso
from aheuithon.codec.compiler import compile

def ffc(typ, node):
    for x in node.children:
        if x.type == typ:
            return x

def find_decorated_nodes(mod):
    decorated = []
    q = [mod]
    while q:
        n = q.pop()
        if not hasattr(n, "children"):
            continue
        found = False
        for x in n.children:
            if not found and x.type == "decorator":
                name = ffc("name", x).value
                if name == "aheui":
                    found = True
                    continue
            elif found and x.type == "funcdef":
                decorated.insert(0, x)
            if hasattr(x, "children"):
                q.append(x)
    return decorated

def parse(src):
    lines = src.splitlines()
    mod = parso.parse(src)
    aheuifuncs = find_decorated_nodes(mod)
    offset = 0
    for func in aheuifuncs:
        start = func.start_pos[0] + offset
        end = func.end_pos[0] + offset
        prefix = func.start_pos[1] + 4
        body = [l[prefix:] for l in lines[start:end]]
        newBody = [' ' * prefix + l for l in compile(body)]
        print(body)
        print(newBody)
        offset += len(newBody) - len(body)
        lines[start:end] = newBody
    return "\n".join(lines)

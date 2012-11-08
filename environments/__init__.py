


def load_environment(name):
    if name not in ALL:
        raise Exception("%s not found" % name)

def to_dict(stored_env):
    for i, row in enumerate(stored_env):
        for j, cell in enumerate(row):
            yield ((i,j), cell)

def solve(s):
    names = s.split()
    new = []
    for name in names:
        name = name[0].upper() + name[1:]
        new.append(name)
    new_name = new[0] + ' ' + new[1]
    return new_name




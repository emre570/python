def mutate_string(string, position, character):
    position = int(i)
    l = list(s)
    character = c
    l[position] = f'{character}'
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
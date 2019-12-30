import sys
def main():
    to_parse = sys.argv[1] 
    bracktes = []
    for w in to_parse:
        if w in ['[', '{', '(']:
            bracktes.append(w)
        elif w == ']':
            if bracktes[-1] != '[':
                sys.exit(-1)
            else:
                _ = bracktes.pop()
        elif w == '}':
            if bracktes[-1] != '{':
                sys.exit(-1)
            else:
                _ = bracktes.pop()
        elif w == ')':
            if bracktes[-1] != '(':
                sys.exit(-1)
            else:
                _ = bracktes.pop()
    if bracktes:
        sys.exit(1)
    sys.exit(0)

if __name__ == '__main__':
    main()
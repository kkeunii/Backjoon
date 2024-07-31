def generate_sequences(n, m, start, sequence):
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return

    for i in range(start, n + 1):
        generate_sequences(n, m, i, sequence + [i])

n, m = map(int, input().split())
generate_sequences(n, m, 1, [])
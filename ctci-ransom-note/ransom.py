from collections import defaultdict


def ransom_note(magazine, ransom):
    available_words = defaultdict(int)
    for word in magazine:
        available_words[word] += 1

    for word in ransom:
        if word not in available_words:
            return False
        if available_words[word] == 0:
            return False
        available_words[word] -= 1

    return True


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")

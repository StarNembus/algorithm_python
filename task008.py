# Задание 1
import hashlib


def alg(len_str):
    sum_substring = set()

    for i in range(len(len_str)):
        for j in range(len(len_str), i, -1):
            hash_str = hashlib.sha1(len_str[i:j].encode('utf-8')).hexdigest()
            sum_substring.add(hash_str)
    print(sum_substring)
    return len(sum_substring)


len_str = input('Введите строку, состоящую только из маленьких латинских букв: ')
print(alg(len_str))


# Задание 2
import heapq
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_code(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input()
    code = huffman_code(s)
    str_encoded = " ".join(code[c] for c in s)
    print(len(code), len(str_encoded))
    for c in sorted(code):
        print("{}:{}".format(c, code[c]))
        print(str_encoded)


if __name__ == "__main__":
    main()

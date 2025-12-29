import heapq
from collections import Counter

def huffman_compress(data):
    # Menghitung frekuensi karakter
    freq = Counter(data)
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    
    # Membangun pohon Huffman
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    # Hasil koding
    huff_dict = dict(heapq.heappop(heap)[1:])
    compressed = "".join([huff_dict[char] for char in data])
    return compressed, huff_dict

print("Algoritma Huffman Siap")

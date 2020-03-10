import heapq

# def solution(numToys, topToys, toys, numQuotes, quotes):
#     freq = {}
#     for toy in toys:
#         freq[toy] = 0
#     for quote in quotes:
#         words = quote.lower().split(" ")
#         for word in words:
#             if not word in freq:
#                 continue
#             freq[word] += 1
#     heap = [(-value, key) for key, value in freq.items()]
#     heapq.heapify(heap)
#     return [heapq.heappop(heap)[1] for _ in range(topToys)]

def solution(numToys, topToys, toys, numQuotes, quotes):
    freq = {}
    for toy in toys:
        freq[toy] = [0, 0]
    for quote in quotes:
        usedWord = {} # denote if the toy name has been seen
        words = quote.lower().split(" ")
        for word in words:
            if not word in freq:
                continue
            freq[word][0] += 1
            if not word in usedWord:
                freq[word][1] += 1
            usedWord[word] = 1

    heap = [(-value[0], -value[1], key) for key, value in freq.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(topToys)]


if __name__ == "__main__":
    numToys = 6
    topToys = 2
    toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
    numQuotes = 6
    quotes = [
        "Elmo is the hottest of the season! Elmo Elmo will be on every kid's wishlist!",
        "The new  dolls are super high quality",
        "Expect the Elsa dolls to be very popular this year, Elsa!",
        "Elsa and  are the toys I'll be buying for my kids, Elsa is good",
        "For parents of older kids,  look into buying them a drone",
        "Warcraft is slowly rising in popularity ahead of the holiday season"
    ]
    a = solution(numToys, topToys, toys, numQuotes, quotes)
    print(a)
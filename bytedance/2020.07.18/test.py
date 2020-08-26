def knn_classifier(test, targets, labels, k):
    distances = []

    for v in targets:
        distances.append(sum((i - j) * 2 for i, j in zip(v, test)) * 0.5)

    topk = sorted(enumerate(distances), key=lambda x: x[1], reverse=False)[:k]
    label_count = []

    for i, _ in topk:
        label_count[labels[i]] = label_count.get(labels[i], -1) + 1

    sor
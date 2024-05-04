class PlagiarismChecker:
    def __init__(self):
        pass

    def plagiarism_percentage(self, text1, text2):
        sentences1 = text1.split("\n")
        sentences2 = text2.split("\n")
        count = 0
        for x in sentences1:
            for y in sentences2:
                if x == y:
                    if x != "":
                        count = count + len(x)
                        break
        similarity = count * 100 / (len(text1) - len(sentences1))
        return int(self.limit(similarity))

    def duplicate_sentences(self, text1, text2):
        sentences1 = text1.split("\n")
        sentences2 = text2.split("\n")
        duplicates = []
        for x in sentences1:
            x = x.strip()
        for x in sentences2:
            x = x.strip()
        for x in sentences1:
            for y in sentences2:
                if x == y:
                    duplicates.append(x)
                    break
        return duplicates

    def limit(self, k):
        if k > 100:
            return 100
        else:
            return k

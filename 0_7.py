sentence = input()
sentence_mod = sentence.replace("r ", "rr ")
sentence_mod = sentence_mod.replace("R ", "RR ")
if sentence_mod[-1] == "r " or sentence_mod[-1] == "R ":
    sentence_mod = sentence_mod + sentence_mod[-1]
print(sentence_mod)
#!/usr/bin/python3
import json
import shutil

with open("emojilib/emojis.json") as f:
    emojis = json.load(f)

mapping = {word: emoji['char'] for name, emoji in emojis.items() for word in emoji['keywords'] + [name] if emoji['char'] is not None}

shutil.copyfile("template.txt", "table.txt")

with open("table.txt", 'a') as f:
    f.write("BEGIN_TABLE\n")

    for word, emoji in mapping.items():
        f.write("{}\t{}\t1\n".format(word.replace(' ', '_'), emoji))

    f.write("END_TABLE\n")


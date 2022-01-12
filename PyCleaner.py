from string import digits

delete_list = ["[{'id': ", ", 'name': '", "'}", "{'id': ", "'}]", "]", "["]
with open("in.csv", 'r', encoding="utf-8") as fin, open("cleaned.csv", "w+", encoding="utf-8") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "")
            remove_digits = str.maketrans('', '', digits)
            line = line.translate(remove_digits)
        fout.write(line)
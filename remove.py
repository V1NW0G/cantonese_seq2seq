with open("data/yue.txt", "r", encoding="utf-8") as input_file:
    with open("eng_yue.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            line = line.split("\t")[0] + "\n"
            output_file.write(line)
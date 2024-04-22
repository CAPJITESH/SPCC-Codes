def main():
    prod_rules = []
    final_rules = []

    with open("/Users/jiteshgogia/Desktop/Books/SPCC/Codes/input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        s1 = line.strip()
        print(s1)
        if s1[3:] not in prod_rules:
            prod_rules.append(s1[3:])
            final_rules.append(s1)

    print("printing all production rules")
    for count, rule in enumerate(final_rules):
        print(f"t{count + 1}",rule[2:])

main()
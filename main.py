from drug import Drug


def main():
    first_drug = Drug('essentiale')
    second_drug = Drug('Karvalol', 'Use before eating', 30, 'transparent', 4, 10)
    third_drug = Drug('Anaferon', 'Use after eating', 15, 'some active subtance', 8, 20)
    drugs = [first_drug, second_drug, third_drug]
    for drug in drugs:
        print(drug)


if __name__ == '__main__':
    main()

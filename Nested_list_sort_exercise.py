if __name__ == '__main__':
    records = [['Achah', 12], ['bobo', 27], ['Mbah', 29], ['Tewan', 27]]

    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     student = [name, score]
    #     records.append(student)

    sorted_records = sorted(records, key=lambda x: (x[1], x[0]))

    second_lowest = sorted(set([record[1] for record in records]))[1]

    names = [sLowScore[0] for sLowScore in sorted_records if sLowScore[1] == second_lowest]

    for name in names:
        print(name)


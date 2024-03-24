def sort_scores(students):
    scores = sorted(set(score for name, score in students))
    second_lowest_score = scores[1]
    second_lowest_names = sorted(name for name, score in students if score == second_lowest_score)

    return second_lowest_names


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest_names = sort_scores(students)
    for name in second_lowest_names:
        print(name)

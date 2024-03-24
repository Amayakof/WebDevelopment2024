# Finding the percentage

def average_marks(query_marks):
    return sum(query_marks) / len(query_marks)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_marks = student_marks[query_name]

    print("{:.2f}".format(average_marks(query_marks)))

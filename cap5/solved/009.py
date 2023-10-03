approved_students = 0
onexame_students = 0
disapproved_students = 0
class_average = 0

for student in range(0,5):
    n1, n2 = map(float, input("Digite duas notas: ").split())
    average = (n1 + n2) / 2

    class_average += average

    if average <= 3:
        print("Reprovado")
        disapproved_students += 1
    elif 3 < average <= 7:
        print("Exame")
        onexame_students += 1
    else:
        print("Aprovado")
        approved_students += 1

print()
print(f"Total de alunos aprovados: {approved_students}")
print(f"Total de alunos reprovados: {disapproved_students}")
print(f"Total de alunos em exame: {onexame_students}")
print(f"Média da classe: {class_average / 5:.2f}")
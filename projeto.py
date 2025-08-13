import json

def calcular_media(aluno):
    
    notas = [
        aluno.get('nota_1', 0) or 0,
        aluno.get('nota_2', 0) or 0,
        aluno.get('nota_3', 0) or 0,
        aluno.get('nota_4', 0) or 0
    ]
    return sum(notas) / len(notas) 


with open('alunos.json', 'r', encoding='utf-8') as f:
    alunos = json.load(f)


aprovados = []
reprovados = []

for aluno in alunos:
    aluno['media'] = calcular_media(aluno)
    
    
    if aluno['media'] >= 7.0 and aluno['faltas'] < 7:
        aluno['status'] = 'Aprovado'
        aprovados.append(aluno)

    else:
        aluno['status'] = 'Reprovado'
        if aluno['media'] < 7.0 and aluno['faltas'] >= 7:
            aluno['motivo'] = 'Média baixa e faltas excessivas'

        elif aluno['media'] < 7.0:
            aluno['motivo'] = 'Média baixa'
            
        else:
            aluno['motivo'] = 'Faltas excessivas'
        reprovados.append(aluno)



print("=== APROVADOS ===")
for a in aprovados:
    print(f"{a['primeiro_nome']} {a['ultimo_nome']} - Média: {a['media']:.2f} - Faltas: {a['faltas']}")


print("\n=== REPROVADOS ===")
for a in reprovados:
    print(f"{a['primeiro_nome']} {a['ultimo_nome']} - Média: {a['media']:.2f} - Faltas: {a['faltas']} - Motivo: {a['motivo']}")

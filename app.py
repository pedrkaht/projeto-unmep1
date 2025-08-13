from flask import Flask, render_template, request
import json

app = Flask(__name__)



def calcular_media(aluno):
    notas = [
        aluno.get('nota_1', 0) or 0,
        aluno.get('nota_2', 0) or 0,
        aluno.get('nota_3', 0) or 0,
        aluno.get('nota_4', 0) or 0
    ]
    return sum(notas) / len(notas)


def carregar_alunos():
    with open('alunos.json', 'r', encoding='utf-8') as f:
        alunos = json.load(f)

    for aluno in alunos:
        aluno['media'] = calcular_media(aluno)
        if aluno['media'] >= 7.0 and aluno['faltas'] < 7:
            aluno['status'] = 'Aprovado'
            aluno['motivo'] = ''
        else:
            aluno['status'] = 'Reprovado'
            if aluno['media'] < 7.0 and aluno['faltas'] >= 7:
                aluno['motivo'] = 'Média baixa e faltas excessivas'
            elif aluno['media'] < 7.0:
                aluno['motivo'] = 'Média baixa'
            else:
                aluno['motivo'] = 'Faltas excessivas'
    return alunos


@app.route("/", methods=["GET"])
def lista_alunos():
    alunos = carregar_alunos()
    busca = request.args.get("busca", "").strip().lower()
    
    if busca:
        alunos = [
        a for a in alunos 
        if busca in f"{a['primeiro_nome']} {a['ultimo_nome']}".lower()
    ]
    
    return render_template("index.html", alunos=alunos, busca=busca)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

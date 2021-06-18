import csv
fieldnames = ["name", "surname", "email", "phone_number", "department", "position"]
with open ('RelatorioRejeitados2.csv', mode = 'w', newline= '', encoding= 'utf-8') as csv_rejeitados:
    rejeitados = csv.DictWriter(csv_rejeitados, fieldnames=fieldnames)

    rejeitados.writeheader()

    with open ('RelatorioAprovados1.csv', mode = 'w', newline= '', encoding= 'utf-8') as csv_aprovados:
      aprovados = csv.DictWriter(csv_aprovados, fieldnames=fieldnames)

      aprovados.writeheader()

      def validaCampos(name,surname, email,department) :
          tiposErros = ['', 'N/A', '-', 'Não consta']
          if name in tiposErros  or surname in tiposErros or email in tiposErros or department in tiposErros:
            rejeitados.writerow({"name": name, "surname": surname, "email": email, "phone_number": phone_number, "department" : department, "position" : position})
          else:
              aprovados.writerow({"name": name, "surname": surname, "email": email, "phone_number": phone_number, "department" : department, "position" : position})

      with open('/content/Cópia de Desafio CSV - Base de colaboradores.csv', encoding='utf-8') as analise_csv:

        tabela = csv.reader(analise_csv, delimiter=';')

      
        next(tabela)

        for linha in tabela:
          name = linha [0]
          surname = linha [1]
          email = linha [2]
          phone_number = linha [3]
          department = linha [4]
          position = linha [5]
          validaCampos(name, surname, email, department)
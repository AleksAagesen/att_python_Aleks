customers=['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salary =[155000, 755000, 455000, 1255000, 635000, 575000]
taxes =[55800, 317100, 182000, 451800, 171450, 71400]

for idx, x in enumerate(customers):
    if salary[idx] >555000 and (taxes[idx]/salary[idx]*100) >30:
        print(x)


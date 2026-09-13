import numpy as np

gene = "TP53"
expression = 12.5

genes = ["TP53", "BRCA1", "EGFR", "MYC", "KRAS"]
print(genes[0])
print(genes[-1])
print(len(genes))
genes.append("PTEN")
print(genes)

expression = {
"TP53": 12.5,
"BRCA1": 8.3,
"EGFR": 15.2,
"MYC": 20.1,
"KRAS": 5.6
}

print(expression["TP53"])
print(expression.keys())
print(expression.values())

value = 12.5
if value > 10:
    print("High expression")
elif value > 5:
    print("Moderate expression")
else:
    print("Low expression") 

for gene in genes:
    print(gene)

for gene, expr in expression.items():
    print(gene, expr)

high_expression_genes = [
    gene 
    for gene, expr in expression.items() 
    if expr > 10
    ]
print(high_expression_genes)

def square(x):
    return x ** 2

squared_expression = {gene: square(expr) for gene, expr in expression.items()}
print(squared_expression)
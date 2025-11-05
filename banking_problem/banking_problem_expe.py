from jinja2 import Template

tenplate_content = open('./banking_problem.py.jinja').read()
template = Template(tenplate_content)

prec_list = [2,10,20,50,100]
annees_list = [10,50,60,75]

factors_comb = [{"prec":prec,"annees":annes} for prec in prec_list for annes in annees_list]
print(factors_comb)

for factor in factors_comb:
    print(f"Running test with parameters: {factor}")
    generated_code = template.render(factor)
    exec(generated_code)
    print("\n")
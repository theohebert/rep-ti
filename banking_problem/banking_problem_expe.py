from jinja2 import Template
import pandas as pd

tenplate_content = open('./banking_problem.py.jinja').read()
template = Template(tenplate_content)

prec_list = [2,10,20,50,100]
annees_list = [10,50,60,75]

factors_comb = [{"prec":prec,"annees":annes} for prec in prec_list for annes in annees_list]

result = pd.DataFrame()

for factor in factors_comb:
    print(f"Running test with parameters: {factor} \n")
    generated_code = template.render(factor)
    local_vars = {}
    exec(generated_code, {"__name__": "__main__"}, local_vars)
    if "res" in local_vars:
        res = local_vars["res"]
        result = pd.concat([result,pd.DataFrame({"monnaie":[res["monnaie"]],"nombreAnnees":[res["nombreAnnees"]],"prec":[res["prec"]]})])
    else:
        print("aiie")

result.to_csv("results_banking_problem.csv", index=False)

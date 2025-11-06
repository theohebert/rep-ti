from jinja2 import Template

tenplate_content = open('property_template.py.jinja').read()
template = Template(tenplate_content)

factors_comb = [
    {"op1": "(x + y) + z", "op2": "x + (y + z)", "repetition": 10000, "seed": 0, "a": 0, "b": 1},
    {"op1": "(x + y) + z", "op2": "x + (y + z)", "repetition": 10000, "seed": 0, "a": 1, "b": 2},
    {"op1": "(x + y) + z", "op2": "x + (y + z)", "repetition": 100000, "seed": 0, "a": 0, "b": 1},
    {"op1": "(x + y) + z", "op2": "x + (y + z)", "repetition": 100000, "seed": 0, "a": 1, "b": 2},
]

for factor in factors_comb:
    generated_code = template.render(factor)
    exec(generated_code)
    print("\n")

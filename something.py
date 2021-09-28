import json
import email
from jinja2 import Environment, FileSystemLoader

with open("data.json", "r") as f:
    data = json.load(f)

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

rendered = env.get_template("e-template.html").render(data=data)


f_name = "email_result.html"
with open(f"./site/{f_name}", "w") as f:
    f.write(rendered)
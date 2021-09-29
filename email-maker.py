import json
import pandas as pd
from jinja2 import Environment, FileSystemLoader

def email_maker(path):
    data = pd.read_csv(path, sep=",")

    with open("data.json", "w") as f:
        f.write(data.to_json(orient='records'))

    with open("data.json", "r") as f:
        data = json.load(f)

    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    rendered = env.get_template("e-template.html").render(data=data)

    f_name = "rendered_email.html"
    with open(f"./site/{f_name}", "w") as f:
        f.write(rendered)

if __name__ == "__main__":
    email_maker('data/09172021_complete_data.csv')
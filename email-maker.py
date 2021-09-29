import json
import pandas as pd
from jinja2 import Environment, FileSystemLoader


def email_maker(path):
    data = pd.read_csv(path, sep=",")

    # makes json file from csv
    with open("data.json", "w") as f:
        f.write(data.to_json(orient='records'))

    # loads json file
    with open("data.json", "r") as f:
        data = json.load(f)

    # give the name of the folder where the template files are located
    file_loader = FileSystemLoader("templates")
    env = Environment(loader=file_loader)

    # select the template file
    rendered = env.get_template("e-template.html").render(data=data)

    # write the rendered template to a file
    f_name = "rendered_email.html"
    with open(f"./site/{f_name}", "w") as f:
        f.write(rendered)


if __name__ == "__main__":
    # add the path to the CSV file as argument
    email_maker('data/09172021_complete_data.csv')
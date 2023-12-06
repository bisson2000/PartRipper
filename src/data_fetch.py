import json
import sys
import pandas as pd

sys.path.append('../')


def import_all():
    with open("data/internal/all_cpus.json", "r") as source_file:
        data = json.load(source_file)

        print(data)


def import_cpu() -> dict:
    with open("data/internal/all_cpus.json", "r") as source_file:
        return json.load(source_file)



if __name__ == "__main__":
    import_all()
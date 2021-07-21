import csv


def load_csv(path="donnees/DE_Risque Climatique_Cartographie des données v1.04 - Sourcing data.csv"):
    ESG_data = {}
    with open(path, "r") as csv_file:
        data = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(data):
            if i == 1:
                keys = row
            if i > 1:
                ESG_data.update({i : {keys[k]: row[k] for k in range(len(keys))}})
    return ESG_data

def get_all_risks(path="donnees/DE_Risque Climatique_Cartographie des données v1.04 - Sourcing data.csv"):
    risks = []
    with open(path, "r") as csv_file:
        data = csv.reader(csv_file, delimiter=",")
        for i, row in enumerate(data):
            if i > 1:
                risks += [row[25]]
    return [risk for risk in set(dict.fromkeys(risks)) if risk != ""]

def search(data, query):
    keys = list(data[2].keys())
    results = []
    for key in list(data.keys()):
        if data[key][keys[25]] in query:
            results += [key]
    return results

if __name__ == "__main__":
    get_all_risks()

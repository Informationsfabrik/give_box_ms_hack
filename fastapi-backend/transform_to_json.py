from ast import Str
from trace import Trace
import pandas as pd
import json
from typing import Dict

MAPPING:Dict[Str, Str] = {
        "Bezeichnung": "description",
        "Adresse (ungefähr)": "address_id",
        "Latitude": "latitude",
        "Longitude": "longitude",
        "Öffnungszeiten": "opening_hours",
        "Infos im Internet": "extern_link",
        "Vor Ort bestätigt am": "last_confirmation_date"
}

def transform_to_json(file_name):
    data_frame = pd.read_csv(f"./fastapi-backend/data/{file_name}", sep=";")

    data_frame.rename(columns=MAPPING, inplace=True)
    data_frame.drop(columns=["Typ"], inplace=True)

    data_frame["street"] = "ToDo"
    data_frame["house_number"] = data_frame["address_id"].str.extract(r'(\d{2})', expand=True)
    data_frame["city"] = "ToDo"
    data_frame["zip_code"] = data_frame["address_id"].str.extract(r'(\d{5})', expand=True)
    data_frame["image_id"] = [image_id for image_id in range(data_frame.shape[0])]
    data_frame["content"] = [{"books": True} for _ in range(data_frame.shape[0])]
    data_frame["is_temporary"] = [False for _ in range(data_frame.shape[0])]
    data_frame["maintenance_needed"] = [False for _ in range(data_frame.shape[0])]
    data_frame["maintainer_info"] = ["" for _ in range(data_frame.shape[0])]

    json_data = json.loads(data_frame.to_json(orient="records"))
    json.dump(json_data, open("test.json","w"), indent=4)


if __name__=="__main__":
    transform_to_json("giveboxen-standorte-muenster_0.csv")

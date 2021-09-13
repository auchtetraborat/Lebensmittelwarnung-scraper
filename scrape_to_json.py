from lebensmittelwarnung import Lebensmittelwarnung
import json
from datetime import datetime

type = "alle"
region = "alle_bundeslaender"

data = Lebensmittelwarnung().get(type, region)

ts = datetime.now()
tss = dt_string = ts.strftime("%d-%m-%Y %H-%M-%S")
with open("output/" + tss + ".json", "w") as f:
    f.write(json.dumps(data))

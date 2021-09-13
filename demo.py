from lebensmittelwarnung import Lebensmittelwarnung

type = "alle"
region = "alle_bundeslaender"

data = Lebensmittelwarnung().get(type, region)
print(data)

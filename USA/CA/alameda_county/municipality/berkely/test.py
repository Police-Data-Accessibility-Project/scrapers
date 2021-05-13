import requests
import mimetypes

response = requests.get(
    "https://data.cityofberkeley.info/api/views/ysvs-bcge/files/d446295a-fe8f-4574-b22f-a8b4d097c977?download=true&filename=Action_Taken.xlsx"
)
content_type = response.headers["content-type"]

extension = mimetypes.guess_extension(content_type)
print(content_type)
print(extension)

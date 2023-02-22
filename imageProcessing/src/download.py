import requests

URL = "https://drive.google.com/u/0/uc?id=1p91KBj-oUmuMfG2Gc33tEN5Js5HpV8YH&export=download&confirm=t&uuid=49f917b9-c7eb-4e8b-a2ad-8591b5d4672e&at=ALgDtsxrUQA_3i_DoDAv89JhmccE:1675665744117"
response = requests.get(URL)
print(response)
open("test.pt", "wb").write(response.content)

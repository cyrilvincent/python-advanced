import geometry
import pickle
import json

r = geometry.Rectangle(3, 2, geometry.Point(0,0))

with open("data/rectangle.pkl", "wb") as f:
    pickle.dump(r, f)

r = None

with open("data/rectangle.pkl", "rb") as f:
    r = pickle.load(f)
    print(r.area())

with open("data/rectangle.json", "w") as f:
    json.dump({"length": r.length, "width": r.width}, f)
    # json.dump(r.__dict__, f)

with open("data/book.json", "r") as f:
    content = json.load(f)
    print(content["title"])
    print(content["plugins"][0])
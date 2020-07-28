import random, os
def cat_pic():
    path = r"/Users/videet/Desktop/Water Bot/cats"
    cat = random.choice([
    x for x in os.listdir(path)
    if os.path.isfile(os.path.join(path, x))
    ])
    cat_path = "cats/" + cat
    return cat_path

if __name__ == "__main__":
    cat_pic()


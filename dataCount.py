import json

print("Data counts for train set: {}".format(len(json.load(open("./assignment2_release/training.json")))))
print("Data counts for validation set: {}".format(len(json.load(open("./assignment2_release/validation.json")))))
print("Data counts for test set: {}".format(len(json.load(open("./assignment2_release/test.json")))))
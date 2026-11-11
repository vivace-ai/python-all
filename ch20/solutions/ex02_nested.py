import json

text = """
{
  "course": "파이썬 기초",
  "students": [
    {"name": "이서연", "scores": [92, 88, 95]},
    {"name": "박준호", "scores": [78, 85, 80]}
  ]
}
"""

data = json.loads(text)
print(data["course"])
for student in data["students"]:
    scores = student["scores"]
    print(student["name"], f"{sum(scores) / len(scores):.1f}")

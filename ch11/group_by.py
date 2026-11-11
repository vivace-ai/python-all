staff = [("이서연", "마케팅"), ("박준호", "개발"), ("최민지", "개발"),
         ("정도윤", "마케팅"), ("한하은", "디자인")]

teams = {}
for name, team in staff:
    if team not in teams:
        teams[team] = []    # 처음 보는 팀이면 빈 리스트를 만든다
    teams[team].append(name)

for team, names in teams.items():
    print(f"{team}: {names}")

# cook your dish here
# cook your dish here
n = int(input())
player1_score = 0
Player2_score = 0
lead = 0
for i in range(n):
    score1, score2 = map(int, input().split())
    player1_score = player1_score + score1
    Player2_score = Player2_score + score2
    diff = player1_score - Player2_score

    if diff > 0 and diff > lead:
        lead = diff
        leader = 1
    elif diff < 0 and abs(diff) > lead:
        lead = abs(diff)
        leader = 2
print(leader,lead)
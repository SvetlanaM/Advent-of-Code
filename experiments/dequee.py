import collections

double_ended = collections.deque(["Mon", "Tue", "Wed"])
double_ended.append("Thu")
double_ended.appendleft("A")
print(double_ended)
double_ended.pop()
print(double_ended)
double_ended.popleft()
print(double_ended)
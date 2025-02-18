from collections import deque


links = deque([int(l) for l in input().split()])    # FIFO
articles = [int(a) for a in input().split()]        # LIFO
target_value = int(input())
final_feed = []

while links and articles:
    link = links.popleft()   
    article = articles.pop()   
    if article > link:
        remainder = article % link
        final_feed.append(int(remainder))
        double_remainder = remainder * 2
        if double_remainder != 0:
            articles.append(double_remainder)
    elif link > article:
        remainder = link % article
        final_feed.append(-remainder)
        double_remainder = remainder * 2
        if double_remainder != 0:
            links.append(double_remainder)
    else:
        final_feed.append(0)


total_engagement_value = sum(final_feed)
shortfall = target_value - total_engagement_value
print(f"Final Feed: {', '.join(str(i) for i in final_feed)}")
# print(f"Final Feed: {', '.join(list(map(str, final_feed)))}")

if total_engagement_value >= target_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {shortfall}")
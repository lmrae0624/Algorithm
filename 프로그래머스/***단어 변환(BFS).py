def solution(begin, target, words):
    from collections import deque

    visited=[False]*len(words)

    def check(begin,target):
        count=0
        for i in range(len(begin)):
            if begin[i]!=target[i]:
                count+=1
        return count

    def BFS(now,target,words):
        queue=deque([(now,0)])

        while queue:
            now, count=queue.popleft()
            if now==target:
                return count
  
            for word in range(len(words)):
                if visited[word]==False and check(now,words[word])==1:
                    visited[word]=True
                    queue.append((words[word],count+1))
        return 0

    return BFS(begin,target,words)


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
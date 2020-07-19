'''

Consider a vector of employees with a name and their title:
[<John, Manager>, <Sally, CTO>, <Sam, CEO>, <Drax, Engineer>, <Bob, CFO>, <Daniel, Engineer>]

And a dictionary where the keys report to the values:
{[CTO, CEO], [Manager, CTO], [Engineer, Manager], [CFO, CEO]}

Re-order the vector of employees according to the dictionary mappings. The vector of employees can be extremely big, 
however the dictionary only contains the title orderings.

Sample output:
[<Drax, Engineer>, <Daniel, Engineer>, <John, Manager>, <Sally, CTO>, <Bob, CFO>, <Sam, CEO>]

Note that in this case, CTO and CFO both report to CEO so they are both before CEO and above the next biggest thing, 
which is manager. They can also be in either order in this case.

'''
import collections
def reorderArray(employees, order):

    graph = collections.defaultdict(list)
    indegree = collections.Counter()
    output=[]
    for job,boss in order:
        graph[boss].append(job)
        indegree[job]+=1


    start=[k for k in graph if indegree[k]==0]

    q=collections.deque(start)
    output=[]

    d = collections.defaultdict(list)
    for name, rank in employees:
        d[rank].append(name)

    while q:
        currBoss=q.popleft()
        output+=[(x,currBoss) for x in d[currBoss]]
        for emps in graph[currBoss]:
            indegree[emps]-=1
            if indegree[emps]==0:
                q.append(emps)

    return(output[::-1])



employees=[('John', 'Manager'), ('Sally', 'CTO'), ('Sam', 'CEO'), ('Drax', 'Engineer'), ('Bob', 'CFO'), ('Daniel', 'Engineer')]
order=[['CTO', 'CEO'], ['Manager', 'CTO'], ['Engineer', 'Manager'], ['CFO', 'CEO']]
print(reorderArray(employees, order))
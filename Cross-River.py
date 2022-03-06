def Solver(): #combine all the function and return the result
    global S,E,W
    S = genStates()
    E = genEastGraph(S)
    W = genWestGraph(S)
    s = "EEEEEE"
    d = "WWWWWW"
    result = genShortestPath(W,s,d,"W",1)
    #print(result)
    #print(E)
    #print(W)
    printpath(result)
    
def genStates(): #list out all the state in this problem
    direction = ("E","W")
    states = []
    for a in direction:
        for b in direction:
            for c in direction:
                for d in direction:
                    for e in direction:
                        for f in direction:
                            state = a + b + c + d + e + f
                            states.append(state)
    return tuple(states)

def isLegal(a): #check whether the states are possible or not
    if ((a[0] != a[1] and (a[1] == a[2] or a[1] == a[4])) or (a[2] != a[3] and (a[0] == a[3] or a[4] == a[3])) or (a[4] != a[5] and (a[0] == a[5] or a[2] == a[5]))):
        return False
    else:
        return True

def EastnextStates(startnode,allstates): #when the boat is on the east side, find out what is the possible next steps for all states
    possible=[startnode]         
    c1 = startnode.count("W")
    for i in range(len(allstates)):
        if allstates[i].count("W") - c1 == 2 and startnode != allstates[i]:
            c = 0
            for j in range(6):
                if allstates[i][j] == startnode[j]:
                    c += 1
            if c >= 4:
                possible.append(allstates[i])
    return possible

def WestnextStates(startnode,allstates): #when the boat is on the west side, find out what is the possible next steps for all states
    possible=[startnode]        
    c1 = startnode.count("E")
    for i in range(len(allstates)):
        if (allstates[i].count("E") - c1 == 1 or allstates[i].count("E") - c1 == 2) and startnode != allstates[i]:
            c = 0
            for j in range(6):
                if allstates[i][j] == startnode[j]:
                    c += 1
            if c >= 4:
                possible.append(allstates[i])
    return possible


def genEastGraph(S): #according to EastnextStates, put all the states and the linkers in to the dictionary
    G = []
    East={}
    for i in range(len(S)):
        if isLegal(S[i]) == True:
            G.append(S[i])
            
    for i in range(len(G)):
        result1 = EastnextStates(G[i],G)
        East.update({G[i]:result1[1:]})
    #print(East)
    return East

def genWestGraph(S): #according to WestnextStates, put all the states and the linkers in to the dictionary
    G = []
    West={}
    for i in range(len(S)):
        if isLegal(S[i]) == True:
            G.append(S[i])
    for i in range(len(G)):
        result1 = WestnextStates(G[i],G)
        West.update({G[i]:result1[1:]})
    #print(West)
    return West

def genShortestPath(graph, start, end, boat,step, path=[]): #use the graph(East and West) to find the path to reach the end point
    global S,E,W,shortest
    graph = E if boat == "W" else W #according to the boat side to use different dictionary
    boat = "E" if boat == "W" else "W" #consider which side is the boat
    #print(step, start, boat)
    path = path + [start]
    if start == end:
        shortest = step
        return path
    elif not (start in graph):
        return None
    elif(not shortest or step < shortest): # if the step is more than the before one it will stop and try another way, to reduce the use of time
        nextstep = None
        for node in graph[start]:
            if node not in path:
                nextstep = genShortestPath(graph,node,end,boat,step+1,path)
        return nextstep
                
def printpath(result): #turn the result back to words and show the result
    posit = 0
    for i in range(1,len(result)):
        people = []
        for r in range(6):
            if result[i-1][r] != result[i][r]:
                posit = r
                if result[i-1][r] == "E":
                    d1 = "east"
                    d2 = "west"
                else:
                    d1 = "west"
                    d2 = "east"
                if posit == 0:
                    who = "blue husband"
                if posit == 1:
                    who = "blue wife"
                if posit == 2:
                    who = "yellow husband"
                if posit == 3:
                    who = "yellow wife"
                if posit == 4:
                    who = "red husband"
                if posit == 5:
                    who = "red wife"
                people.append(who)
        if len(people) == 1:
            p1 = people[0] + " goes"
            print(str(i) + " The " + p1 + " from the " + d1 + " to the " + d2 + ".")
        else:
            p1 = people[0] + " and "
            p2 = people[1] + " go"
            print(str(i) + " The " + p1 + p2 + " from the " + d1 + " to the " + d2 + ".")
            
S = tuple()
E = dict()
W = dict()
shortest = False
Solver() 

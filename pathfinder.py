import queue

def box():
    puz = []
    puz.append(["-", "-", "-", "-", "-", "O", "-", "-", "-", "-"])
    puz.append(["|", " ", " ", " ", " ", " ", "-", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", " ", " ", " ", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", " ", " ", " ", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", " ", "-", " ", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", " ", " ", "-", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", " ", " ", " ", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", " ", " ", " ", " ", " ", "|"])
    puz.append(["|", " ", " ", " ", "-", " ", " ", " ", " ", "|"])
    puz.append(["|", "-", "-", "-", "-", "X", "-", "-", "-", "|"])
    return puz

def box1(puz1, pattern=""):
    for x, post in enumerate(puz1[0]):
        if post == "O":
            begin = x
    a = begin
    b = 0
    post = set()
    for shift in pattern:
        if shift == "L": a -= 1
        elif shift == "R": a += 1
        elif shift == "U": b -= 1
        elif shift == "D": b += 1
        post.add((b, a))
    for b, row in enumerate(puz1):
        for a, col in enumerate(row):
            if (b, a) in post:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()

def vld(puz1, addmove):
    for x, post in enumerate(puz1[0]):
        if post == "O":
            begin = x
    a = begin
    b = 0
    for shift in addmove:
        if shift == "L": a -= 1
        elif shift == "R": a += 1
        elif shift == "U": b -= 1
        elif shift == "D": b += 1
        if not (0 <= a < len(puz1[0]) and 0 <= b < len(puz1)):
            return False
        elif (puz1[b][a] == "-"):
            return False
    return True

def final(puz1, addmove):
    for x, post in enumerate(puz1[0]):
        if post == "O":
            begin = x
    a = begin
    b = 0
    for shift in addmove:
        if shift == "L": a -= 1
        elif shift == "R": a += 1
        elif shift == "U": b -= 1
        elif shift == "D": b += 1
    if puz1[b][a] == "X":
        print("Found: " + addmove)
        box1(puz1, addmove)
        return True
    return False

part = queue.Queue()
part.put("")
join = ""
puz1 = box()

while not final(puz1, join):
    join = part.get()
    for b in ["Left ", "Right ", "Up ", "Down "]:
        put = join + b
        if vld(puz1, put): part.put(put)


#Why did you choose this particular algorithm?
#ans: i choose this algorithm to get the shortest way of it, and i get to learn the Dijkstra’s Shortest Path algo of it

#What have you observed?
#ans: i observe that if we learn such a thing of this the dijkstra's shortest path it would be a lot of help, specially like global area/mapping then we use a calculation like Dijkstra’s Shortest Path
#and if we plan to make an AI we can use Dijkstra Shortest path of it, like something u want that AI to go a specific location, and can adjust the movements of AI on any obstacle it sees by using dijkstra's shortest path


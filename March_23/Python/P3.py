#Prison Break
"""
The basic idea here would be from each cell to check for all the paths in recursive manner.
We would also store the state of the current grid to get paths that are unique.
"""

def paths(adj,grid_size,cx,cy,num_paths,vis):
    #check whether the current cordinates are not out of bounds or negative
    if cx==grid_size or cy==grid_size or cx<0 or cy<0:
        return num_paths
    # check if the last point is not a motion sensor cell or the current cell does not have a motion sensor.
    if adj[grid_size-1][grid_size-1]==1 or adj[cx][cy]==1:
        return num_paths
    # if the last cell is reached increment the number of paths and return
    if cx==grid_size-1 and cy==grid_size-1:
        return num_paths+1
    if vis[cx][cy]==1:
    # if the cell has already been visited return
        return num_paths
    #make the current cell as visited
    vis[cx][cy]=1
    #check all the four comibantions.
    num_paths=paths(adj,grid_size,cx+1,cy,num_paths,vis)
    num_paths=paths(adj,grid_size,cx,cy+1,num_paths,vis)
    num_paths=paths(adj,grid_size,cx-1,cy,num_paths,vis)
    num_paths=paths(adj,grid_size,cx,cy-1,num_paths,vis)
    #again mark the current cell as univisited. This is done when the function returns to the 
    # calling function this cell would not have been visited there.
    vis[cx][cy]=0
    return num_paths

def get_paths():
    grid=int(input())
    adj=[]
    vis=[[0 for k in range(grid)] for d in range(grid)]
    for i in range(grid):
        temp=input()
        adj.append([int(x) for x in temp.split()])
    print(paths(adj,grid,0,0,0,vis))

def main():
    n=int(input())
    #print(n)
    for i in range(n):
        get_paths()

main()
def paths(adj,grid_size,cx,cy,num_paths,vis):
    if cx==grid_size or cy==grid_size or cx<0 or cy<0:
        return num_paths
    if adj[grid_size-1][grid_size-1]==1 or adj[cx][cy]==1:
        return num_paths
    if cx==grid_size-1 and cy==grid_size-1:
        return num_paths+1
    if vis[cx][cy]==1:
        return num_paths
    vis[cx][cy]=1
    num_paths=paths(adj,grid_size,cx+1,cy,num_paths,vis)
    num_paths=paths(adj,grid_size,cx,cy+1,num_paths,vis)
    num_paths=paths(adj,grid_size,cx-1,cy,num_paths,vis)
    num_paths=paths(adj,grid_size,cx,cy-1,num_paths,vis)
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
from collections import defaultdict
from typing import List
class Soultion:
    def criticalConnections(self, n, edges) -> List:
        graph = defaultdict(list)
        self.low_id = -1
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False]*n
        lowest_ids = [-1]*n
        self.res = []

        self.TarjansAlgo(graph, -1, 0, visited, lowest_ids)
        return self.res
    

    def TarjansAlgo(self, graph, parent_id, node_id, visited, lowest_ids):
        
        
        for n in graph[node_id]:
            if n != parent_id and not visited[n]:
                visited[n] = True
                lowest_ids[n] = self.low_id +1

                self.low_id+=1
                self.TarjansAlgo(graph, node_id, n, visited, lowest_ids)

                if lowest_ids[n] < lowest_ids[node_id]:
                    lowest_ids[node_id] = lowest_ids[n]
                else:
                    self.res.append([n, node_id])










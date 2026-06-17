"""单源最短路径 — Dijkstra 实现（适用于非负权图）

说明：
- 使用邻接表表示图，图类型为 Dict[顶点, List[(邻接顶点, 权重)]]。
- 算法返回两个字典：`dist`（源点到每个顶点的最短距离）和 `prev`（用于重建路径的前驱节点）。
- 时间复杂度：使用二叉堆的 Dijkstra 为 O((V+E) log V)。
"""

from typing import Dict, List, Tuple, Any
import heapq

Graph = Dict[Any, List[Tuple[Any, float]]]


def dijkstra(graph: Graph, source: Any) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
	# 初始化：将所有顶点距离设为无穷大，前驱设为 None
	# 注意文件中使用制表符进行缩进，以下保留制表符风格
	dist = {v: float('inf') for v in graph}
	prev = {v: None for v in graph}
	dist[source] = 0.0

	# 使用最小堆（距离, 顶点）来选择当前未处理的最短路径顶点
	heap: List[Tuple[float, Any]] = [(0.0, source)]

	while heap:
		d, u = heapq.heappop(heap)
		# 如果堆中弹出的距离大于当前记录，说明这是过期记录，跳过
		if d > dist[u]:
			continue
		# 遍历邻接边并尝试松弛（relax）操作
		for v, w in graph.get(u, []):
			nd = d + w  # 候选距离：source -> ... -> u -> v
			# 若通过 u 到 v 的距离更短，则更新 dist 和 prev，并把新距离压入堆
			if nd < dist.get(v, float('inf')):
				dist[v] = nd
				prev[v] = u
				heapq.heappush(heap, (nd, v))

	# 返回最终的距离表和前驱表，用于后续的路径重建
	return dist, prev


def reconstruct_path(prev: Dict[Any, Any], target: Any) -> List[Any]:
	"""根据前驱表 `prev` 重建从源点到 `target` 的路径。

	实现细节：从目标点向前按 prev 链回溯直到 None（源点的前驱），收集顶点并反转。
	返回值为顶点列表，若目标不可达则通常 dist[target] 为 inf（调用者可检查）。
	"""

	path: List[Any] = []
	u = target
	# 通过 prev 链回溯到源点，收集路径（当前为逆序）
	while u is not None:
		path.append(u)
		u = prev.get(u)
	path.reverse()
	return path


def example() -> None:
	# 示例图（无向图）：为了清晰起见，边在邻接表中对称列出
	graph: Graph = {
		'A': [('B', 5), ('C', 1)],
		'B': [('A', 5), ('C', 2), ('D', 1)],
		'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
		'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
		'E': [('C', 8), ('D', 3)],
		'F': [('D', 6)],
	}

	# 计算最短路径表和前驱表
	dist, prev = dijkstra(graph, 'A')
	print("从 A 到各点最短距离：")
	for v in sorted(dist):
		print(f"{v}: {dist[v]}")

	print("\n示例路径 A -> F：")
	path = reconstruct_path(prev, 'F')
	# 如果 F 不可达，dist['F'] 会是 inf；调用者可以先检查 dist
	print(" -> ".join(path))


if __name__ == '__main__':
	example()


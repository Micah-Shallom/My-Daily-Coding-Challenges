// In this implementation of a graph , i will do it functionally and with the use of methods so as to see the differences in both implementations and use it for further purposes

package algorithms

import "fmt"


//method based implementation
// ===============================
type Graph struct {
	adjacencyList map[string][]string
}

//creating an addedge method that adds edges to the graph
func(g *Graph) AddEdge (node1, node2 string) {
	g.adjacencyList[node1] = append(g.adjacencyList[node1], node2)
	g.adjacencyList[node2] = append(g.adjacencyList[node2], node1)
}

//printgraph
func(g *Graph) PrintGraph() {
	for node, neighbors := range g.adjacencyList{
		fmt.Printf("%s -> %v\n",node, neighbors)
	}
}

func main() {
	graph := Graph{
		adjacencyList: make(map[string][]string),
	}
	// Add edges to the graph
	graph.AddEdge("A", "B")
	graph.AddEdge("A", "C")
	graph.AddEdge("B", "D")
	graph.AddEdge("C", "E")
	graph.AddEdge("D", "E")
	graph.AddEdge("E", "F")

	// Print the graph
	graph.PrintGraph()
}


//Function based implementation
// ====================================================

type Graph struct{
	adjacencyList map[string][]string
}

func AddEdge(graph *Graph, node1, node2 string){
	graph.adjacencyList[node1] = append(graph.adjacencyList[node1], node2)
	graph.adjacencyList[node2] = append(graph.adjacencyList[node2], node1)
}

func PrintGraph(graph *Graph) {
	for node, neighbors := range graph.adjacencyList{
		fmt.Printf("%s -> %v\n", node, neighbors)
	}
}

func main(){
	graph := &Graph{
		adjacencyList: make(map[string][]string),
	}

	// Add edges to the graph
	AddEdge(graph, "A", "B")
	AddEdge(graph, "A", "C")
	AddEdge(graph, "B", "D")
	AddEdge(graph, "C", "E")
	AddEdge(graph, "D", "E")
	AddEdge(graph, "E", "F")

	// Print the graph
	PrintGraph(graph)
}
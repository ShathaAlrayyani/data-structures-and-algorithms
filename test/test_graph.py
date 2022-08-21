import pytest

from DS.Graph.graph import *


# An empty graph
def test_empty():
    graph = Graph()
    actual = graph.size()
    assert actual == 0


def test_instantiate():
    graph = Graph()
    assert graph


# Node can be successfully added to the graph
def test_add_node_and_size():
    graph = Graph()
    graph.add_node(10)
    graph.add_node(15)
    actual = 2
    expected = graph.size()

    assert actual == expected


# An edge can be successfully added to the graph
def test_add_edge():
    graph = Graph()



# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes(graph):
    result = []
    for i in graph.get_nodes():
        result.append(i.value)
    actual = result
    expected = ['A', 'B', 'E', 'C', 'D']
    assert actual == expected


# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_get_neighbors(graph):
    actual = graph.get_neighbors(graph.value)
    expected = ['B', 'C', 'D', 'E']

    assert actual == expected


# The proper size is returned, representing the number of nodes in the graph
def test_size(graph):
    actual = graph.size()
    expected = 5

    assert actual == expected


# A graph with only one node and edge can be properly returned-- HUH/Nani?!!




@pytest.fixture
def graph():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(b, a)
    g.add_edge(a, e)
    g.add_edge(e, a)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)

    return g


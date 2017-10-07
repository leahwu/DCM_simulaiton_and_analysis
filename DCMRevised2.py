import heapq
from itertools import combinations, permutations
import math
from operator import itemgetter
import random
import networkx as nx
from networkx.utils import random_weighted_sample

def directed_configuration_model_revised(in_degree_sequence,
                                 out_degree_sequence,
                                 create_using=None,seed=None):
    """Return a directed_random graph with the given degree sequences.

    The configuration model generates a random directed pseudograph
    (graph with parallel edges and self loops) by randomly assigning
    edges to match the given degree sequences.

    Parameters
    ----------
    in_degree_sequence :  list of integers
       Each list entry corresponds to the in-degree of a node.
    out_degree_sequence :  list of integers
       Each list entry corresponds to the out-degree of a node.
    create_using : graph, optional (default MultiDiGraph)
       Return graph of this type. The instance will be cleared.
    seed : hashable object, optional
        Seed for random number generator.

    Returns
    -------
    G : MultiDiGraph
        A graph with the specified degree sequences.
        Nodes are labeled starting at 0 with an index
        corresponding to the position in deg_sequence.

    Raises
    ------
    NetworkXError
        If the degree sequences do not have the same sum.

    See Also
    --------
    configuration_model

    Notes
    -----
    Algorithm as described by Newman [1]_.

    A non-graphical degree sequence (not realizable by some simple
    graph) is allowed since this function returns graphs with self
    loops and parallel edges.  An exception is raised if the degree
    sequences does not have the same sum.

    This configuration model construction process can lead to
    duplicate edges and loops.  You can remove the self-loops and
    parallel edges (see below) which will likely result in a graph
    that doesn't have the exact degree sequence specified.  This
    "finite-size effect" decreases as the size of the graph increases.

    References
    ----------
    .. [1] Newman, M. E. J. and Strogatz, S. H. and Watts, D. J.
       Random graphs with arbitrary degree distributions and their applications
       Phys. Rev. E, 64, 026118 (2001)

    Examples
    --------
    >>> D=nx.DiGraph([(0,1),(1,2),(2,3)]) # directed path graph
    >>> din=list(D.in_degree().values())
    >>> dout=list(D.out_degree().values())
    >>> din.append(1)
    >>> dout[0]=2
    >>> D=nx.directed_configuration_model(din,dout)

    To remove parallel edges:

    >>> D=nx.DiGraph(D)

    To remove self loops:

    >>> D.remove_edges_from(D.selfloop_edges())
    """
    if not sum(in_degree_sequence) == sum(out_degree_sequence):
        raise nx.NetworkXError('Invalid degree sequences. '
                               'Sequences must have equal sums.')

    if create_using is None:
        create_using = nx.MultiDiGraph()

    if not seed is None:
        random.seed(seed)

    nin=len(in_degree_sequence)
    nout=len(out_degree_sequence)

    # pad in- or out-degree sequence with zeros to match lengths
    if nin>nout:
        out_degree_sequence.extend((nin-nout)*[0])
    else:
        in_degree_sequence.extend((nout-nin)*[0])

    # start with empty N-node graph
    N=len(in_degree_sequence)

    # allow multiedges and selfloops
    G=nx.empty_graph(N,create_using)

    if N==0 or max(in_degree_sequence)==0: # done if no edges
        return G

    # build stublists of available degree-repeated stubs
    # e.g. for degree_sequence=[3,2,1,1,1]
    # initially, stublist=[1,1,1,2,2,3,4,5]
    # i.e., node 1 has degree=3 and is repeated 3 times, etc.
    in_stublist=[]
    for n in G:
        for i in range(in_degree_sequence[n]):
            in_stublist.append(n)

    out_stublist=[]
    for n in G:
        for i in range(out_degree_sequence[n]):
            out_stublist.append(n)

    # shuffle stublists and assign pairs by removing 2 elements at a time
    random.shuffle(in_stublist)
    random.shuffle(out_stublist)

    while in_stublist and out_stublist:
        source = out_stublist.pop()
        target = in_stublist.pop()
        if source == target or G.edges().__contains__((source, target)):
            print((source, target))
            continue
        G.add_edge(source,target)

    G.name="directed configuration_model_revised %d nodes %d edges"%(G.order(),G.size())
    return G
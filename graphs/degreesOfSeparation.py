from .breadthFirstPaths import BreadthFirstPaths
from .symbolGraph import SymbolGraph
from ..stdlib import stdio

class DegreesOfSeparation:
    """
    The DegreesOfSeparation class provides a client for finding
    the degree of separation between one distinguished individual and
    every other individual in a social network.
    As an example, if the social network consists of actors in which
    two actors are connected by a link if they appeared in the same movie,
    and Kevin Bacon is the distinguished individual, then the client
    computes the Kevin Bacon number of every actor in the network.

    The running time is proportional to the number of individuals and
    connections in the network. If the connections are given implicitly,
    as in the movie network example (where every two actors are connected
    if they appear in the same movie), the efficiency of the algorithm
    is improved by allowing both movie and actor vertices and connecting
    each movie to all of the actors that appear in that movie.
    """
    
    def __init__(self):
        """this class shouldn't be instantiated"""
        pass


    @staticmethod
    def main(args):
        """
        Reads in a social network from a file, and then repeatedly reads in
        individuals from standard input and prints out their degrees of
        separation.
        Takes three command-line arguments: the name of a file,
        a delimiter, and the name of the distinguished individual.
        Each line in the file contains the name of a vertex, followed by a
        list of the names of the vertices adjacent to that vertex,
        separated by the delimiter.
        
        :param args: the command-line arguments
        """
        filename  = args[0]
        delimiter = args[1]
        source = args[2]

        sg = SymbolGraph(filename, delimiter)
        G = sg.graph()
        if not sg.contains(source):
            stdio.writeln("{} not in database".format(source))
            return
        
        s = sg.index_of(source)
        bfs = BreadthFirstPaths(G, s)

        while not stdio.isEmpty():
            sink = stdio.readLine()
            if sg.contains(sink):
                t = sg.index_of(sink)
                if bfs.has_path_to(t):
                    for v in bfs.path_to(t):
                      stdio.writeln(sg.name_of(v))
                else:
                    stdio.writeln("Not connected")
            else:
                stdio.writeln("Not in database.")
        
    
    
    
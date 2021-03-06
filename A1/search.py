# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from pacmanPriorityQ import AI_Priority_Queue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    '''
    Return the sequence of moves to reach the goal from the start state.
    '''
    # Let a node be composed of that node's 
    # (row, col) coordinates and a list containing
    # the directions followed to reach the node.
    
    # Let fringe be a stack holding the 
    # nodes yet to be searched.
    fringe = util.Stack()
    
    # Let start be the starting node to search from 
    # and push it to the fringe.
    start = (problem.getStartState(), [])
    fringe.push(start)
    
    # Let seen be a set of all the coords 
    # that have already been visited.
    # And add the starting coordinates to seen.
    seen = set()
    #seen.add(start[0])
    
    # Search for the goal until it's found or until
    # determining that one doesn't exist.
    while not fringe.isEmpty():
        # Let curr be the current coordinates 
        # that are being searched and
        # let path be the directions 
        # followed from start to curr.
        curr, path = fringe.pop()
        
        seen.add(curr)
        
        # Found the goal!
        if problem.isGoalState(curr):
            return path
        
        # Let successors be the neighbors 
        # accessible from the current coords
        successors = problem.getSuccessors(curr)
        
        # Add each of the successors to the fringe.
        for succ, direction, _ in successors:
            if succ not in seen:
                fringe.push((succ, path + [direction]))
    
    return None
    

def breadthFirstSearch(problem):
    '''
    Search the shallowest nodes in the search tree first.
    '''
    # Let a node be composed of that node's 
    # (row, col) coordinates and a list containing
    # the directions followed to reach the node.
    
    # Let fringe be a queue holding the 
    # nodes yet to be searched.
    fringe = util.Queue()
    
    # Let start be the starting node to search from 
    # and push it to the fringe.
    start = (problem.getStartState(), [])
    fringe.push(start)
    
    # Let seen be a set of all the coords 
    # that have already been visited.
    # And add the starting coordinates to seen.
    seen = set()
    seen.add(start[0])
    
    # Search for the goal until it's found or until
    # determining that one doesn't exist.
    while not fringe.isEmpty():
        # Let curr be the current coordinates 
        # that are being searched and
        # let path be the directions 
        # followed from start to curr.
        curr, path = fringe.pop()
        
        # Found the goal!
        if problem.isGoalState(curr):
            return path
        
        # Let successors be the neighbors 
        # accessible from the current coords
        successors = problem.getSuccessors(curr)
        
        # Add each of the successors to the fringe.
        for succ, direction, _ in successors:
            if succ not in seen:
                seen.add(succ)
                fringe.push((succ, path + [direction]))


def uniformCostSearch(problem):
    '''
    Search the node of least total cost first.
    '''
    # Let a node be composed of that 
    # node's (row, col) coordinates,
    # a list containing the directions followed to reach the node,
    # and the cost to reach that node.
    
    # Let fringe be a priority queue holding the 
    # nodes yet to be searched.
    fringe = AI_Priority_Queue()
    
    # Let start be the starting node to search from 
    # and push it to the fringe.
    start = (problem.getStartState(), [], 0)
    fringe.insert(start, 0)
    
    # Let seen be a set of all the coords 
    # that have already been visited.
    # And add the starting coordinates to seen.
    seen = set()
    ##seen.add(start[0])
    
    # Search for the goal until it's found or until
    # determining that one doesn't exist.
    while True:
        # Let curr be the current coordinates that are being searched,
        # let path be the directions followed from start to curr,
        # let cost be the cost to reach curr from start.
        node, currCost = fringe.delete_min()
        curr, path = node[0], node[1]
        
        # Found the goal!
        if problem.isGoalState(curr):
            return path
        
        # Add each of the successors to the fringe.
        if curr not in seen:
            seen.add(curr)
            
            # Let successors be the neighbors 
            # accessible from the current coords
            successors = problem.getSuccessors(curr)
            
            for succ, direction, succCost in successors:
                if succ not in seen:
                    cost = currCost + succCost
                    fringe.insert((succ, path + [direction], cost), cost)
    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    '''
    Search the node that has the lowest combined cost and heuristic first.
    '''
    # Let a node be composed of that 
    # node's (row, col) coordinates,
    # a list containing the directions followed to reach the node,
    # and the cost to reach that node.
    
    # Let fringe be a priority queue holding the 
    # nodes yet to be searched.
    fringe = AI_Priority_Queue()
    
    # Let start be the starting node to search from 
    # and push it to the fringe.
    start = (problem.getStartState(), [], 0)
    fringe.insert(start, 0)
    
    # Let seen be a set of all the coords 
    # that have already been visited.
    # And add the starting coordinates to seen.
    seen = set()
        
    # Search for the goal until it's found or until
    # determining that one doesn't exist.
    while True:
        # Let curr be the current coordinates that are being searched,
        # let path be the directions followed from start to curr,
        # let currCost be the cost to reach curr from start.
        node, _ = fringe.delete_min()
        curr, path, currCost = node[0], node[1], node[2]
        
        # Found the goal!
        if problem.isGoalState(curr):
            return path
        
        if curr not in seen:
            seen.add(curr)
            
            # Let successors be the neighbors 
            # accessible from the current coords
            successors = problem.getSuccessors(curr)
        
            # Add each of the successors to the fringe.
            for succ, direction, succCost in successors:
                if succ not in seen:             
                    cost = currCost + succCost
                    totalCost = cost + heuristic(succ, problem)
                    fringe.insert((succ, path + [direction], cost), totalCost)
    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

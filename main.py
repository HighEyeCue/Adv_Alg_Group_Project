from graph_environment import Graphiest
import exhaustive_search
from has_hamiltonian import hamie
from hill_climber import hill_climber
from geneticHillClimber import geneticHillClimber
import time
from branch_and_bound import branchAndBound

# Code for testing the Class Functions
# Output in the console will be used to verify functionality

print("\n")
print("Creating a Fully Connected Graph G with weights bound by 100")
vertexCount = int(input("Enter the number of vertexes for G..  (5 or more, 5 for function tests)\n"))
G = Graphiest(vertexCount, 100)

# Test Graph
def test_graph():
    print("\n")
    print("Fettching neighbors of vertex 2")
    print()
    print(G.get_neighbors(2))
    print()

    print("Getting weigt of edge from vertex 2 to 4")
    print()
    print(G.get_edge_weight(2,4))
    print()
    print("\n")

def test_hill():
    print("\n")
    print("Making a Hill CLimber")
    h = hill_climber(0, G)
    # First Step
    print("current position is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print()
    print("taking next move")
    h.take_move(h.next_move())

    print("new current is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print("current path is")
    print(h.path)

    print("fitness is ")
    print(h.fitness_function())

    # Second Step
    print()
    print("current position is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print()
    print("taking next move")
    h.take_move(h.next_move())

    print("new current is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print("current path is")
    print(h.path)

    print("fitness is ")
    print(h.fitness_function())

    # Third Step
    print()
    print("current position is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print()
    print("taking next move")
    h.take_move(h.next_move())

    print("new current is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print("current path is")
    print(h.path)

    print("fitness is ")
    print(h.fitness_function())

    # Frouth Step
    print()
    print("current position is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print()
    print("taking next move")
    h.take_move(h.next_move())

    print("new current is")
    print(h.current)

    print("possible moves")
    print(h.possible_moves)

    print("current path is")
    print(h.path)

    print("fitness is ")
    print(h.fitness_function())

    print()
    print()
    print("is goal state")
    print(h.is_goal())

    print()
    print("________________________________")
    print()
    print("making second hill climber")
    h_2 = hill_climber(0, G)

    print ("taking four steps on same graph")
    h_2.step(4)

    print("current is")
    print(h.current)

    print("possible moves")
    print(h_2.possible_moves)

    print()
    print("is goal state")
    print(h_2.is_goal())
    print("\n")

    print("current path is")
    print(h_2.path)

    print("fitness is ")
    print(h_2.fitness_function())

def test_has_ham():
    print("\n")
    ham = hamie()
    print("has ham")
    print(ham.has_hamiltonian(G, 0))
    ham.sortList(0, len(ham.list_cycles)-1)
    print(*ham.list_cycles, sep = "\n")
    print("\n\nBest : \n")
    print(*ham.list_cycles[0])

def test_genetic_hill_climber() :
    geneticTest = geneticHillClimber(G, 4 , 2)
    print("\nGraph:")
    geneticTest.GRAPH.print()
    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("TAKING A POPULATION STEP OF SIZE "+str(geneticTest.STEP_SIZE)+".")
    geneticTest.stepPopulaion()
    print("\n_________________________________________\n")

    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("TAKING A POPULATION STEP OF SIZE "+str(geneticTest.STEP_SIZE)+".")
    geneticTest.stepPopulaion()
    print("\n_________________________________________\n")

    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("TAKING A POPULATION STEP OF SIZE "+str(geneticTest.STEP_SIZE)+".")
    geneticTest.stepPopulaion()
    print("\n_________________________________________\n")

    print("\nPopulation size: ") 
    print(geneticTest.POPULATION_SIZE)
    print("\nStep size: ")
    print(geneticTest.STEP_SIZE)
    print("\nPopulation: ")
    geneticTest.printPopulation()
    print("\nAged: ")
    geneticTest.printAged()

    print("\n_________________________________________\n")
    print("SORTING POPULATION.")
    geneticTest.sortPopulation(0, geneticTest.POPULATION_SIZE-1)
    print("\n_________________________________________\n")
    geneticTest.printPopulation()

    print(geneticTest.PARENTCOUNT)

def test_G():
    GHC = geneticHillClimber(G, 10, G.vertices_count+1)
    GHC.printPopulation()
    generations = int(input("Number of Generations..?\n"))
    start_time = time.time()
    GHC.run(generations)
    run_time = time.time() - start_time
    GHC.sortAged(0, len(GHC.AGED)-1)
    GHC.printAged()
    GHC.printBestSolution()
    print("--- %s seconds ---" % (run_time))

def to_file():
    G.toFile(input("Enter File Name\n"))

def new_g():
    print("\n")
    print("Creating a Fully Connected Graph G with weights bound by 100")
    vertexCount = int(input("Enter the number of vertexes for G..  (5 or more, 5 for function tests)\n"))
    global G
    G = Graphiest(vertexCount, 100)

def from_file():
    G.fromFile(input("Enter File Name\n"))

def test_BAB_G():
    start_time = time.time()
    BAB = branchAndBound(G)
    run_time = time.time() - start_time
    print("--- %s seconds ---" % (run_time))

def test_HC_G():
    HC = hill_climber(0, G)
    start_time = time.time()
    HC.step(G.vertices_count+1)
    run_time = time.time() - start_time
    print("\nIndividual "+ str(0) + " Path: " + str(HC.path) + " Fitness: " 
            + str(HC.fitness_function()) +" Nodes: " + str(len(HC.path)-1) +
            " Length of Path: " + str(HC.getPathWeight())) 
    print("--- %s seconds ---" % (run_time)) 

end = False

def _end():
    global end
    end = True

# mapped the inputs to the function blocks
options = {'end' : _end,
             '0' : test_graph,
             '1' : test_hill,
             '2' : test_has_ham,
             '3' : test_genetic_hill_climber,
             '4' : test_G,
             '5' : to_file,
             '6' : new_g,
             '7' : from_file,
             '8' : test_BAB_G,
             '9' : test_HC_G,
}

while(end == False):
    
    options[input(
        "=========================================\n"+
        "Enter...\n" +
        " 0  : To test the Graph.\n"+
        " 1  : To test the Hill Climber.\n"+
        " 2  : To test the Exhustive Search.\n"+
        " 3  : To test the Genetic Hill Climber.\n"+
        " 4  : To test the GHC with G.\n"+
        " 5  : To Push G to file.\n"+
        " 6  : Generate new G.\n"+
        " 7  : To Pull G from file.\n"+
        " 8  : To test the BAB with G.\n"+
        " 9  : To test the HC with G.\n"+
        "end : To end this program.\n"+
        "=========================================\n\n"
    )]()

# grabs best option in a step 
# it never revist a choices
# short nd fasr
# if an early pick was wrong, nothing can repair it. -> may or may not yield otimal soln 


# greedy Template 

def greedy(items) : 
    items = sorted(items,key=SORT_KEY) # 1. ORDER the choices -- the sort key IS the strategy  # type: ignore
    chosen=[]

    for item in items :  # 2. one pass
        if fits(item,chosen) :  # 3. take it if the solution stays valid  # type: ignore
            chosen.append(item) #    ...and never take it back
    return chosen 

# SORT_KEY and fits() change per problem. The skeleton almost never does. 
# Cost: the sort dominates -> usually O(n log n). Many problems skip the sort -> O(n).

# Name the objective — maximise a count? minimise a cost? decide yes/no?
# Propose a rule — usually a sort key, or “always take the best available”.
# Try to break it with tiny inputs before writing any code.
# Justify it in one sentence — exchange argument or stays-ahead.
# Code it (sort + scan), then state the complexity: O(n log n) with a sort, O(n) without.


import sys

# Increase recursion depth for deep game trees
sys.setrecursionlimit(2000)

def get_exponents(n):
    """Returns a sorted tuple of the exponents of the prime factorization of N."""
    exponents = []
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            exponents.append(count)
        d += 1
    if temp > 1:
        exponents.append(1)
    return tuple(sorted(exponents))

memo = {}

def solve_game(counts, can_tie):

    if not counts:
        return 0  # Previous player reached N, so current player loses.
    
    state = (counts, can_tie)
    if state in memo:
        return memo[state]
    
    # Priority: Win (2) > Tie (1) > Loss (0)
    best_outcome = 0
    
    # If a prime factor was already exhausted, current player can force a tie immediately
    if can_tie:
        best_outcome = 1

    unique_counts = set(counts)
    for val in unique_counts:
        # Create new state
        temp_list = list(counts)
        temp_list.remove(val)
        
        new_val = val - 1
        new_can_tie = can_tie
        if new_val > 0:
            temp_list.append(new_val)
        else:
            new_can_tie = True # A prime factor just hit its limit; next player can tie.
        
        new_state_tuple = tuple(sorted(temp_list))
        
        # Opponent's result
        res = solve_game(new_state_tuple, new_can_tie)
        
        # Invert opponent's result for current player
        current_val = 0
        if res == 0: current_val = 2 # Opponent loses -> I win
        elif res == 1: current_val = 1 # Opponent ties -> I tie
        else: current_val = 0          # Opponent wins -> I lose
        
        if current_val == 2: # Optimization: found a winning move
            memo[state] = 2
            return 2
        
        best_outcome = max(best_outcome, current_val)
        
    memo[state] = best_outcome
    return best_outcome

def main():
    # Using read().split() to handle all inputs at once for speed
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    results = []
    pointer = 1
    
    for _ in range(T):
        n = int(input_data[pointer])
        first_player = input_data[pointer + 1]
        pointer += 2
        
        exponents = get_exponents(n)
        
        outcome = solve_game(exponents, False)
        
        if outcome == 2:
            results.append(first_player)
        elif outcome == 1:
            results.append("tie")
        else:
            winner = "Bob" if first_player == "Alice" else "Alice"
            results.append(winner)
            
    print("\n".join(results))

if __name__ == "__main__":
    main()

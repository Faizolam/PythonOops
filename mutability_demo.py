# # ==============================================================================
# # PYTHON MUTABILITY & MEMORY ADDRESS (ID) DOCUMENTATION
# # ==============================================================================
# # This script demonstrates how Python handles object references, memory addresses,
# # and mutability when variables are passed into functions.
# # ==============================================================================

# # ------------------------------------------------------------------------------
# # CASE 1: MUTABLE OBJECTS (Lists)
# # ------------------------------------------------------------------------------
# # Lists are MUTABLE. When passed into a function, Python passes a reference 
# # to the original object. Modifications happen IN-PLACE, altering the original list.

# def change_list(L):
#     print("  [Inside Function] Initial L ID:       ", id(L))
#     L.append(5)  # Modifies the object in-place at the exact same memory address
#     print("  [Inside Function] Appended list L:    ", L)
#     print("  [Inside Function] L ID after append:  ", id(L)) # ID remains identical

# print("--- CASE 1: LIST EXECUTION (MUTABLE) ---")
# L1 = [1, 2, 3, 4]
# print("1. Original L1 ID:                      ", id(L1))
# print("2. Original L1 Value:                   ", L1)

# # Calling the function passes the reference of L1 to L
# change_list(L1) 

# print("3. Final L1 Value (OUTSIDE function):   ", L1)  # The original L1 HAS CHANGED!
# print("4. Final L1 ID (OUTSIDE function):      ", id(L1)) # The ID never changed

# # Note on Cloning: 
# # If you run `change_list(L1[:])`, Python creates a brand new copy of L1 
# # at a different memory address. The function would modify that copy, 
# # leaving the original L1 completely untouched.


# print("\n" + "-"*70 + "\n")


# # ------------------------------------------------------------------------------
# # CASE 2: IMMUTABLE OBJECTS (Tuples)
# # ------------------------------------------------------------------------------
# # Tuples are IMMUTABLE. When you attempt to alter a tuple inside a function, 
# # Python cannot modify it in-place. It creates a BRAND NEW tuple object at a 
# # new memory address and reassigns the local variable to it.

# def change_tuple(T):
#     print("  [Inside Function] Initial T ID:       ", id(T))
#     T = T + (5, 6)  # Creates a NEW tuple in memory. Reassigns local variable 'T' to it.
#     print("  [Inside Function] Concatenated T:     ", T)
#     print("  [Inside Function] T ID after change:  ", id(T)) # ID changes to a new address

# print("--- CASE 2: TUPLE EXECUTION (IMMUTABLE) ---")
# T1 = (1, 2, 3, 4)
# print("1. Original T1 ID:                      ", id(T1))
# print("2. Original T1 Value:                   ", T1)

# # Calling the function passes the reference of T1 to T
# change_tuple(T1)

# print("3. Final T1 Value (OUTSIDE function):   ", T1)  # The original T1 DID NOT CHANGE!
# print("4. Final T1 ID (OUTSIDE function):      ", id(T1)) # Points to the original address




# --------------------------------------------------------------------------------------------------------



# ==============================================================================
# PYTHON PASS-BY-REFERENCE SIMULATION USING OBJECT-ORIENTED PROGRAMMING (OOP)
# ==============================================================================
# This script documents and executes the three scenarios of handling object
# references, attribute mutations, reassignments, and proper encapsulation.
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. Modifying Object Attributes (Standard OOP Approach)
# ------------------------------------------------------------------------------
# When you pass an object instance and mutate its internal state (its attributes),
# it behaves like pass-by-reference. Both variables point to the same memory ID.

class Counter:
    def __init__(self, value):
        self.value = value  # The attribute we want to modify

def increment_score(game_counter):
    print("  [Inside Func 1] Object reference ID: ", id(game_counter))
    # Modifying the attribute of the passed object in-place
    game_counter.value += 10
    print(f"  [Inside Func 1] Updated Value:       {game_counter.value}")

print("--- 1. MODIFYING ATTRIBUTES (PASS-BY-REFERENCE BEHAVIOUR) ---")
player_score = Counter(50)
print("Original Object ID:                    ", id(player_score))
print(f"Original Value Outside:                 {player_score.value}")

# Pass the object to the function
increment_score(player_score)

print(f"Final Value Outside:                    {player_score.value}") # Value HAS CHANGED!
print("Final Object ID:                       ", id(player_score))     # ID remains the same


print("\n" + "-"*70 + "\n")


# ------------------------------------------------------------------------------
# 2. The OOP Pitfall: Reassigning the Instance
# ------------------------------------------------------------------------------
# If you reassign the parameter itself to a new instance using the `=` operator,
# you break the reference link. The local variable points to a completely new ID.

class ResetCounter:
    def __init__(self, value):
        self.value = value

def reset_counter(game_counter):
    print("  [Inside Func 2] Initial Received ID: ", id(game_counter))
    # PITFALL: Reassigning the local variable to a brand new object instance
    game_counter = ResetCounter(0) 
    print("  [Inside Func 2] ID After Reassign:   ", id(game_counter)) # ID changes!
    print(f"  [Inside Func 2] Reassigned Value:    {game_counter.value}")

print("--- 2. THE OOP PITFALL (REASSIGNING THE INSTANCE VARIABLE) ---")
player_score_2 = ResetCounter(50)
print("Original Object ID:                    ", id(player_score_2))
print(f"Original Value Outside:                 {player_score_2.value}")

# Attempt to reset
reset_counter(player_score_2)

print(f"Final Value Outside:                    {player_score_2.value}") # DID NOT CHANGE!
print("Final Object ID:                       ", id(player_score_2))   # Retains original ID


print("\n" + "-"*70 + "\n")


# ------------------------------------------------------------------------------
# 3. Best Practice: Handling This Method-to-Method (Pure OOP)
# ------------------------------------------------------------------------------
# In pure object-oriented design, you rarely pass objects to standalone global functions to change them. 
# Instead, you encapsulate the logic inside methods of the class itself.

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    # Method to modify internal state safely
    def take_damage(self, amount):
        self.health -= amount

class Trap:
    def trigger(self, target_player):
        print("  [Inside Method] Received target ID:  ", id(target_player))
        # Passes the player reference and modifies it via its own encapsulated method
        target_player.take_damage(20)

print("--- 3. BEST PRACTICE (METHOD-TO-METHOD INTERACTION) ---")
hero = Player("Arthur", 100)
print("Original 'hero' Object ID:             ", id(hero))
print(f"Original Health Outside:                {hero.health}")

spike_trap = Trap()
# Pass the 'hero' object instance into the trap's method
spike_trap.trigger(hero)

print(f"Final Health Outside:                   {hero.health}") # Safely mutated via reference!
print("Final 'hero' Object ID:                ", id(hero))     # Retains original ID

# Dictionary to track the time each parent is put in
parent_time_tracker = {}

def iterate_all_times(parent_preferences, current_parent=0, current_time=0):
    if not parent_preferences:
        print("No parent preferences provided.")
        return
    
    # Base case: if we have processed all parents
    if current_parent >= len(parent_preferences):
        return parent_time_tracker
    
    # Get the current parent's preferred times list
    preferred_times = parent_preferences[current_parent]

    # Try each time slot for the current parent
    for i in range(len(preferred_times)):
        # Get the current time for the parent
        current_time_for_parent = parent_time_tracker.get(current_parent, 0)
        
        # Get the current preferred time for the parent
        preferred_time = preferred_times[(current_time_for_parent + i) % len(preferred_times)]

        # Check if the time slot is available
        if preferred_time not in parent_time_tracker.values():
            # Print the scheduled time for the parent
            print(f"Parent {current_parent + 1}, Time {current_time_for_parent + 1}: {preferred_time}")
            
            # Update the time for the current parent
            parent_time_tracker[current_parent] = (current_time_for_parent + i) % len(preferred_times)
            
            # Move to the next parent
            iterate_all_times(parent_preferences, current_parent + 1)
            return
    
    # If none of the times work for the current parent, reset the time and move to the next parent
    parent_time_tracker[current_parent] = 0
    iterate_all_times(parent_preferences, current_parent + 1)

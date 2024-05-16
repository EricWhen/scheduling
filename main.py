from Scheduler import iterate_all_times

# Main code
if __name__ == "__main__":  
    # Example parent preferences dictionary
    parent_preferences = {
        "Parent1": ["Time1", "Time2", "Time3"],
        "Parent2": ["Time2", "Time3", "Time1"],
        # Add more parents and their preferred times as needed
    }

    # Call the recursive function to iterate through all times
    iterate_all_times(parent_preferences)
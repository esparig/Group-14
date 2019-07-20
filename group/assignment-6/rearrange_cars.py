def move(state, leaving_car):
  """
  Moves a car from current lot to empty lot
  @state: a maping from each car to its current parking lot
  @leaving_car: a car which is leaving its current lot to be moved to currently empty lot
  """
  state[0], state[leaving_car] = state[leaving_car], state[0]
  
def rearrange_cars(start_state, end_state) :
  """
  @start_state: a mapping from each car to its starting parking lot
  @end_state: a mapping from each car to its goal parking lot
  """
  for i in range(1, len(start_state)):
    if start_state[i] == end_state[i]: 
      continue # if a car's goal slot is the same as its initial one, we won't move it at all
    yield "Moving car {0} from lot {1} to empty space at lot {2}".format(i, start_state[i], start_state[0])
    move(start_state, i)

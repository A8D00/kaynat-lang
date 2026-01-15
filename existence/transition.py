def transition(state, pattern):
    state.evolve(pattern.delta)
    pattern.evolve()

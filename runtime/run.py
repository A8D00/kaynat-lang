from existence.state import State
from existence.pattern import Pattern
from existence.loop import loop

def run():
    state = State()
    pattern = Pattern()
    loop(state, pattern)

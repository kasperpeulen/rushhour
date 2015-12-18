import time


class BenchMark:
    states_count = 0

    steps_made = 0

    start_time = None

    @staticmethod
    def start_the_time():
        BenchMark.start_time = time.time()

    @staticmethod
    def log_states_count():
        print("states count:", BenchMark.states_count)

    @staticmethod
    def log_steps_made():
        print("steps made:", BenchMark.steps_made)

    @staticmethod
    def log_time():
        current = time.time() - BenchMark.start_time
        print("time: ", current)
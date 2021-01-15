class SimpleFunctionsManager:
    def __init__(self, main_log, fm):
        pass

    def round_round(self, now, min_i, max_i):
        if now < min_i:
            return max_i
        if now > max_i:
            return min_i
        return now

    def not_round_round(self, now, min_i, max_i):
        if now < min_i:
            return min_i
        if now > max_i:
            return max_i
        return now

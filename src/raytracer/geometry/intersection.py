class Intersection:
    def __init__(self, t: float, object) -> None:
        self.t = t
        self.object = object

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Intersection):
            return NotImplemented

        return self.t == value.t and self.object == value.object
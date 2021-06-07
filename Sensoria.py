class Sensor:
    ...
    def format(self, value:Union[float, Optional[bool], Optional[float], List[Tuple[str, str]]]) -> str:
        raise NotImplementedError

class ToySensor(Sensor):
    def format(self, value: Optional[bool]) -> str:
        return "Yes"

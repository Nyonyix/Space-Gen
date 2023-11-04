from Body import Body

class Barycenter(Body):

    def __init__(self, primary_object: Body, companion_object: Body) -> None:
        super().__init__()

        self._body_type = "Barycenter"

        self._primary_object = primary_object
        self._companion_object = companion_object

        self._distance = 0.0

        self._dict_onject = self._generate_dict_object()

    def get_dict_object(self) -> dict:
        return self._dict_onject
    def get_primary_object(self) -> Body:
        return self._primary_object
    def get_companion_object(self) -> Body:
        return self._companion_object

    def set_dict_object(self, barycenter_object: dict):
        self._dict_onject = barycenter_object
    def set_primary_object(self, body: Body):
        self._primary_object = body
    def set_companion_object(self, body: Body):
        self._companion_object = body

    def _generate_dict_object(self) -> dict:

        return {"a": self._primary_object, "b": self._companion_object}
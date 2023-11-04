from Body import Body
import math
import random
import json

class SpectralClassError(Exception):
    pass
class LuminosityClassError(Exception):
    pass

class Star(Body):

    """
    Star Object, Extends Body

    Generates and stores values relevent to a star
    """

    STEFAN_BOLTZMANN_CONSTANT = 5.67037e-8

    S_RADIUS = 696340 # Solar Radius in M
    S_LUMINOSITY = 3.828e+26 # Solar Luminosity in W
    S_MASS = 1.989e+30 # Solar mass in KG
    S_TEMPERATUE = 5778 # Solar temperature in K

    def __init__(self, seed: int, file_path: str) -> None:

        super().__init__()
        self._body_type = "Star"

        self._star_definitions = json.load(open(file_path, 'r'))["star"]

        self._seed = seed
        random.seed(self._seed)
        self._star_percentile = random.uniform(0, 1)

        self._planets = {}

        try:
            self._spectral_class = self._generate_spectral_class()
            self._spectral_class_number = round((1 - self._star_percentile) * 10, 1)
            self._luminosity_class = self._generate_luminosity_class()
            self._temperature = self._generate_value("temperature", "int")
            self._metallicity = 0
            self._radius = self._generate_value("radius", "float")
            self._mass = self._generate_value("mass", "float")
            self._descriptor = self._generate_descriptor()
            self._luminosity = self._calculate_luminosity()

            self._surface_gravity = self.calculate_surface_gravity(self._mass * self.S_MASS, self._radius * self.S_RADIUS)
            self._volume = self.calculate_volume((self._radius * self.S_RADIUS) * 100)
            self._density = self.calculate_density((self._mass * self.S_MASS) * 1e+3, self._volume)
        
        except SpectralClassError:
            self._spectral_class = "E"
            self._temperature = 0
            self._spectral_class_number = 0
            self._metallicity = 0
            self._luminosity_class = "E"
            self._luminosity = 0
            self._radius = 0
            self._mass = 0
            self._descriptor = "Spectral Error, Generation Failed."
            self._surface_gravity = 0
            self._volume = 0
            self._density = 0
        
        except LuminosityClassError:
            self._spectral_class = self._spectral_class
            self._temperature = 0
            self._spectral_class_number = 0
            self._metallicity = 0
            self._luminosity_class = "E"
            self._luminosity = 0
            self._radius = 0
            self._mass = 0
            self._descriptor = "Luminosity Error, Generation Failed."
            self._surface_gravity = 0
            self._volume = 0
            self._density = 0

    def get_luminosity(self, format: bool) -> float:
        return round(self._luminosity, 3) if format else self._luminosity * self.S_LUMINOSITY
    def get_radius(self, format: bool) -> float:
        return round(self._radius, 3) if format else self._radius * self.S_RADIUS
    def get_mass(self, format: bool) -> float:
        return round(self._mass, 3) if format else self._mass * self.S_MASS
    def get_surface_gravity(self, format: bool) -> float:
        return round(self._surface_gravity / 9.81, 3) if format else self._surface_gravity
    def get_density(self, format: bool) -> float:
        return round(self._density, 3) if format else self._density

    def get_temperature(self) -> int | float:
        return self._temperature
    def get_spectral_class(self) -> str:
        return self._spectral_class
    def get_spectral_class_scaler(self) -> float:
        return self._spectral_class_number
    def get_luminosity_class(self) -> str:
        return self._luminosity_class
    def get_descriptor(self) -> str:
        return self._descriptor
    def get_star_percentile(self) -> float:
        return self._star_percentile
    def get_metallicity(self) -> float:
        return self._metallicity
    def get_planets(self) -> dict:
        return self._planets

    def set_temperature(self, value: int):
        self._temperature = value   
    def set_spectral_class(self, value: str):
        self._spectral_class = value
    def set_spectral_class_scaler(self, value: float):
        self._spectral_class_number = value
    def set_luminosity_class(self, value: str):
        self._luminosity_class = value
    def set_descriptor(self, value: str):
        self._descriptor = value
    def set_star_percentile(self, value: float):
        self._star_percentile = value
    def set_metallicity(self, value: float):
        self._metallicity = value
    def set_planets(self, value: dict):
        self._planets = value
    def set_luminosity(self, value: float):
        self._luminosity = value
    
    def _generate_spectral_class(self) -> str:

        current_probability = 0
        random_spectral_class_number = random.uniform(0, 1)

        for k, v in self._star_definitions.items():
            
            current_probability += v["weight"]

            if random_spectral_class_number <= current_probability:
                return k
        raise SpectralClassError
    
    def _generate_luminosity_class(self) -> str:

        current_probability = 0
        random_luminosity_class_number = random.uniform(0, 1)

        for k, v in self._star_definitions[self._spectral_class]["luminosity_classes"].items():

            current_probability += v["weight"]

            if random_luminosity_class_number <= current_probability:
                return k
        raise LuminosityClassError 
    
    def  _generate_descriptor(self) -> str:

        written_description = self._star_definitions[self._spectral_class]["descriptor"] + " " + self._star_definitions[self._spectral_class]["luminosity_classes"][self._luminosity_class]["descriptor"]
        classification = self._spectral_class + " " + str(self._spectral_class_number) + " " + self._luminosity_class

        return classification + " " + written_description

    def _generate_value(self, value_to_generate: str, value_type: str) -> int | float:

        value_to_generate += "_range"
        min_val, max_val = self._star_definitions[self._spectral_class]["luminosity_classes"][self._luminosity_class][value_to_generate]

        random_offset = random.uniform(0, 0.05)
        if random.randint(0, 1) == 1:
            return_value = (min_val + ((max_val - min_val) * self._star_percentile)) + (random_offset * (max_val - min_val))
        else:
            return_value = (min_val + ((max_val - min_val) * self._star_percentile)) - (random_offset * (max_val - min_val))

        if value_type.lower() == "int":
            return round(return_value)
        elif value_type.lower() == "float":
            return return_value
        else:
            raise ValueError(f"Unsupported type passed: {value_type}")
    
    def _calculate_luminosity(self) -> float:

        return (4 * math.pi * ((self._radius * self.S_RADIUS) ** 2)) * (self.STEFAN_BOLTZMANN_CONSTANT * (self._temperature ** 4)) / self.S_LUMINOSITY

if __name__ == "__main__":
    print("This is not to be run by it's self.")
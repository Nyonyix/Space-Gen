import math
import random

class Body:

    GRAVITATIONAL_CONSTANT = 6.67430e-11
    AU_IN_METERS = 149597870.7
    LIGHTYEARS_IN_AU = 63241.1
    LIGHTYEARS_IN_METERS = LIGHTYEARS_IN_AU * AU_IN_METERS
    
    def __init__(self) -> None:

        self._body_type = ""
        self._designation = ""
        self._parent = ""
        self._mass = 0.0
        self._radius = 0.0
        self._surface_gravity = 0.0
        self._volume = 0.0
        self._density = 0.0
        self._surface_gravity = 0.0
        self._velocity = 0.0
        self._orbit_eccentricty = 0.0
        self._orbit_semimajor_axis = 0.0
        self._sphere_of_influence = 0.0
        self._orbital_period = 0.0

    def get_body_type(self) -> str:
        return self._body_type
    def get_designation(self) -> str:
        return self._designation
    def get_parent(self) -> str:
        return self._parent
    def get_mass(self) -> float:
        return self._mass
    def get_radius(self) -> float:
        return self._radius
    def get_surface_gravity(self) -> float:
        return self._surface_gravity
    def get_volume(self) -> float:
        return self._volume
    def get_density(self) -> float:
        return self._density
    def get_velocity(self) -> float:
        return self._velocity
    def get_orbit_eccentricty(self) -> float:
        return self._orbit_eccentricty
    def get_orbit_semimajor_axis(self) -> float:
        return self._orbit_semimajor_axis
    def get_sphere_of_influence(self) -> float:
        return self._sphere_of_influence
    def get_orbital_period(self) -> float:
        return self._orbital_period

    def set_body_type(self, value: str):
        self._body_type = value
    def set_designation(self, value: str):
        self._designation = value
    def set_parent(self, value: str):
        self._parent = value
    def set_mass(self, value: float):
        self._mass = value
    def set_radius(self, value: float):
        self._radius = value
    def set_surface_gravity(self, value: float):
        self._surface_gravity = value
    def set_volume(self, value: float):
        self._volume = value
    def set_density(self, value: float):
        self._density = value
    def set_velocity(self, value: float):
        self._velocity = value
    def set_orbit_eccentricty(self, value: float):
        self._orbit_eccentricty = value
    def set_orbit_semimajor_axis(self, value: float):
        self._orbit_semimajor_axis = value
    def set_sphere_of_influence(self, value: float):
        self._sphere_of_influence = value
    def set_orbital_period(self, value: float):
        self._orbital_period = value
    
    @staticmethod
    def calculate_volume(radius: float) -> float:
        return 4/3 * math.pi * radius ** 3

    @staticmethod
    def calculate_density(mass: float, volume: float) -> float:
        return mass / volume

    @classmethod
    def calculate_surface_gravity(cls, mass: float, radius: float) -> float:
        return cls.GRAVITATIONAL_CONSTANT * mass / radius ** 2

    @staticmethod
    def calculate_semimajor_axis(radius1: float, radius2: float) -> float:
        return 2 / (1/radius1 + 1/radius2)

    @staticmethod
    def calculate_barycenter_position(primary_mass: float, companion_mass: float, distance: float) -> tuple[float, float]:
        
        center_from_primary_mass = (distance * companion_mass) / (primary_mass + companion_mass)
        center_from_companion_mass = distance - center_from_primary_mass

        return center_from_primary_mass, center_from_companion_mass

    @staticmethod
    def calculate_hill_sphere(distance: float, mass1: float, mass2: float) -> float:
        return distance * (mass1 / (3 * mass2)) ** (1/3)
    
    @staticmethod
    def calculate_inner_binary_limit(primary_object_radius: float) -> float:
        return (primary_object_radius * 4) + (random.uniform(0, 0.1) * (primary_object_radius * 4))

    @classmethod
    def calculate_system_size(cls, object_mass: float) -> float:
        return ((2 * cls.GRAVITATIONAL_CONSTANT * object_mass) / 1000 ** 2) / 1000

    @classmethod
    def calculate_orbital_period(cls, mass: float, semi_major_axis: float) -> float:
        return math.sqrt(((semi_major_axis * cls.AU_IN_METERS) ** 3) / mass)
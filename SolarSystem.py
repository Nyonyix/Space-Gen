from Star import Star
from Body import Body
from Barycenter import Barycenter

import random
from typing import cast

class SolarSystem:

    def __init__(self, seed: int) -> None:
        
        self._seed = seed
        self._original_seed = seed
        random.seed(seed)
        self._path_to_definitions = "defs.json"

        self._galaxy_black_hole_mass = 1.9891e+37
        self._distance_to_galaxy_center = 1.41911e+20

        self._system_size = 0.0
        self._system_mass = 0.0

        self._system_objects = {}
        self._stars = []
        self._planets = []
        self._planetoids = []

        self._generate_system()

    def get_galaxy_black_hole_mass(self) -> float:
        return self._galaxy_black_hole_mass
    def get_system_objects(self) -> dict:
        return self._system_objects
    def get_stars(self) -> list:
        return self._stars
    def get_planets(self) -> list:
        return self._planets
    def get_planetoids(self) -> list:
        return self._planetoids
    def get_system_size(self) -> float:
        return self._system_size

    def set_galaxy_black_hole_mass(self, mass: float):
        self._galaxy_black_hole_mass = mass
    def set_system_objects(self, objects: dict):
        self._system_objects = objects
    def set_stars(self, stars: list):
        self._stars = stars
    def set_planets(self, planets: list):
        self._planets = planets
    def set_planetoids(self, planetoids: list):
        self._planetoids = planetoids
    def set_system_size(self, size: float):
        self._system_size = size

    def _generate_system(self):

        self._system_objects = {
            "stars": {},
            "planets": {},
            "planetoids": {}
        }

        self._stars = self._generate_stars()
        self._generate_star_layout()
        self._stars.clear()
        self._pre_orbit()
        self._generate_star_orbits()

    def _pre_orbit(self):

        if len(self._system_objects["stars"]) == 1 and isinstance(self._system_objects["stars"]["A"], Star):

            star = cast(Star, self._system_objects["stars"]["A"])

            self._system_mass = star.get_mass(False)
            self._system_size = Body.calculate_system_size(self._system_mass)

            return

        for o in self._system_objects["stars"].values():

            if isinstance(o, Star):
                self._system_mass += o.get_mass(format=False)
            elif isinstance(o, Barycenter):
                self._system_mass += o.get_mass()
            else:
                raise TypeError(f"Invalid Type: {type(o)}")

        self._system_size = Body.calculate_system_size(self._system_mass)

    def _generate_star_orbits(self):

        for i, (k, v) in enumerate(self._system_objects["stars"].items()):

            if isinstance(v, Barycenter):

                pass

            elif isinstance(v, Star):
                
                pass

            else:
                raise TypeError(f"Invalid Type: {type(v)}")

    def _generate_star_layout(self):

        workable_stars: list[Star] = self._stars.copy()
        star_designations = ["A", "B", "C", "D"]

        for i in range(len(self._stars)):

            if len(workable_stars) == 0 or len(workable_stars) < i:

                break

            if len(workable_stars) > 2:

                if random.uniform(0, 1) < 0.65:

                    primary_star = workable_stars[i]
                    workable_stars.remove(primary_star)
                    primary_star.set_designation(star_designations[i] + "a")

                    companion_star = random.choice(workable_stars)
                    workable_stars.remove(companion_star)
                    companion_star.set_designation(star_designations[i] + "b")

                    barycenter_object = Barycenter(primary_star, companion_star)
                    barycenter_object.set_designation(star_designations[i])
                    barycenter_object.set_mass(primary_star.get_mass(False) + companion_star.get_mass(False))
                    barycenter_object.set_radius(barycenter_object.calculate_inner_binary_limit(primary_star.get_radius(False)))

                    self._system_objects["stars"][star_designations[i]] = barycenter_object

                else:

                    solo_star = workable_stars[i]
                    workable_stars.remove(solo_star)
                    solo_star.set_designation(star_designations[i])

                    self._system_objects["stars"][star_designations[i]] = solo_star

            elif len(workable_stars) == 2:

                primary_star = workable_stars[0]
                primary_star.set_designation(star_designations[i] + "a")
                companion_star = workable_stars[1]
                companion_star.set_designation(star_designations[i] + "b")
                workable_stars.clear()

                barycenter_object = Barycenter(primary_star, companion_star)
                barycenter_object.set_designation(star_designations[i])
                barycenter_object.set_mass(primary_star.get_mass(False) + companion_star.get_mass(False))
                barycenter_object.set_radius(barycenter_object.calculate_inner_binary_limit(primary_star.get_radius(False)))

                self._system_objects["stars"][star_designations[i]] = barycenter_object

            else:

                solo_star = workable_stars[0]
                solo_star.set_designation(star_designations[i])

                self._system_objects["stars"][star_designations[i]] = solo_star

    def _generate_stars(self) -> list:

        stars: list[Star] = []
        sorted_stars: list[Star] = []
        number_of_stars = 0

        rand_val = random.uniform(0, 1)
        if rand_val <= 0.30:
            number_of_stars = 1
        elif rand_val <= 0.90:
            number_of_stars = 2
        elif rand_val <= 0.93:
            number_of_stars = 3
        elif rand_val <= 0.98:
            number_of_stars = 4
        else:
            number_of_stars = 5

        for s in range(number_of_stars):

            stars.append(Star(self._seed, self._path_to_definitions))
            self._seed = self._seed * 2
            random.seed(self._seed)

        sorted_stars = sorted(stars, key=lambda star: star.get_mass(format=False), reverse=True)

        return sorted_stars
        #return [sorted_stars[i:i+2] for i in range(0, len(sorted_stars), 2)]
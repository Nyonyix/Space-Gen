from SolarSystem import SolarSystem
from Barycenter import Barycenter
from Star import Star
from Body import Body

from typing import cast
import random

def main() -> None:
    
    seed = random.randint(0,9999)
    original_seed = seed

    star_count = {}
    galaxy = []

    for y in range(1000):
        system = SolarSystem(seed)
        seed += 1

        galaxy.append(system)
        system_objects = system.get_system_objects()

        for k, v in system_objects["stars"].items():

            print(f"{k}:")

            if isinstance(v, Barycenter):
                primary_star = cast(Star, v.get_primary_object())
                companion_star = cast(Star, v.get_companion_object())

                print(f"    {primary_star.get_designation()}:") # type: Star
                print(f"        {primary_star.get_descriptor()}") # type: Star
                print(f"            Temp: {primary_star.get_temperature()} K") # type: Star
                print(f"            Mass: {primary_star.get_mass(True)} M☉") # type: Star | Barycenter
                print(f"            Radius: {primary_star.get_radius(True)} R☉") # type: Barycenter
                print(f"            Density: {primary_star.get_density(False)} g/cm^3") # type: Barycenter
                print(f"            Luminosity: {primary_star.get_luminosity(True)} L☉") # type: Barycenter
                print(f"            Surface Gravity: {primary_star.get_surface_gravity(True)} G") # type: Barycenter
                print(f"            Semi Major Axis: {primary_star.get_orbit_semimajor_axis() / Body.AU_IN_METERS}") # type: Barycenter
                print(f"            Orbital Period: {primary_star.get_orbital_period()}") # type: Barycenter

                print(f"    {companion_star.get_designation()}:")
                print(f"        {companion_star.get_descriptor()}")
                print(f"            Temp: {companion_star.get_temperature()} K")
                print(f"            Mass: {companion_star.get_mass(True)} M☉")
                print(f"            Radius: {companion_star.get_radius(True)} R☉")
                print(f"            Density: {companion_star.get_density(False)} g/cm^3")
                print(f"            Luminosity: {companion_star.get_luminosity(True)} L☉")
                print(f"            Surface Gravity: {companion_star.get_surface_gravity(True)} G")
                print(f"            Semi Major Axis: {companion_star.get_orbit_semimajor_axis() / Body.AU_IN_METERS}")
                print(f"            Orbital Period: {companion_star.get_orbital_period()}")
            
            else:

                v = cast(Star, v)

                print(f"    {v.get_designation()}:") # type: Star
                print(f"        {v.get_descriptor()}") # type: Star
                print(f"            Temp: {v.get_temperature()} K") # type: Star
                print(f"            Mass: {v.get_mass(True)} M☉") # type: Star
                print(f"            Radius: {v.get_radius(True)} R☉") # type: Star
                print(f"            Density: {v.get_density(False)} g/cm^3") # type: Star
                print(f"            Luminosity: {v.get_luminosity(True)} L☉") # type: Star
                print(f"            Surface Gravity: {v.get_surface_gravity(True)} G") # type: Star

        print(f"System Size: {round(system.get_system_size() / Body.AU_IN_METERS, 3)} AU")
        print(system_objects)
        print("-" * 20)

        # print(f"{s.get_descriptor()}")
        # print(f"    Temp: {s.get_temperature()} K")
        # print(f"    Mass: {s.get_mass(True)} M☉")
        # print(f"    Radius: {s.get_radius(True)} R☉")
        # print(f"    Density: {s.get_density(False)} g/cm^3")
        # print(f"    Luminosity: {s.get_luminosity(True)} L☉")
        # print(f"    Surface Gravity: {s.get_surface_gravity(True)} G")
    print(original_seed)

if __name__ == "__main__":
    main()
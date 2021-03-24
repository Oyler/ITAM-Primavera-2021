import numpy as np
import string as st
import Generators as gen
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------
# TODO: add random name generator to the initialization of the name attribute in Person. Create method to sample
#  population from city.
# ----------------------------------------------------------------------------------------------------------------------


# Private Race class object.
class _Race:
    def __init__(self, race_name=None):
        df = pd.read_csv('Races.csv')
        keys = df['Race'].tolist()
        values = df['Lifespan'].tolist()
        races_lifespan = dict(zip(keys, values))
        if race_name is None:
            self.name = np.random.choice(list(races_lifespan.keys()))
        else:
            self.name = race_name

        self.lifespan = races_lifespan[self.name]

    def get_name(self):
        return self.name

    def get_lifespan(self):
        return self.lifespan

    def to_string(self):
        return f'race: {self.get_name()}, lifespan: {self.get_lifespan()}'


# Person class object.
class Person:

    # Class constructor.
    def __init__(self, current_year, i_d=None, race=None, gender=None, name=None, birthday=None, age=None,
                 p_o_b=None, values=None):
        """
        Class constructor.
        :param i_d: An integer that represents the person.
        :param race: The name of the race of the person (races from PHB + Orc of Eberron).
        :param name: The full name of the person in the following format: 'name, lastname'.
        :param birthday: The date of birth of the person in Y/M/D format.
        :param age: The Age of the person, if greater than it's lifespan it returns an error.
        :param p_o_b: The place of birth of the person.
        :param values: A list of moral values and ideals.
        """

        self.current_year = current_year

        # Setting the ID of the person.
        if i_d is None:
            self.ID = np.random.randint(0, 300000)
        else:
            self.ID = i_d

        # Setting the race of the person.
        if race is None:
            self.race = _Race()
        else:
            self.race = _Race(race)

        # Setting the gender of a person.
        if gender is None:
            self.gender = np.random.choice(['M', 'F', 'O'])
        else:
            self.gender = gender

        # Setting the name of the person.
        if name is None:
            def random_word(size):
                letters = st.ascii_lowercase
                return ''.join(np.random.choice(letters) for _ in range(size))

            self.name = 'REDACTED'
        else:
            self.name = name

        # Setting the birth date of a person.
        if birthday is None:
            self.birthdate = gen.birthdate(self.race, current_year)
        else:
            self.birthdate = birthday

        # Setting the age of a person.
        if age is None:
            self.age = self.current_year - self.birthdate[0]
        else:
            self.age = age

        # Setting the place of birth.
        if p_o_b is None:
            self.place_of_birth = gen.location()
        else:
            self.place_of_birth = p_o_b

        # Setting the values of the person.
        if values is None:
            self.personality_traits = gen.values()
        else:
            self.personality_traits = values

    # Getters.
    def get_ID(self):
        return self.ID

    def get_race(self):
        return self.race.get_name()

    # to_string method.
    def to_string(self):
        s = f"ID: {self.ID}\n" \
            f"Name: {self.name}\n" \
            f"Race: {self.race.get_name()}\n" \
            f"Gender: {self.gender}\n" \
            f"Date of Birth: {self.birthdate}\n" \
            f"Age: {self.age}\n" \
            f"Place of Birth: {self.place_of_birth}\n" \
            f"Personality Traits: {self.personality_traits}"
        return s


# City class object.
class City:
    def __init__(self, current_year, name=None, population_size=None, government=None):
        self.current_date = current_year
        if name is None:
            def random_word(size):
                letters = st.ascii_lowercase
                return ''.join(np.random.choice(letters) for _ in range(size))

            self.name = random_word(6)
        else:
            self.name = name

        if population_size is None:
            self.population_density = np.random.randint(100, 300000)
        else:
            self.population_density = population_size
        if government is None:
            self.gov_type = np.random.choice(['Kingdom', 'Monarchy', 'Empire', 'Democracy'])
        else:
            self.gov_type = government

        def gen_population(size):
            population = []
            for _ in range(size):
                citizen = Person(self.current_date)
                population.append(citizen)
            return population

        self.population = gen_population(self.population_density)




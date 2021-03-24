# =====================================================================================================================
# In this python package we define various random generators to use in the Fantasy Population app. We define everything
# from random age and birthday generators to random name generators.
# =====================================================================================================================

# TODO: Create random name generator using a csv file

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp
import pandas as pd


# Function that generates random integers within (low, up) with a normal distribution

def _normal_int(low, up):
    lower = 0
    upper = 1
    mu = 0.5
    sigma = 0.1

    samples = sp.truncnorm.rvs(
        (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma)
    samples = (up - low + 2) * samples + low - 1
    samples = np.round(samples).astype(int)
    return samples


# Random birth date generator based on the race of a person. Certain races in fantasy live longer.

def birthdate(race, current_date):
    """
    Function that generates a random date of birth based on the race lifespan and the current date.
    :param race: A race object
    :param current_date: The current year of the world
    :return: A triplet (Year, Month, Day)
    """
    lifespan = race.lifespan
    up = current_date
    low = current_date - lifespan
    year = _normal_int(low, up)
    month = np.random.randint(1, 12)
    day = np.random.randint(1, 35)
    return year, month, day


def location():
    continent = np.random.choice(['Xers', 'Nar Arael', 'Elaya'])
    region = None
    if continent == 'Xers':
        region = np.random.choice(['Ar Vidhal', 'Saraph', 'Khorvaire', 'Tir Nahdal', 'Zendria', 'Wastes', 'Fir',
                                   'Whuul', 'Minrathous'])
    elif continent == 'Nar Arael':
        region = np.random.choice(['Ciel Arbor', 'Ungror', 'Ingeir Lham', 'Imperium'])
    elif continent == 'Elaya':
        region = np.random.choice(['Avalon', 'Cadwen', 'Mistral', 'Geth', 'Kite', 'Orion'])

    return continent, region

def values():
    vals = []
    alignment_0 = np.random.choice(['Neutral', 'Good', 'Evil'])
    alignment_1 = np.random.choice(['Neutral', 'Lawful', 'Chaotic'])
    alignment = alignment_1 + ' ' + alignment_0
    vals.append(alignment)
    df = pd.read_csv('Values.csv')
    good_values = df['Good'].tolist()
    bad_values = df['Bad'].tolist()
    leader_values = df['Leadership'].tolist()
    good = [np.random.choice(good_values) for _ in range(3)]
    bad = [np.random.choice(bad_values) for _ in range(3)]
    leadership = [np.random.choice(leader_values) for _ in range(3)]
    vals.extend(good)
    vals.extend(bad)
    vals.extend(leadership)

    return list(set(vals))



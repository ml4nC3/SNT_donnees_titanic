from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args
import csv


# Versions corrigées des fonctions :
def quarante_deux():
    return 42


def plus_deux(a):
    return a + 2


# Jeux de données des fonctions de correction :
inputs_quarantedeux = [Args()]

inputs_plusdeux = [
    Args(5),
    Args(42),
    Args(-2),
]

###########################
# Fonctions de correction #
cr_plus_deux = ExerciseFunction(
    plus_deux,
    inputs_plusdeux,
    layout='pprint',
    layout_args=(40, 20, 35)
)

cr_quarante_deux = ExerciseFunction(
    quarante_deux,
    inputs_quarantedeux,
    layout='pprint',
    layout_args=(40, 20, 35)
)



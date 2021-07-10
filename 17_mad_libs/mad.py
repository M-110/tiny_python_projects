from typing_extensions import TypedDict


class Range(TypedDict):
    min: float
    max: float


class NutritionInformation(TypedDict):
    value: int
    unit: str
    confidenceRange95Percent: Range
    standardDeviation: float


class RecipeNutritionInformation(TypedDict):
    recipes_used: int
    calories: NutritionInformation
    fat: NutritionInformation
    protein: NutritionInformation
    carbs: NutritionInformation


def gen_stuff() -> RecipeNutritionInformation:
    ...


nutrition_information: RecipeNutritionInformation = gen_stuff()

b = nutrition_information['fat'][]

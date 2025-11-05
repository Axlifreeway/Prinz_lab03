import pandas as pd

from titanic import age_range_for


def test_age_range_normal_case():
    df = pd.DataFrame([
        {'Sex': 'male', 'Survived': 1, 'Age': 22},
        {'Sex': 'male', 'Survived': 1, 'Age': 35},
        {'Sex': 'female', 'Survived': 1, 'Age': 28},
    ])

    min_age, max_age = age_range_for(df, 'male', 1)
    assert min_age == 22.0
    assert max_age == 35.0


def test_age_range_with_missing_ages():
    df = pd.DataFrame([
        {'Sex': 'female', 'Survived': 0, 'Age': None},
        {'Sex': 'female', 'Survived': 0, 'Age': 18},
        {'Sex': 'female', 'Survived': 0, 'Age': None},
    ])

    min_age, max_age = age_range_for(df, 'female', 0)
    assert min_age == 18.0
    assert max_age == 18.0


def test_age_range_no_matches():
    df = pd.DataFrame([
        {'Sex': 'male', 'Survived': 1, 'Age': 30},
    ])

    assert age_range_for(df, 'female', 0) == (None, None)


def test_age_range_empty_df():
    df = pd.DataFrame(columns=['Sex', 'Survived', 'Age'])
    assert age_range_for(df, 'male', 1) == (None, None)

def age_range_for(df, sex, survived):

    if df is None or df.empty:
        return (None, None)

    filtered = df[(df.get('Sex') == sex) & (df.get('Survived') == survived)]
    ages = filtered['Age'].dropna()
    if ages.empty:
        return (None, None)
    return (float(ages.min()), float(ages.max()))


def main():
    import pandas as pd
    import streamlit as st

    df = pd.read_csv('titanic_train.csv')

    st.image("image.png")
    st.title('Данные пассажиров Титаника')
    st.subheader(
        'Найти диапазон возрастов пассажиров, указав пол и '
        'спасен/погиб'
    )

    col1, col2 = st.columns(2)

    with col1:
        gender_options = {
            'Мужской': 'male',
            'Женский': 'female',
        }
        selected_gender_label = st.selectbox(
            'Выберите пол:',
            ('Мужской', 'Женский'),
        )

    with col2:
        status_options = {'Спасен': 1, 'Погиб': 0}
        selected_status_label = st.selectbox(
            'Выберите статус:',
            ('Спасен', 'Погиб'),
        )

    sex = gender_options[selected_gender_label]
    survived = status_options[selected_status_label]

    min_age, max_age = age_range_for(df, sex, survived)

    st.write(
        f"Результаты для: **{selected_gender_label}, "
        f"{selected_status_label.lower()}"
    )

    if min_age is not None and max_age is not None:
        results_col1, results_col2 = st.columns(2)
        results_col1.metric(
            "Минимальный возраст", f"{min_age:.1f} лет"
        )
        results_col2.metric(
            "Максимальный возраст", f"{max_age:.1f} лет"
        )
    else:
        st.warning("Нет данных")

    if st.checkbox('Показать отфильтрованные данные'):
        filtered = df[(df['Sex'] == sex) & (df['Survived'] == survived)]
        st.write(filtered)


if __name__ == '__main__':
    main()

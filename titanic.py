import streamlit as st
import pandas as pd

df = pd.read_csv('titanic_train.csv')


st.image("image.png")



st.title('Данные пассажиров Титаника')
st.subheader('Найти диапазон возрастов пассажиров, указав пол и спасен/погиб')

col1, col2 = st.columns(2)

with col1:
    gender_options = {'Мужской': 'male', 'Женский': 'female'}
    selected_gender_label = st.selectbox('Выберите пол:', ('Мужской', 'Женский'))

with col2:
    status_options = {'Спасен': 1, 'Погиб': 0}
    selected_status_label = st.selectbox('Выберите статус:', ('Спасен', 'Погиб'))


filtered_df = df[
    (df['Sex'] == gender_options[selected_gender_label]) &
    (df['Survived'] == status_options[selected_status_label])
]


min_age = filtered_df['Age'].dropna().min()
max_age = filtered_df['Age'].dropna().max()


st.write(f"Результаты для: **{selected_gender_label}, {selected_status_label.lower()}**")

if not pd.isna(min_age) and not pd.isna(max_age):
    results_col1, results_col2 = st.columns(2)
    results_col1.metric("Минимальный возраст", f"{min_age:.1f} лет")
    results_col2.metric("Максимальный возраст", f"{max_age:.1f} лет")
else:
    st.warning("Нет данных")

if st.checkbox('Показать отфильтрованные данные'):
    st.write(filtered_df)
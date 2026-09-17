import pandas as pd
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="선수 통계",
    page_icon='⚽',
    layout="wide")

#BASE_DIR = Path(__file__).resolve().parent
#DATA_PATH = BASE_DIR / 'data' / 'data_csv'
#df = pd.read_csv(DATA_PATH)

df = pd.read_csv("data/data.csv")

#----사이드바(1)
with st.sidebar:
    st.subheader('찾아보기')
    team=st.selectbox('팀 선택', ['전체','서울FC',
                            '부산유나이티드','인천드래곤즈','대구타이거즈',
                            '광주스타즈','수원블루윙즈','울산샤크스','전북그린스','포항스틸러스','제주유나이티드'
])

if team == '전체':
    filtered = df.copy()

else:
    filtered = df[df['팀'] == team]


st.title('선수 통계')
st.write(f'선택된 팀:{team}')
st.dataframe(filtered, hide_index=True)
#----

#최다 출전 KPI
max_matchs = filtered['경기수'].max()

#최다 득점 KPI
max_goal = filtered['득점'].max()

#최다 도움 KPI
max_assist = filtered['도움'].max()


#----
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('최다 출전(경기)',value=max_matchs,border=True)

with col2:
    st.metric('최다 득점(골)', value=max_goal,border=True)

with col3:
    st.metric('최다 도움(도움)', value=max_assist,border=True)

#---

if team == '전체':
    top_matches = df.nlargest(5, '경기수')[['이름', '팀', '경기수']]
    with st.expander("⚽ 경기수 TOP5"):
        st.dataframe(top_matches, hide_index=True)

    top_goal = df.nlargest(5, '득점')[['이름','팀','득점']]
    with st.expander('⚽ 득점 TOP5'):
        st.dataframe(top_goal, hide_index=True)

    top_assist = df.nlargest(5, '도움')[['이름','팀','도움']]
    with st.expander('⚽ 도움 TOP5'):
        st.dataframe(top_assist, hide_index=True)

#---사이드바(2)

with st.sidebar:
    st.subheader('팀별 상세 통계')

    stat_option = st.radio(
        '선택',
        ['팀별 평균 경기수', '팀별 평균 득점', '팀별 평균 도움']
    )

if stat_option == '팀별 평균 경기수':
    avg_matchs=df.groupby('팀')['경기수'].mean()
    st.subheader('팀별 평균 경기수')
    st.bar_chart(avg_matchs)


if stat_option == '팀별 평균 득점':
    avg_goal=df.groupby('팀')['득점'].mean()
    st.subheader('팀별 평균 득점')
    st.bar_chart(avg_goal)

if stat_option == '팀별 평균 도움':
    avg_assist=df.groupby('팀')['도움'].mean()
    st.subheader('팀별 평균 도움')
    st.bar_chart(avg_assist)

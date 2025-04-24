
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Simulated Data
lineup_data = {
    'Lineup': ['Core + Sydney', 'Core + Tia', 'Core + Hannah', 'Core + Maya'],
    'Estimated Runs': [0.528, 0.516, 0.508, 0.506],
    'Sydney Barker': [0.108, 0, 0, 0],
    'Tia Milloy': [0, 0.096, 0, 0],
    'Hannah Coor': [0, 0, 0.085, 0],
    'Maya Bland': [0, 0, 0, 0.084],
    '8-Starters': [0.42]*4
}

lineup_df = pd.DataFrame(lineup_data)

st.title("OU Softball Lineup Optimization Dashboard")

# Bar Chart
st.subheader("Expected Runs per Lineup (Overall Stats)")
colors = ['#2E8B57', '#1E90FF', '#8A2BE2', '#FF6347']
bar_fig = go.Figure([go.Bar(x=lineup_df['Lineup'], y=lineup_df['Estimated Runs'], marker_color=colors)])
bar_fig.update_layout(yaxis_title='Estimated Runs', xaxis_title='Lineup')
st.plotly_chart(bar_fig)

# Stacked Contribution Chart
st.subheader("Player Contribution Breakdown")
stacked_fig = go.Figure()
stacked_fig.add_trace(go.Bar(name='8-Starters', x=lineup_df['Lineup'], y=lineup_df['8-Starters'], marker_color='#708090'))
stacked_fig.add_trace(go.Bar(name='Sydney Barker', x=[lineup_df['Lineup'][0]], y=[lineup_df['Sydney Barker'][0]], marker_color='#FFD700'))
stacked_fig.add_trace(go.Bar(name='Tia Milloy', x=[lineup_df['Lineup'][1]], y=[lineup_df['Tia Milloy'][1]], marker_color='#FF69B4'))
stacked_fig.add_trace(go.Bar(name='Hannah Coor', x=[lineup_df['Lineup'][2]], y=[lineup_df['Hannah Coor'][2]], marker_color='#00CED1'))
stacked_fig.add_trace(go.Bar(name='Maya Bland', x=[lineup_df['Lineup'][3]], y=[lineup_df['Maya Bland'][3]], marker_color='#DA70D6'))
stacked_fig.update_layout(barmode='stack', yaxis_title='Run Contribution')
st.plotly_chart(stacked_fig)

# Dropdown Interactive Comparison
st.subheader("Compare Alternate Players")
alternate_choice = st.selectbox("Choose Alternate Player:", ['Sydney Barker', 'Tia Milloy', 'Hannah Coor', 'Maya Bland'])
alt_index = ['Sydney Barker', 'Tia Milloy', 'Hannah Coor', 'Maya Bland'].index(alternate_choice)
selected_run = lineup_df['Estimated Runs'][alt_index]
alt_colors = {
    'Sydney Barker': '#FFD700',
    'Tia Milloy': '#FF69B4',
    'Hannah Coor': '#00CED1',
    'Maya Bland': '#DA70D6'
}

alt_fig = go.Figure()
alt_fig.add_trace(go.Bar(x=['8-Starters'], y=[0.42], name='8-Starters', marker_color='#708090'))
alt_fig.add_trace(go.Bar(x=[alternate_choice], y=[selected_run - 0.42], name=alternate_choice, marker_color=alt_colors[alternate_choice]))
alt_fig.update_layout(barmode='stack', title=f"Run Contribution: 8-Starters + {alternate_choice}", yaxis_title='Estimated Runs')
st.plotly_chart(alt_fig)

st.info("Use the dropdown above to test each alternate player's impact on the lineup.")

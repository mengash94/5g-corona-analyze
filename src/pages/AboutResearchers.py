from dash import html

def AboutResearchers():
    return html.Div([
        html.H3("About the Researchers:",style={'textAlign': 'center'}),
        html.P("We are a dedicated team of students from the Information Systems Management program at the Academic Center for Law and Business."),
        html.P("Passionate about leveraging technology to understand and solve real-world problems, we have diverse backgrounds and interests that range from data analysis to social media dynamics and crisis management."),
        html.P("Our research journey began as part of our final project, where we sought to understand the spread and impact of misinformation on Twitter during emergencies."),
        html.P("Under the esteemed guidance of Dr. Avi Yussoff, we embarked on this project with the goal of using data-driven insights to improve the accuracy and reliability of information shared during global crises."),
        html.P("Throughout the process, we have gained invaluable knowledge and skills in areas like sentiment analysis, data visualization, text preprocessing, time series forecasting, and text classification with advanced models like BERT."),
        html.P("We're excited to share our findings and insights with you, and we hope that our work contributes to the ongoing discussions about information accuracy on social media platforms during emergencies."),
    ], style={'backgroundColor': 'white', 'color': 'black', 'padding': '15px'})

from dash import html

def AboutWriter():
    return html.Div([
        html.H3('About the Writer'),
        html.P('We are students at the Academic Center for Law and Business in Information Systems Management.'),
        html.Br(),
        html.P('We carried out the research as part of a final project Under the guidance of Dr. Avi Yussoff.'),
    ])

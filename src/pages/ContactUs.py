from dash import html

def ContactUs():
    return html.Div([
        html.H3("Contact Us:"),
        html.P("We value your input and feedback on our project. Whether you have a question, suggestion, or just want to discuss the research, we'd love to hear from you!"),
        html.P("To get in touch, you can:"),
        html.Ol([
            html.P([html.U("Email Us:"), " Feel free to send us an email at Yakirattias7@gmail.com and mengash94@gmail.com. We aim to respond to all queries within 48 hours."])
        ]),
        html.P("Your insights can help us refine our research and better understand the impact of our work."),
        html.P(" Thank you for your interest and engagement!")
    ], style={'backgroundColor': 'white', 'color': 'black', 'padding': '15px'})

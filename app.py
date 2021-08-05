import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

#Import Figures defined in figures.py folder
from figures import *

#Print Initial message - Doesnot have any impact on the application. Just a simple stratup message to show on the console
print('============================================\nMultipage Dashboard App Boilerplate using Plotly Dash\n============================================')
print('Designed by: Manaruchi Mohapatra (https://github.com/manaruchi)')
print('Setting Up and Starting Server... Please Wait...\n')


#---------Dash App Declaration-------------------------------------------------------------------------------------------------------------------
#Font Awesome provides really nice icons for free.
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"

#I have used bootstrap theme DARKLY. YOu can find more themes at https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY, FONT_AWESOME], update_title=None,
                        suppress_callback_exceptions=True)

app.title = 'Multipage Dashboard'


#--------Function to generate the side navigation bar------------------------------------------------------------
def generate_linkbar(active_val):
    buttons_list = [{'label': 'Page 1', 'href': '/', 'logo': industry_logo},
                    {'label': 'Page 2', 'href': '/page2', 'logo': admin_logo},
                    {'label': 'Page 3', 'href': '/page3', 'logo': admin_logo},
                    {'label': 'Page 4', 'href': '/page4', 'logo': about_logo},
                    {'label': 'Page 5', 'href': '/page5', 'logo': login_logo}]

    elements_list = [dbc.Button(html.I(className = 'fas fa-arrow-circle-right fa-lg'), id = 'open-button', color = 'dark')]
    for i in buttons_list:
        if(i['href'] == active_val):
            elements_list.append(dcc.Link(html.Div([html.Img(src=i['logo'], className = 'nav-bar-options-img'), html.P(i['label'], className = 'nav-bar-options-p')], className = 'nav-bar-options-active'), href = i['href'], refresh = True, style = {'color': 'white'}))
        else:
            elements_list.append(dcc.Link(html.Div([html.Img(src=i['logo'], className = 'nav-bar-options-img'), html.P(i['label'], className = 'nav-bar-options-p')], className = 'nav-bar-options'), href = i['href'], refresh = True, style = {'color': 'white'}))

    return elements_list


# ### Layout for the Sidebar -------------------------------------------------------------------------------------------------------------------

sidebar_layout = [dbc.Button(html.I(className = 'fas fa-arrow-circle-right fa-lg'), id = 'open-button', color = 'dark')]
#-----------------------------------------------------------------------------------------------------------------------------------------------

app.layout = html.Div([
                html.Div(sidebar_layout, id = 'sidebar', style = {'width': '50px'}),

                html.Div([html.Div([

                    html.P(['Multipage Dashboard App'], id = 'header-nav-wbdis'),
                    dcc.Location(id='url', refresh=True),
                ], id = 'headernav')], id = 'main-div'),

                html.Div(html.Div(html.Img(src = spinner_anim, width = 150, height = 150), id = 'loading-screen-industry'),id='page-content')
            ], id = 'mainbody')


#------------------CALLBACKS-------------------------------------------------------------------------------------------------------------------
#Callback to open the side bar when the expand button is clicked.
@app.callback(Output('sidebar', 'style'), Output('open-button', 'style'), [Input('open-button', 'n_clicks')], prevent_initial_call = True)
def showsidebar(n):
    if(n):
        if(n%2 == 1):
            return {'width': '200px'}, {'transform': 'rotate(180deg)'}
        else:
            return {'width': '50px'}, {'transform': 'rotate(0deg)'}
    else:
        return {'width': '50px'}, {'transform': 'rotate(0deg)'}


# ### URL Routing

#Callback to set the side navigation bar content
@app.callback(Output('sidebar', 'children'),[Input('url', 'pathname')])
def generate_sidebar(url):
    return generate_linkbar(url)

#Page content to be generated according to the path
@app.callback(Output('page-content','children'),
             [Input('url', 'pathname')])
def navigate_app(path):
    if(path == '/'):
        return dbc.Alert('Page 1')
    elif(path == '/page2'):
        return dbc.Alert('Page 2')
    elif(path == '/page3'):
        return dbc.Alert('Page 3')
    elif(path == '/page4'):
        return dbc.Alert('Page 4')
    elif(path == '/page5'):
        return dbc.Alert('Page 5')
    else:
        return dbc.Alert('Page not available', color = 'danger')



if __name__ == '__main__':
    app.run_server()

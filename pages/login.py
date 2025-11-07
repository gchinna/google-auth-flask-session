import dash
from dash import html, dcc
from utils.helpers import iconify
import dash_mantine_components as dmc 

dash.register_page(__name__)
from dash_iconify import DashIconify


dash.register_page(__name__)

loginWithGoogleStyle =   {
    "textDecoration": "white",
    "borderRadius": "50px",
  }

layout = dmc.Center(
    dmc.Paper(
        shadow='sm',
        p = "30px",
        mt = 60,
        children = [
            html.Form(
                style = {"width":'300px'},
                method='POST',
                children = [
                    dmc.Divider(label="Sign-in with", mb = 10, mt = 10, size="md"),
                    html.A(
                        href='/signingoogle', 
                        style = loginWithGoogleStyle,
                        children = [
                            dmc.Button(
                                "Google",
                                variant="outline",
                                color = "#E418C2ff",
                                fullWidth=True,
                                radius='xl',
                                leftSection=DashIconify(icon="flat-color-icons:google"),
                            ),
                        ]
                    ),
                ]
            )
        ]
    )
)



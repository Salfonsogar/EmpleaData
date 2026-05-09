from dash import Input, Output
from visualizations.correlacion import figura_correlacion_frontera


def register_extra_callbacks(app):
    @app.callback(
        Output("grafica-correlacion", "figure"),
        Input("slider-año", "value")
    )
    def actualizar_correlacion(año):
        return figura_correlacion_frontera(año)

    @app.callback(
        Output("contenido-correlacion", "style"),
        Output("toggle-correlacion", "children"),
        Input("toggle-correlacion", "n_clicks"),
    )
    def toggle_correlacion(n_clicks):
        if n_clicks and n_clicks % 2 == 1:
            return {"display": "block", "marginTop": "12px"}, \
                   "\u25bc Ocultar an\u00e1lisis de correlaci\u00f3n fronteriza"
        return {"display": "none"}, \
               "\u25b6 Ver an\u00e1lisis de correlaci\u00f3n fronteriza (+0.5)"

import flet as ft

# Criação do ColorScheme utilizando a nova paleta de cores
custom_color_scheme = ft.ColorScheme(
    primary="#BB86FC",
    on_primary="#1E1E1E",
    secondary="#03DAC6",
    on_secondary="#1E1E1E",
    background="#1E1E1E",
    on_background="#FFFFFF",
    surface="#2C2C2C",
    on_surface="#FFFFFF",
    error="#CF6679",
    on_error="#1E1E1E",
)

# Definindo o tema utilizando o ColorScheme criado
custom_theme = ft.Theme(
    color_scheme=custom_color_scheme
)

# Definindo estilos de texto padrão
default_headline_style = ft.TextStyle(
    font_family="Roboto",
    size=24,  # Tamanho da fonte
    color="#FFFFFF"
)

default_body_style = ft.TextStyle(
    font_family="Roboto",
    size=16,  # Tamanho da fonte
    color="#B0B0B0"  
)
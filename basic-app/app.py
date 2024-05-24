import sys 

from shiny import App, render, ui
from poketracker.src.poketracker import Poketracker

sys.path.insert(0, '/e/datamunchio/dev/poketracker/src')
poke = Poketracker() 

app_ui = ui.page_fluid(
    ui.panel_title('PokeTracker'),
    ui.input_selectize(
        'selectize',
        'Choose your card:',
        poke.searchables
    ),
    ui.output_text('value')
)


def server(input, output, session):
    @render.text 
    def value():
        return f'{input.selectize()}'


app = App(app_ui, server)

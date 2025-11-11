import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO

    def popola_dropdown_musei(self):

        self._view._dd_museo.options.append(ft.dropdown.Option(None, "Nessun filtro"))

        musei = self._model.get_musei()

        if not musei:
            self._view.show_alert("Errore nel recupero dei dati dal database.")
            return

        for museo in musei:
            self._view._dd_museo.options.append(ft.dropdown.Option(key = str(museo.id), text=museo.nome))

        self._view.update()

    def popola_dropdown_epoche(self):

        self._view._dd_epoca.options.append(ft.dropdown.Option(key=None, text = "Nessun filtro"))

        epoche = self._model.get_epoche()

        if not epoche:
            self._view.show_alert("Errore nel recupero dei dati dal database.")
            return

        for epoca in epoche:
            self._view._dd_epoca.options.append(ft.dropdown.Option(key = epoca, text=epoca))

        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO

    def handle_selezione_epoca(self, e):
        self.epoca_selezionata = self._view._dd_epoca.value

    def handle_selezione_museo(self, e):
        self.museo_selezionato = self._view._dd_museo.value


    # AZIONE: MOSTRA ARTEFATTI
    # TODO

    def handle_mostra_artefatti(self, e):

        museo_filtro_str = self.museo_selezionato
        epoca_filtro = self.epoca_selezionata

        museo_filtro_int = None
        if museo_filtro_str is not None:
            try:
                museo_filtro_int = int(museo_filtro_str)
            except ValueError:
                museo_filtro_int = None

        artefatti = self._model.get_artefatti_filtrati(museo_filtro_int, epoca_filtro)

        if artefatti is None:
            self._view.show_alert("Errore durante la ricerca degli artefatti nel database.")
            return

        self._view._lv_risultati.controls.clear()

        if not artefatti:
            self._view._lv_risultati.controls.append(
                ft.Text("Nessun artefatto trovato con i filtri selezionati.")
            )
        else:
            self.add_results_to_view(artefatti)

        self._view.update()

    def add_results_to_view(self, artefatti):

        self._view._lv_risultati.controls.append(
            ft.Text(f"Trovati {len(artefatti)} artefatti:", weight=ft.FontWeight.BOLD))

        for artefatto in artefatti:
            testo = (
                f"ID: {artefatto.id} | Nome: {artefatto.nome} | "
                f"Epoca: {artefatto.epoca} | ID Museo: {artefatto.id_museo}"
            )

            self._view._lv_risultati.controls.append(
                ft.Text(testo)
            )




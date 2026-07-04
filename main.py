import os
from app.dao.Produto_dao import Produto_dao
from app.views.Produto_view import Produto_Terminal_View
from app.controllers.Produto_controller import Produto_Controller
if __name__ == "__main__":
    dao = Produto_dao()
    view = Produto_Terminal_View()
    controller = Produto_Controller(dao, view)
    controller.inicializar_sistema()
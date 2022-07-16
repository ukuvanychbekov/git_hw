from . import views
from . import app


# urls for posts
app.add_url_rule('/', view_func=views.index, methods=['GET'], endpoint='index')
app.add_url_rule('/add', view_func=views.transactions_add, methods=['GET', 'POST'], endpoint='transactions_add')
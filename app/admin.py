from flask_admin.contrib.sqla import ModelView
from app.models import DBSession, User, Question

admin_session = DBSession()
ModelView.create_modal = True
ModelView.edit_modal = True
from flask import Blueprint

bp_user = Blueprint('user', __name__)

from .route import *
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required
)

play_views = Blueprint('play_views', __name__, template_folder='../templates')
@play_views.route('/play',methods=["GET"])
@jwt_required()
def play_page():
    return render_template("play.html")


def get_daily_cipher():
    
    return cipher
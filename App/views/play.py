from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for,g
from flask_jwt_extended import jwt_required, get_jwt_identity


from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required,
    create_cipher,
    create_game,
    check_guess,
    delete_game
)
from App.models import (Game, Guess, Score, User)

play_views = Blueprint('play_views', __name__, template_folder='../templates')
@play_views.route('/play',methods=["GET"])
@jwt_required()
def play_page():
    game = start_game()
    return render_template("play.html", w_l = 0)

@play_views.route('/submit_guess', methods=['POST'])
@jwt_required()
def make_guess():
    user_id = get_jwt_identity()
    game = Game.query.filter_by(user_id = user_id).order_by(Game.id.desc()).first()
    data = request.form
    check_guess(game.id,int(data['guess1']),int(data['guess2']),int(data['guess3']),int(data['guess4']))
    guesses = Guess.query.filter_by(score_id=game.score_id).all()

    return render_template("play.html", guesses= guesses, w_l = game.win)

@play_views.route('/forfeit' ,methods=['POST'])
@jwt_required()
def forfeit():
    user_id = get_jwt_identity()
    
    delete_game(user_id)  
    start_game()  
    return render_template("play.html",w_l = 0)

def get_daily_cipher():
    cipher = create_cipher()
    return cipher

@jwt_required()
def start_game():
    user_id = get_jwt_identity()
    return create_game(user_id)
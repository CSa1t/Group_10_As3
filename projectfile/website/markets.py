from flask import Blueprint, render_template, request, redirect, url_for

# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('market', __name__, url_prefix='/markets')


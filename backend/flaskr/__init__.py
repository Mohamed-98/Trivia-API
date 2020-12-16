import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS'
        )
        return response

    @app.route('/categories', methods=['GET'])
    def get_all_categories():
        categories = Category.query.order_by(Category.type).all()
        formatted_category = [category.format() for category in categories]
        return jsonify({
            'success': True,
            'categories': formatted_category
        })
    
    @app.route('/questions', methods=['GET'])
    def get_questions():
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10
        questions = Question.query.all()
        formatted_Question = [question.format() for question in questions]
        questions_page = formatted_Question[start:end]
        categories = Category.query.order_by(Category.type).all()
        if len(questions_page) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'questions': questions_page,
            'total_questions': len(questions_page),
            'categories': {
                category.id: category.type for category in categories}
        })
    
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delet_questions(question_id):
        question = Question.query.get(question_id)
        question.delete()
        return jsonify({
            'success': True,
            'deleted': question_id
        })
    return app

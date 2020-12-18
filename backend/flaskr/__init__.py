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
        if question is None:
            abort(405)

        else:
            return jsonify({
                'success': True,
                'deleted': question_id
            })

    @app.route('/questions', methods=['POST'])
    def create_questions():
        body = request.get_json()
        #if not ('question' in body and 'answer' in body and 'difficulty' in body and 'category' in body):
        #    abort(422)

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)

        try:
            question = Question(question=new_question, answer=new_answer,
                                category=new_category, difficulty=new_difficulty)
            question.insert()
            
            #selection = Question.query.get(question_id).all()
            #current_question = 
            return jsonify({
                'success': True,
                'new_question': question.id
            })

        except:
            abort(422)

    @app.route('/questions/search', methods=['POST'])
    def searching():
        body = request.get_json()
        search = body.get('Search')

        try:
            search_res = Question.query.filter(
            Question.question.ilike(f'%{Search}%')).all()
            
            return jsonify({
                'success': True,
                'questions': [question.format() for question in search_res],
                'total_questions': len(search_res),
                'current_category': None
            })
        except:
            abort(404)

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def list_questions(category_id):
        try:
            #category = Category.query.filter_by(
            #    id=category_id).one_or_none()
            questions = Question.query.filter(
                Question.category == str(category_id)).all()
            total_questions = len(questions)
            #questions = Question.query.all()
            #formatted_Question = [question.format() for question in questions]
            #questions_page = formatted_Question[start:end]
            return jsonify({
                'success': True,
                'questions': [question.format() for question in questions],
                'totalQuestions': total_questions,
                'categories': category_id
            })
        except:
            abort(404)

    @app.route('/quizzes', methods=['POST'])
    def quizz():
        body = request.get_json()
        if not body:
            abort(404)
        category = body.get('quiz_category')
        previous_questions = body.get('previous_questions')
        category_id = int(category['id'])
        if category_id == 0:
            selection = Question.query.order_by(func.random())
        else:
            selection = Question.query.filter(
                Question.category == category_id).order_by(func.random())
            question = selection.filter(Question.id.notin_(
                previous_questions)).first()
            return jsonify({
                'success': True,
                'question': question.format()
            })

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400
    return app

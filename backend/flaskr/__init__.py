import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    question = [question.format() for question in selection]
    current_question = question[start:end]
    return current_question

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
    def get_all_questions():
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
            'total_questions': len(questions),
            'categories': {
                category.id: category.type for category in categories}
        })
    
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delet_the_questions(question_id):
        question = Question.query.get(question_id)
        
        if question is None:
            abort(404)

        question.delete()
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)

        return jsonify({
            'success': True,
            'deleted': question_id,
            'question': current_questions,
            'total_question': len(Question.query.all())
            })

    @app.route('/questions/new', methods=['POST'])
    def create_new_questions():
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
            questions = Question.query.all()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)
            #formatted_Question = [question.format() for question in questions]
            #questions_page = formatted_Question[start:end]
            return jsonify({
                'success': True,
                'new_question': question.id,
                'total_questions': len(questions),
                'questions': current_questions
            })

        except:
            abort(422)

    @app.route('/categories/questions', methods=['GET'])
    def view_all_categories():
        categories = Category.query.order_by(Category.type).all()
        return jsonify({
            'success': True,
            'categories': {category.id: category.type for category in categories}
        })

    @app.route('/questions/search', methods=['POST'])
    def search_in_questions():
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        if search_term:
            search_results = Question.query.filter(
                Question.question.ilike(f'%{search_term}%')).all()

            return jsonify({
                'success': True,
                'questions': [question.format() for question in search_results],
                'total_questions': len(search_results),
                'current_category': None
            })
        abort(404)

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def list_all_questions(category_id):
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
        if not (body == None):
            quizzes_category = body.get('quiz_category')
            last_questions = body.get('previous_questions')

            if quizzes_category['type'] == 'click':
                task_questions = Question.query.filter(
                    Question.id.notin_((last_questions))).all()
            else:
                task_questions = Question.query.filter_by(
                    category=quizzes_category['id']).filter(Question.id.notin_((last_questions))).all()

            next_question = task_questions[random.randrange(
                0, len(task_questions))].format() if len(task_questions) > 0 else None

            return jsonify({
                'success': True,
                'question': next_question
            })
        else:
            abort(422)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400


    return app

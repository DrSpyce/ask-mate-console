from data import db_connect


def get_questions():
    sql_request = 'SELECT * FROM questions ORDER BY created_at'
    return db_connect.execute_query(sql_request)


def get_question_with_answers(question_id):
    sql_request = 'SELECT * FROM questions WHERE id = %(question_id)s'
    query_parameters = {"question_id": question_id}
    question = db_connect.execute_query(sql_request, query_parameters)

    if question:
        sql_request = 'SELECT * FROM answers WHERE question_id = %(question_id)s ORDER BY created_at'
        answers = db_connect.execute_query(sql_request, query_parameters)
        return question, answers

from app import create_app, db

application = create_app()


@application.before_first_request
def cria_banco():
    db.create_all()

if __name__ == '__main__':
    application.run(debug=True)
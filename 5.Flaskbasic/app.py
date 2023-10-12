from flask import Flask, Blueprint, render_template

# Declare a Flask App
app = Flask(__name__)


# Created a Blueprint
basic_controller = Blueprint(
    "basic_controller",
    __name__,
    url_prefix="/",
    template_folder="template-assets/templates",
    static_folder="template-assets/assets",
    static_url_path="assets"
)

@basic_controller.route('/', methods=['GET'])
@basic_controller.route('/registration', methods=['GET'])
def registration():
    return render_template("view/registration.html")


@basic_controller.route('/login', methods=['GET'])
def login():
    return render_template("view/login.html")


@basic_controller.route('/forgotpassword', methods=['GET'])
def forgotpassword():
    return render_template("view/forgotpassword.html")

@basic_controller.route('/setpassword', methods=['GET'])
def setpassword():
    return render_template("view/setpassword.html")

@basic_controller.route('/otp', methods=['GET'])
def otp():
    return render_template("view/otp.html")

@basic_controller.route('/resetsuccess', methods=['GET'])
def resetsuccess():
    return render_template("view/resetsuccess.html")

@basic_controller.route('/verificationsuccess', methods=['GET'])
def verificationsuccess():
    return render_template("view/verificationsuccess.html")

@basic_controller.route('/invalidtoken', methods=['GET'])
def invalidtoken():
    return render_template("view/invalidtoken.html")

@basic_controller.route('/notfound', methods=['GET'])
def notfound():
    return render_template("view/notfound.html")

@basic_controller.route('/somethingwrong', methods=['GET'])
def somethingwrong():
    return render_template("view/somethingwrong.html")


# Register the Blueprint
app.register_blueprint(basic_controller)


if __name__ == '__main__':
    app.run(debug=True)

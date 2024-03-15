from forms import ChangePasswordForm, ChangeUsername
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from user import User
from flask import flash


user_profile = Blueprint("user_profile", __name__, template_folder="templates", static_folder="static")

@user_profile.route("/user-profile", methods=["POST", "GET"])
@login_required
def user_profileMain():
    user = current_user
    changePassForm = ChangePasswordForm()
    changeUserForm = ChangeUsername()
    if request.method == "GET":
        return render_template("user_profile/user_profile.html", changePassForm=changePassForm, changeUserForm=changeUserForm)

    else:
        if changePassForm.submitPasswordChange.data and changePassForm.validate():
            # Password change
            oldPassword = changePassForm.oldPassword.data
            newPassword = changePassForm.newPassword.data
            verifyNewPassword = changePassForm.verifyNewPassword.data
            
            user = current_user
            success, message = user.changePassword(oldPassword, newPassword, verifyNewPassword)
            if success:
                message = "Succsesfully changed password !"
                flash(message)
                return render_template("user_profile/user_profile.html", changePassForm=changePassForm, changeUserForm=changeUserForm)
            else:
                flash(message)
                return render_template("user_profile/user_profile.html", changePassForm=changePassForm, changeUserForm=changeUserForm)
            

        elif changeUserForm.submitUsernameChange.data and changeUserForm.validate():
            # Username and Name change 
            newUsername = changeUserForm.newUsername.data
            password = changeUserForm.password.data
            newFirstName = changeUserForm.newFirstName.data
            newLastName = changeUserForm.newLastName.data
            
            user = current_user
            success, message = user.changeNames(password,newUsername,newFirstName,newLastName)
            if success:
                message = "Succsesfully changed User names !"
                flash(message)
                return render_template("user_profile/user_profile.html", changePassForm=changePassForm, changeUserForm=changeUserForm)
            else:
                flash(message)
                return render_template("user_profile/user_profile.html", changePassForm=changePassForm, changeUserForm=changeUserForm)
        
        # Error handling
        else:
            if changePassForm.errors:
                for errors in changePassForm.errors.values():
                    for error in errors:
                        flash(error)
            else:
                for errors in changeUserForm.errors.values():
                    for error in errors:
                        flash(error)
            return render_template("user_profile/user_profile.html", changePassForm=changePassForm,changeUserForm=changeUserForm)


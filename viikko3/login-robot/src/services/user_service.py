import re, sys, pdb
from entities.user import User


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username) < 3:
            raise UserInputError('Username must be 3 or more char')
        if re.search('^[a-z]+$',username) == None:
            raise UserInputError('Username must only contain lowercase a-z')
        if len(password) < 8:
            raise UserInputError('Password must be 8 or more char')
        if re.search('[^a-z]', password) == None:
            raise UserInputError('Password must contain other than a-z char')
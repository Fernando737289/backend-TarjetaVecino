from app.models.user import User

fake_db = []

def create_user(user: User):
    if any(u.id == user.id for u in fake_db):
        return None
    fake_db.append(user)
    return user

def list_users():
    return fake_db
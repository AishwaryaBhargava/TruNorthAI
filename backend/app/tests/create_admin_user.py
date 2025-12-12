# """
# Utility script to bootstrap an admin account in the database.
# Run from the backend directory: `python -m app.tests.create_admin_user --email you@example.com --password StrongPass123!`
# """

# from dotenv import load_dotenv

# # Ensure environment is loaded (points to the correct DB)
# load_dotenv(".env", override=True)

# # Force SQLAlchemy to register all related models before using User
# from app.models import (  # noqa: F401
#     user,
#     chat_history,
#     questionnaire,
#     user_recommendation,
#     user_journey_state,
#     final_data,
#     feedback,
#     career_profile,
#     admin_review,
#     admin_action_log,
# )
# from app.core.database import SessionLocal
# from app.models.user import User
# from app.utils.admin_password import hash_admin_password


# def create_admin(email: str, password: str, firstname: str = "Admin", lastname: str = "User") -> None:
#     db = SessionLocal()
#     try:
#         existing = db.query(User).filter(User.email == email).first()
#         if existing:
#             print(f"User with email {email} already exists (id={existing.id}, role={existing.role}); aborting.")
#             return

#         pw_hash, pw_salt = hash_admin_password(password)
#         admin = User(
#             firstname=firstname,
#             lastname=lastname,
#             email=email,
#             role="admin",
#             admin_password_hash=pw_hash,
#             admin_password_salt=pw_salt,
#         )
#         db.add(admin)
#         db.commit()
#         db.refresh(admin)
#         print(f"Created admin id={admin.id} email={admin.email}")
#     finally:
#         db.close()


# if __name__ == "__main__":
#     import argparse

#     parser = argparse.ArgumentParser(description="Create an admin user in the database.")
#     parser.add_argument("--email", required=True, help="Admin email")
#     parser.add_argument("--password", required=True, help="Admin password (choose a strong unique value)")
#     parser.add_argument("--firstname", default="Admin")
#     parser.add_argument("--lastname", default="User")
#     args = parser.parse_args()

#     create_admin(
#         email=args.email,
#         password=args.password,
#         firstname=args.firstname,
#         lastname=args.lastname,
#     )

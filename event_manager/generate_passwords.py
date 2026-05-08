from werkzeug.security import generate_password_hash

admin_hash  = generate_password_hash("admin123")
viewer_hash = generate_password_hash("viewer123")

print("INSERT INTO Users (username, password, role) VALUES")
print(f"('admin',  '{admin_hash}', 'admin'),")
print(f"('viewer', '{viewer_hash}', 'viewer');")
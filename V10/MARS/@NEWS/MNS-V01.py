from flask import Flask, jsonify
app = Flask(__name__)
posts = [
    {"title": "Test", "date": "2024-01-01", "description": "Description for Post 1"},
    {"title": "Test 1", "date": "2024-01-02", "description": "Description for Post 2"},
]
@app.route('/get_posts', methods=['GET'])
def get_posts():
    return jsonify(posts)
if __name__ == '__main__':
    app.run(debug=True)
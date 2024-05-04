from flask import Flask, request, jsonify
from plagiarism import PlagiarismChecker

app = Flask(__name__)
checker = PlagiarismChecker()

@app.route('/api/plagiarism', methods=['POST'])
def check_plagiarism():
    data = request.json
    text1 = data.get('text1', '')
    text2 = data.get('text2', '')
    
    similarity_percentage = checker.plagiarism_percentage(text1, text2)
    duplicate_sentences = checker.duplicate_sentences(text1, text2)
    
    return jsonify({
        'similarity_percentage': similarity_percentage,
        'duplicate_sentences': duplicate_sentences
    })

if __name__ == "__main__":
    app.run(debug=True)

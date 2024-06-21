from flask import Flask, request, render_template_string
import subprocess
import sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form.get('text')
        if user_input:
            try:
                # modify.py 파일을 실행하고 결과를 받아옵니다.
                result = subprocess.run(
                    [sys.executable, 'modify.py', user_input],
                    capture_output=True, text=True, encoding='utf-8'
                )
                
                stdout_output = result.stdout if result.stdout else "No stdout output"
                stderr_output = result.stderr if result.stderr else "No stderr output"

                print(f"stdout: {stdout_output}")  # stdout 출력
                print(f"stderr: {stderr_output}")  # stderr 출력

                if result.returncode == 0:
                    modified_text = stdout_output.strip()
                    return render_template_string('''
                        <h1>Modified text: {{ modified_text }}</h1>
                        <a href="/">Go back</a>
                    ''', modified_text=modified_text)
                else:
                    return f'Error in processing the request: {stderr_output}', 500
            except Exception as e:
                print(f"Exception occurred: {e}")  # 예외 로그 출력
                return 'Internal Server Error', 500
        else:
            return 'No text provided', 400
    
    return '''
        <form method="post">
            Enter text: <input type="text" name="text">
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(port=5000)

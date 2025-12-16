pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Rajat Pathak\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Check Python') {
            steps {
                bat "\"%PYTHON%\" --version"
            }
        }

        stage('Install Dependencies') {
            steps {
                bat "\"%PYTHON%\" -m pip install --upgrade pip"
                bat "\"%PYTHON%\" -m pip install -r requirements.txt"
            }
        }

        stage('Run Tests') {
            steps {
                bat "\"%PYTHON%\" -m pytest"
            }
        }

        stage('Run App') {
            steps {
                bat "\"%PYTHON%\" app.py"
            }
        }
    }

    post {
        success {
            echo '✅ All tests passed. Build successful!'
        }
        failure {
            echo '❌ Tests failed. Fix the code!'
        }
    }
}

pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Rajat Pathak\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
        IMAGE_NAME = 'jenkins-flask-api'
    }

    stages {

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

        stage('Run Unit Tests') {
            steps {
                bat 'set PYTHONPATH=%CD% && "%PYTHON%" -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Run Docker Container') {
            steps {
                bat "docker run -d -p 5000:5000 %IMAGE_NAME%"
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check above logs.'
        }
    }
}

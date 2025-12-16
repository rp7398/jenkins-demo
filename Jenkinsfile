pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-flask-api"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Code pulled from GitHub automatically'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'pytest'
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
            echo '✅ CI/CD Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Fix errors!'
        }
    }
}

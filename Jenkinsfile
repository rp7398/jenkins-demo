pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\Rajat Pathak\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Code will be checked out by Jenkins'
            }
        }

        stage('Check Python') {
            steps {
                bat "\"%PYTHON%\" --version"
            }
        }

        stage('Run App') {
            steps {
                bat "\"%PYTHON%\" app.py"
            }
        }
    }
}

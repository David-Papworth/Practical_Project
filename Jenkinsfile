pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "docker-compose build --parallel"  
            }
        }
        stage('Test') {
            steps {
                sh "bash test.sh"
            }
        }
    }
}
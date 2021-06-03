pipeline {
    agent any
    environment{
        docker_hub_credentials = credentials('docker-hub-credentials')
    }
    stages {
        stage('Test') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "docker-compose build --parallel"  
            }
        }
        stage('push'){
            steps{
                sh "docker login -u ${docker_hub_credentials_USR} -p ${docker_hub_credentials_PSW}"
                sh "docker-compose push"
            }
        }
        stage('configuration'){
            steps{
                sh "sudo apt install ansible -y"
                sh "bash ansible.sh"
                sh "ansible-playbook -i ./ansible/inventory.yaml ./ansible/playbook.yaml"
            }
        }
        stage('deploy'){
            steps{
                sh "bash deploy.sh"
            }
        }
    }
    post{
        always{
            junit "junit/*.xml"
            cobertura coberturaReportFile: 'coverage.xml', failNoReports:false
        }
    }
    
}
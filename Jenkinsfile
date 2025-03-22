pipeline {
    agent any

    triggers {
        pollSCM '*/5 * * * *' // Poll GitHub every 5 minutes
    }

    environment {
        DOCKER_CREDENTIALS_ID = 'lab_jenkins_PAT'
        GITHUB_REPO = 'https://github.com/ayusao/test_lab.git'
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Cloning the repository from GitHub..."
                    git branch: 'main', credentialsId: "${DOCKER_CREDENTIALS_ID}", url: "${GITHUB_REPO}"
                }
            }
        }
        
        stage('Check Docker Access') { 
            steps {
                script {
                    echo "Checking Docker and Docker Compose versions..."
                    sh 'docker --version'
                    sh 'docker-compose --version'
                    sh 'docker ps'
                }
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    echo "Building frontend and backend Docker images..."
                    sh 'docker build -t Webapp/frontend:latest ./frontend'
                    sh 'docker build -t Webapp/backend:latest ./backend'
                }
            }
        }

        stage('Run Containers') {
            steps {
                script {
                    echo "Stopping existing containers and running new ones..."
                    sh 'docker-compose down || true'
                    sh 'docker-compose up -d --build'
                }
            }
        }
        stage('Deploy with Ansible') {
            steps {
                script {
                    sh 'ansible-playbook -i ansible/hosts ansible/deploy.yml --become'
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution completed!"
        }
    }
    
}

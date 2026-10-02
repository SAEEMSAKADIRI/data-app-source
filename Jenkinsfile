pipeline {
    agent any
    environment {
        // Explicitly adding the path you just found
        PATH = "/usr/local/bin:${env.PATH}"
        
        DOCKER_IMAGE = 'your-dockerhub-username/data-processor'
        IMAGE_TAG = "v${env.BUILD_NUMBER}" 
    }
    stages {
        stage('CI: Test') {
            steps {
                echo "Running tests..."
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest tests/'
            }
        }
        stage('CI: Build & Push') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
            }
        }
        stage('CD: Deploy (The Traditional Way)') {
            steps {
                echo "Jenkins is deploying directly to the server..."
                sh "docker run --rm ${DOCKER_IMAGE}:${IMAGE_TAG}"
            }
        }
    }
}

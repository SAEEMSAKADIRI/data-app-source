pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'your-dockerhub-username/data-processor'
        IMAGE_TAG = "v${env.BUILD_NUMBER}" 
    }
    stages {
        stage('CI: Test') {
            steps {
                echo "Running tests..."
                sh 'pip3 install -r requirements.txt'
                // Using python3 -m ensures it runs regardless of the system PATH
                sh 'python3 -m pytest tests/'
            }
        }
        stage('CI: Build & Push') {
            steps {
                echo "Building Docker image..."
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
                // For the local demo, we are skipping the push to Docker Hub
                // to keep it simple, but we will test that the build works.
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

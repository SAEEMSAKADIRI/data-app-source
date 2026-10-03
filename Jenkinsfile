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
        stage('CD: Deploy (The Traditional Way)') {
            steps {
                echo "Jenkins is deploying directly to the server..."
                // 1. Create the logs directory on your Mac if it doesn't exist
                sh "mkdir -p /Users/saeems.akadiri/data-app-source/logs"
                
                // 2. Run the container with a volume mount (-v)
                sh "docker run --rm -v /Users/saeems.akadiri/data-app-source/logs:/app/logs ${DOCKER_IMAGE}:${IMAGE_TAG}"
            }
        }
    }
}

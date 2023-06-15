pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials("DockerHub")
    }
    stages {
        stage ("SCM Checkout") {
            steps {
                git "https://github.com/devopsxengg/passgen.git"
            }
        }
        stage ("Build Docker Image") {
            steps {
                sh "docker build -t devopsxengg/passgen:$BUILD_NUMBER ."
            }
            
        }
        stage ('DockerHub Login') {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }
        stage ("Push Image to DockerHub") {
            steps {
                sh "docker push devopsxengg/passgen:$BUILD_NUMBER"
            }
        }
         stage ("Pull Image from DockerHub") {
            steps {
                sh "docker pull devopsxengg/passgen:$BUILD_NUMBER"
            }
        }
    }
    post {
        always {
            sh "docker logout"
        }
    }
}

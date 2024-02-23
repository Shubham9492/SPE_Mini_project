//1234
pipeline { 
    agent any
    
    environment {
    DOCKER_IMAGE_NAME ='spe_minipro_cal'
    GITHUB_REPO_URL ='https://github.com/Shubham9492/SPE_Mini_project.git'
    }
    
    stages {
        stage('Clone Git') {
            steps {
                echo "hello"
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x cal.py"
                sh 'printf "1\n25\n" | python3 cal.py'
            }
        }
     stage('Test Code') {
            steps {
                sh "chmod u+x test.py"
                sh "./test.py"
            }
        }
    } 
    
}

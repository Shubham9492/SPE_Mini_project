//123456
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
        stage('Create Docker Image'){
                steps{
                    script{
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                    }
                }
     }
        stage('Docker Image Pushed'){
        	steps{
        	   script{
        	   docker.withRegistry('','caldocker'){
        	   	sh 'docker tag spe_minipro_cal shubham004/spe_minipro_cal:latest'
        	   	sh 'docker push shubham004/spe_minipro_cal'
        	     }
        	   }
        	
            }
        }
        
           stage('Ansible Playbook Run') {
            steps {
                script {
                    ansiblePlaybook(
                    colorized: true,
                    installation: 'ansible',
                    playbook: 'deploy.yml',
                    inventory: 'inventory.ini'
                    )
                }
            }
        }
    } 
    
}

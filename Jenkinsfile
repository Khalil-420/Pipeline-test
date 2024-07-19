node {
    withCredentials([usernamePassword(credentialsId: 'docker_creds', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
        DOCKER_HUB_CREDENTIALS = "${DOCKER_HUB_USERNAME}:${DOCKER_HUB_PASSWORD}"
    output = "${WORKSPACE}/reports"
}
    stage('Checkout') {

    script {
            git branch: 'main',
                credentialsId: 'xhalyl_github',
                url: 'git@github.com:Khalil-420/Pipeline-test.git'
                }
    }


    stage('GitLeaks Scan') {
        sh "echo ${output}"
            sh "docker run --rm -v \"${WORKSPACE}:/repo\" -v \"${output}/gitleaks-report.txt:/tmp/gitleaks-report.txt\" zricethezav/gitleaks:latest  detect --source /repo --report-path /tmp/gitleaks-report.txt --exit-code 0"
        }
    
    stage('SAST SonarQube'){
        withSonarQubeEnv('devsecops'){
            sh'mvn sonar:sonar'
        }
    }

    stage('Build Docker Image'){
        docker.build("xhalyl/fastapi-app:build","-f Dockerfile .")    
        }

    stage('Push Docker Images'){
        docker.withRegistry("",'xhalyl_docker'){
            docker.image("xhalyl/fastapi-app:build").push()
        }
    }

    stage('Deploy'){
        sh'docker-compose down'
        sh'docker-compose up -d'
    }

    try {
        sh'docker system prune -f'
        echo 'Successfully Deployed'
    }
    catch (Exception e){
        echo 'Pipeline failed'
        throw e
    }
}
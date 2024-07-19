node {
    withCredentials([usernamePassword(credentialsId: 'docker_creds', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USERNAME')]) {
        DOCKER_HUB_CREDENTIALS = "${DOCKER_HUB_USERNAME}:${DOCKER_HUB_PASSWORD}"}
    output = "${WORKSPACE}/reports"
    scannerHome = tool 'sonar';

    stage('Checkout') {
    script {
            git branch: 'main',
                credentialsId: 'xhalyl_github',
                url: 'git@github.com:Khalil-420/Pipeline-test.git'
                }
    }


    stage('GitLeaks Scan') {
            sh "docker run --rm -v \"${WORKSPACE}:/repo\" -v \"${output}:/tmp\" zricethezav/gitleaks:latest  detect --source /repo --report-path /tmp/gitleaks-report.json --exit-code 0"
            withCredentials([string(credentialsId: 'xhalyl_defectdojo', variable: 'API_KEY')]){
            sh "bash defectdojo.sh  \"${API_KEY}\" \"Gitleaks Scan\" \"./reports/gitleaks-report.json\" \"http://localhost:8080\" DevSecOps DevSecOps"
        }
        }
    

    stage('SAST SonarQube'){
        withSonarQubeEnv(credentialsId:'xhalyl_sonar'){
            sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=xhalyl_sonar -o sonar_report.json"
        }
    }

    stage('Build Docker Image'){
        docker.build("xhalyl/fastapi-app:build","-f Dockerfile .")    
        }

    stage('Container Scanning Trivy'){
        sh"docker run --rm -v \"${WORKSPACE}/../:/root/.cache/\" aquasec/trivy:latest image xhalyl/fastapi-app:build --scanners vuln -f json --output /root/.cache/report_trivy.json"
        withCredentials([string(credentialsId: 'xhalyl_defectdojo', variable: 'API_KEY')]){
            sh "bash defectdojo.sh  \"${API_KEY}\" \"Gitleaks Scan\" \"../report_trivy.json\" \"http://localhost:8080\" DevSecOps DevSecOps"
        }
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
        sh"rm -rf ${WORKSPACE}"
        echo 'Successfully Deployed'
    }
    catch (Exception e){
        echo 'Pipeline failed'
        sh"rm -rf ${WORKSPACE}"
        throw e
    }
}